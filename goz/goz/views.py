# goz/views.py

from django.http import Http404
from django.shortcuts import render


def login(request):
  try:
    context = {}

    return render(request, 'login.html', context)
  except Exception as e:
    print(e)
    raise Http404
