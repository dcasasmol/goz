# utils/test.py

from django.test import TestCase
from django.conf import settings
from django.utils.importlib import import_module


class SessionTestCase(TestCase):
  '''This class models a TestCase with the session engine actived.

    Use:
      class SampleTestClass(SessionTestCase):

        def test_sample_with_session(self):
          session = self.session
          session['key'] = 'value'
          session.save()

    Note:
      Snippet related to this issue: http://code.djangoproject.com/ticket/10899

  '''
  def setUp(self):
    '''Sets the session engine and activates it.

    '''
    # Imports session engine.
    settings.SESSION_ENGINE = 'django.contrib.sessions.backends.file'
    engine = import_module(settings.SESSION_ENGINE)

    # Creates a session store.
    store = engine.SessionStore()
    store.save()

    # Sets the session store as the current session.
    self.session = store
    self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key
