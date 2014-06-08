# goz/views.py

from django.views.generic import TemplateView

from foursquareapi.models import FsApi
from utils.mixins import LoginRequiredMixin

class Index(TemplateView):
  template_name = 'login.html'


class Home(LoginRequiredMixin, TemplateView):
  template_name = 'home.html'

  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)

    access_token = self.request.session.get('access_token', '')
    if access_token:
      api = FsApi(access_token)

      user_info = api.get_user_info()
      username = user_info['response']['user']['firstName']

      context['username'] = username

    else:
      print('[ERROR] Access token not found in session')

    return self.render_to_response(context)
