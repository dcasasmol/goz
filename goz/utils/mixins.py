# foursquareapi/mixins.py

from django.shortcuts import redirect

class LoginRequiredMixin(object):
  """
    View mixin which requires that the user is authenticated.
  """
  not_logged_url = 'index'

  def is_logged(self, request):
    return request.user.is_authenticated()

  def redirect_to_login(self, request, *args, **kwargs):
    return redirect(self.not_logged_url)

  def dispatch(self, request, *args, **kwargs):
    if not self.is_logged(request):
      return self.redirect_to_login(request, *args, **kwargs)

    return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
