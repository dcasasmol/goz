# goz/views.py

from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_login
from django.views.generic import RedirectView, TemplateView

from dbapi.models import User
from foursquareapi.models import FsApi
from utils.mixins import LoginRequiredMixin


class Index(TemplateView):
  template_name = 'login.html'

  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)

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
    access_token = self.request.session.get('access_token', '')
    if access_token:
      # Gets user info from fousquare api.
      api = FsApi(access_token)
      user_info = api.get_user_info()

      # Logins in User model.
      user = self.__login_in_goz(user_info)

      # Logins in django User model.
      django_logged = self.__login_in_django(request, user)

      self.request.session['login'] = {}
      self.request.session['login']['user'] = {
        'username': user.username,
        'full_name': user.full_name,
      }
    else:
      print('[ERROR] Access token not found in session')

    return super(Login, self).get(request, *args, **kwargs)

  def __login_in_goz(self, user_info):
    username = user_info.get('response', {}).get('username', '')

    if username:
      defaults = user_info.get('response', {})
      user, created = User.objects.get_or_create(username=username,
                                                  defaults=defaults)

      if created:
        print('[INFO] New user created: %s' % user)
      else:
        print('[INFO] User logged: %s' % user)
    else:
      # TODO Return a 'foursquare user not found' error message.
      print('[ERROR] Foursquare user not found')
      pass

    return user

  def __login_in_django(self, request, user):
    success = False

    djangoUser = authenticate(username=user.username,
                              password=user.password)

    if djangoUser:
      if djangoUser.is_active:
        django_login(request, djangoUser)
        success = True
        # Redirect to a success page.
      else:
        # TODO Return a 'disabled account' error message.
        print('[ERROR] Disabled account')
    else:
      # TODO Return an 'invalid login' error message.
      print('[ERROR] Invalid login')


class Logout(RedirectView):
  permanent = False
  url = 'home'

  def get_redirect_url(self, *args, **kwargs):
    return reverse(self.url)

  def get(self, request, *args, **kwargs):
    user_info = request.session.get('login', {}).get('user', {})
    username = user_info.get('username', '')
    full_name = user_info.get('full_name', '')

    if 'access_token' in self.request.session:
      del self.request.session['access_token']
    if 'login'in self.request.session:
      del self.request.session['login']

    logout(request)
    print('[INFO] User logged out: [%s] %s' % (username, full_name))

    # Redirect the user to show we're done.
    return super(Logout, self).get(request, *args, **kwargs)
