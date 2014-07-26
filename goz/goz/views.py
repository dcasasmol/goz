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
  '''This class models the index template renderer.

  Attributes:
    template_name (str): Template to render.

  '''
  template_name = 'login.html'

  def get(self, request, *args, **kwargs):
    '''Override `get` method of `TemplateView` class.

    Args:
      request (HttpRequest): Request object received.
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      HttpResponse: Response object with the template rendered.

    '''
    # Redirect to home if the user is logged.
    if request.user.is_authenticated():
      return redirect('home')

    return super(Index, self).get(request, *args, **kwargs)


class Home(LoginRequiredMixin, TemplateView):
  '''This class models the home template renderer.

  Attributes:
    template_name (str): Template to render.

  '''
  template_name = 'home.html'


class Login(RedirectView):
  '''This class models the login in the *Game of Zones* authentication system.

  Attributes:
    permanent (bool): If the redirect is permanent, default False.
    url (str): Url to redirect when the user is logged.

  '''
  permanent = False
  url = 'home'

  def get_redirect_url(self, *args, **kwargs):
    '''Override `get_redirect_url` method of `RedirectView` class.

    Args:
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      str: Url of the post-login page.

    '''
    return reverse(self.url)

  def get(self, request, *args, **kwargs):
    '''Override `get` method of `RedirectView` class.

    Args:
      request (HttpRequest): Request object received.
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      HttpResponse: Response object of the `url` attribute.

    '''
    access_token = self.request.session.get('login',{}).get('access_token','')

    if access_token:
      # Gets user info from fousquare api.
      api = FsApi(access_token)
      user_info = api.get_user_info()

      # Logins in User model.
      user = self._login_in_goz(user_info)

      # Logins in Django User model.
      django_logged = self._login_in_django(request, user)

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

  def _login_in_django(self, request, user):
    '''Logins in the Django authentication system.

    Args:
      request (HttpRequest): Request object received.
      user (User): *Game of Zones* User object.

    Returns:
      bool: True if the login has been successfull, False otherwise.

    '''
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

  def _login_in_goz(self, user_info):
    '''Logins in the *Game of Zones* authentication system.

    If the user does not exist in *Game of Zones*, creates it.

    Args:
      user_info (dict): User info from *Foursquare* API.

    Returns:
      User: *Game of Zones* User object who has been logged.

    '''
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


class Logout(RedirectView):
  '''This class models the logout in the *Game of Zones* authentication system.

  Attributes:
    permanent (bool): If the redirect is permanent, default False.
    url (str): Url to redirect when the user is logged out.

  '''
  permanent = False
  url = 'index'

  def get_redirect_url(self, *args, **kwargs):
    '''Override `get_redirect_url` method of `RedirectView` class.

    Args:
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      str: Url of the post-logout page.

    '''
    return reverse(self.url)

  def get(self, request, *args, **kwargs):
    '''Override `get` method of `RedirectView` class.

    Args:
      request (HttpRequest): Request object received.
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      HttpResponse: Response object of the `url` attribute.

    '''
    user_info = request.session.get('login', {}).get('user', {})
    username = user_info.get('username', '')
    full_name = user_info.get('full_name', '')

    if 'login'in self.request.session:
      del self.request.session['login']

    logout(request)
    logger.info('Logout info. User logged out: [%s] %s' % (username, full_name))

    return super(Logout, self).get(request, *args, **kwargs)
