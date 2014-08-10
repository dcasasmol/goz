# goz/tests.py

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotAllowed

from dbapi.mocks import MockUsersManager
from utils.tests import SessionTestCase


DUMMY_ACCESS_TOKEN = '1AKJB2BU4RZ45OLLLLE2P0V1VWJQRAZEWPCJJSLGR5F2UQRP'


class TestIndex(TestCase):
  def test_index_anonymous(self):
    # GET request to index page.
    response = self.client.get(reverse('index'), follow=True)
    self.assertIn('login.html', response.template_name)

    # POST request to index page.
    response = self.client.post(reverse('index'), follow=True)
    self.assertIsInstance(response, HttpResponseNotAllowed)

  def test_index_logged(self):
    # Creates a user and login.
    user_manager = MockUsersManager()
    user = user_manager.create_mock_user()
    self.client.login(username=user.username, password=user.password)

    # GET request to index page.
    response = self.client.get(reverse('index'), follow=True)
    self.assertRedirects(response, reverse('home'))

    # GET request to index page.
    response = self.client.post(reverse('index'), follow=True)
    self.assertIsInstance(response, HttpResponseNotAllowed)


class TestHome(TestCase):
  def test_home_anonymous(self):
    # GET request to home page.
    response = self.client.get(reverse('home'), follow=True)
    self.assertRedirects(response, reverse('index'))

    # POST request to home page.
    response = self.client.post(reverse('home'), follow=True)
    self.assertRedirects(response, reverse('index'))

  def test_home_logged(self):
    # Creates a user and login.
    user_manager = MockUsersManager()
    user = user_manager.create_mock_user()
    self.client.login(username=user.username, password=user.password)

    # GET request to home page.
    response = self.client.get(reverse('home'), follow=True)
    self.assertIn('home.html', response.template_name)

    # POST request to home page.
    response = self.client.post(reverse('home'), follow=True)
    self.assertIsInstance(response, HttpResponseNotAllowed)


class TestLogin(SessionTestCase):
  def test_login_no_token(self):
    # GET request to home page.
    response = self.client.get(reverse('login'), follow=True)
    self.assertRedirects(response, reverse('index'))

    # POST request to home page.
    response = self.client.post(reverse('login'), follow=True)
    self.assertRedirects(response, reverse('index'))

  def test_login_with_token(self):
    # Sets the access token in session.
    session = self.session
    session['login'] = {
      'access_token': DUMMY_ACCESS_TOKEN,
    }
    session.save()

    # GET request to home page.
    response = self.client.get(reverse('login'), follow=True)
    self.assertRedirects(response, reverse('home'))

    # POST request to home page.
    response = self.client.post(reverse('login'), follow=True)
    self.assertRedirects(response, reverse('home'))


class TestLogout(TestCase):
  def test_logout_with_login_get(self):
    # Creates a user and login.
    user_manager = MockUsersManager()
    user = user_manager.create_mock_user()
    self.client.login(username=user.username, password=user.password)

    # GET request to home page.
    self.assertTrue(user.is_logged)
    response = self.client.get(reverse('logout'), follow=True)
    self.assertRedirects(response, reverse('index'))

    # Updates user object.
    user = user_manager.get_user_by_id(user.id)
    self.assertFalse(user.is_logged)

  def test_logout_with_login_post(self):
    # Creates a user and login.
    user_manager = MockUsersManager()
    user = user_manager.create_mock_user()
    self.client.login(username=user.username, password=user.password)

    # POST request to home page.
    self.assertTrue(user.is_logged)
    response = self.client.post(reverse('logout'), follow=True)
    self.assertRedirects(response, reverse('index'))
    self.assertFalse(user.is_logged)

  def test_logout_no_login(self):
    # GET request to home page.
    response = self.client.get(reverse('logout'), follow=True)
    self.assertRedirects(response, reverse('index'))

    # POST request to home page.
    response = self.client.post(reverse('logout'), follow=True)
    self.assertRedirects(response, reverse('index'))
