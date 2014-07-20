# foursquareapi/mixins.py

from django.shortcuts import redirect

class LoginRequiredMixin(object):
  '''Mixin class which requires that the user is authenticated.

  Attributes:
    not_logged_url (str): Url to redirect when the user is not authenticated.

  '''
  not_logged_url = 'index'

  def is_logged(self, request):
    '''Check if the user is logged or not.

    Args:
      request (HttpRequest): Request object received.

    Returns:
      book: True if is logged, False otherwise.

    '''
    return request.user.is_authenticated()

  def redirect_to_login(self, request, *args, **kwargs):
    '''Redirects to the login page.

    Args:
      request (HttpRequest): Request object received.
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      HttpRequest: Request to redirect to the login page.

    '''
    return redirect(self.not_logged_url)

  def dispatch(self, request, *args, **kwargs):
    '''Override the `dispatch` method of the object.

    Checks if the user is logged. If False, redirect to the login page.

    Args:
      request (HttpRequest): Request object received.
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    Returns:
      HttpRequest: If the user is not logged.
      function: Otherwise.

    '''
    if not self.is_logged(request):
      return self.redirect_to_login(request, *args, **kwargs)

    return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
