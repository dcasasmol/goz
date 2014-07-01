# goz/views.py

import logging

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login
from django.views.generic import RedirectView, TemplateView

from dbapi.models import User
from goz.settings import LOGGER_NAME
from foursquareapi.models import FsApi
from utils.mixins import LoginRequiredMixin

logger = logging.getLogger(LOGGER_NAME)


class Index(TemplateView):
  template_name = 'login.html'

  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)

    # Redirect to home if the user is logged.
    if request.user.is_authenticated():
      return redirect('home')

    return self.render_to_response(context)


class Home(LoginRequiredMixin, TemplateView):
  template_name = 'home.html'


class Login(RedirectView):
  permanent = False
  url = 'home'

  def get_redirect_url(self, *args, **kwargs):
    return reverse(self.url)

  def get(self, request, *args, **kwargs):
    access_token = self.request.session.get('login',{}).get('access_token','')

    if access_token:
      # Gets user info from fousquare api.
      api = FsApi(access_token)
      user_info = api.get_user_info()

      # Logins in User model.
      user = self.__login_in_goz(user_info)

      # Logins in django User model.
      django_logged = self.__login_in_django(request, user)

      if user and django_logged:
        logger.info('Login info. User logged: %s' % user)
      else:
        #TODO Control if some login fails. Send error message in template.
        logger.info('Login info. Login fails.')

      # Saves user info in session.
      if not 'login' in self.request.session:
        self.request.session['login'] = {}

      self.request.session['login']['user'] = {
        'username': user.username,
        'full_name': user.full_name,
      }
    else:
      logger.error('Login error. Access token not found in session.')

    return super(Login, self).get(request, *args, **kwargs)

  def __login_in_goz(self, user_info):
    username = user_info.get('response', {}).get('username', '')

    if username:
      defaults = user_info.get('response', {})
      user, created = User.objects.get_or_create(username=username,
                                                  defaults=defaults)
      if created:
        logger.info('Login info. New user created: %s' % user)
    else:
      logger.error('Login error. Foursquare username not found.')

    return user

  def __login_in_django(self, request, user):
    success = False

    djangoUser = authenticate(username=user.username,
                              password=user.password)
    if djangoUser:
      if djangoUser.is_active:
        django_login(request, djangoUser)
        success = True
      else:
        logger.warning('Login info. User disabled/inactive: %s' % user)
    else:
      logger.info('Login info. Invalid login for user: %s' % user)

    return success


class Logout(RedirectView):
  permanent = False
  url = 'home'

  def get_redirect_url(self, *args, **kwargs):
    return reverse(self.url)

  def get(self, request, *args, **kwargs):
    user_info = request.session.get('login', {}).get('user', {})
    username = user_info.get('username', '')
    full_name = user_info.get('full_name', '')

    if 'login'in self.request.session:
      del self.request.session['login']

    logout(request)
    logger.info('Logout info. User logged out: [%s] %s' % (username, full_name))

    return super(Logout, self).get(request, *args, **kwargs)
