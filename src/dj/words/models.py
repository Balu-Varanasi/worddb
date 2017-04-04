# -*- coding: utf-8 -*-
"""`words` models."""
from django.contrib.postgres import fields as postgres_fields
from django.db import models

from . import constants


class Language(models.Model):
    iso = models.CharField(max_length=3)


class WordRelation(models.Model):
    # plural, present-contineous, past, future, typo
    name = models.CharField(max_length=64)


class Accent(models.Model):
    name = models.CharField(max_length=64)  # American, British, Wales


class System(models.Model):
    name = models.CharField(max_length=64)  # IPA vs ARPA vs "Native"
    code = models.CharField(max_length=64)  # ipa vs native_hi
    language = models.ForeignKey(Language, null=True)


class Word(models.Model):
    language = models.ForeignKey(Language)

    # /en/Love_(Feeling) vs /en/Love_(Score): wikipedia style
    text = models.CharField(max_length=200)

    # {
    #     "ipa": {
    #         "American": "asdasdasd",
    #     }
    # }
    pronunciation = postgres_fields.JSONField()
    # American: /ˈkwɛst͡ʃən/ British: /ˈkwɛʃt͡ʃən/
    # ipa = pg.JSONField(max_length=200)
    # arpa = pg.JSONField(max_length=200)
    # brahmic = pg.JSONField(max_length=200)
    # telugu = pg.JSONField(max_length=200)

    # Loves etc are roots
    root = models.ForeignKey("Word", null=True, blank=True)
    root_relation = models.ForeignKey(WordRelation)
    disambiguation = models.CharField(max_length=200, blank=True)
    # TODO: Do we need this? Can we use WordRelation model?
    pos = models.CharField(max_length=64, choices=constants.PARTS_OF_SPEECH)

    class Meta:
        unique_together = ('language', 'text', 'disambiguation')

# like, love
#
# loves, loved, loving
#
# NASA vs N.A.S.A vs
# Nasa / en / NASA_(Space_Organization) vs / en / Nasa_(City)


class WordInfo(models.Model):
    word = models.ForeignKey(Word)
    language = models.ForeignKey(Language)
    # all meanings of english word love in hindi
    meanings = models.ManyToManyField(Word, related_name='meanings')
    # all anotnyms of english word love in hindi
    antonyms = models.ManyToManyField(Word, related_name='antonyms')
    synonyms = models.ManyToManyField(Word, related_name='synonyms')
    text = models.TextField(blank=True)


# URL:
#
# // word URL: /en/love/
# // /en/love/hi/ (I know hindi, so prefer hindi meaning etc)
