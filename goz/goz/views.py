# goz/views.py

from django.http import Http404
from django.shortcuts import render

from utils.debug import handle_exception

def login(request):
  try:
    context = {}

    return render(request, 'login.html', context)
  except:
    handle_exception()
    raise Http404
