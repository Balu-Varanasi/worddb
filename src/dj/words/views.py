# -*- coding: utf-8 -*-
from django.http import JsonResponse


def words(request, from_iso, word):
    return JsonResponse({'success': True, 'data': {}})


def word(request, from_iso, word, to_iso):
    return JsonResponse({'success': True, 'data': {}})
