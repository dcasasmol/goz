# dbapi/mock.py

from .models import User

class MockUsersManager:
  '''This class models a mock users manager for testing.

  '''
  def __init__(self):
    '''Creates the `MockUsersManager` object and set the attribute.

    Attributes:
      user_id (Generator): Generator to get the id of the user.

    '''
    self.user_id = self._create_generator(100)

  def create_mock_user(self):
    '''Creates a mock user with an unique id.

    Returns:
      User: Mock User object created.
    '''
    user_id = next(self.user_id)
    user = User()
    user.first_name = 'User %s' % user_id
    user.last_name = 'Mock'
    user.username = user_id.zfill(8)
    user.save()

    return user

  def get_all_users(self):
    '''Gets all the mock users.

    Returns:
      list of User: List with all the mock users.
    '''
    return User.objects.all()

  def get_user_by_id(self, identifier):
    '''Gets the mock user with the given id.

    Args:
      identifier (str): User identifier.
    '''
    return User.objects.filter(id = identifier).first()

  def _create_generator(self, max_id):
    '''Creates a generator which return the next id between 1 and `max_id`.

    Args:
      max_id (int): Max id to return.

    Returns:
      str: The next id.
    '''
    n = 1

    while n < max_id:
      yield str(n)
      n += 1
