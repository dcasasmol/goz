# dbapi/models.py

import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User as djangoUser

from .exceptions import UserNotSaved
from utils.views import generate_password, is_valid_password


class User(models.Model):
  '''This class models the *Game of Zones* user model.

  Note:
    This class uses a Django User object to authenticate itself in Django
    authentication system.

  Attributes:
    MALE (str): Male database token.
    FEMALE (str): Female database token.
    NOT_AVAILABLE: (str): Gender gender not available database token.
    GENDER_CHOICES (tuple): Database gender choices.
    id (int): User id.
    user (djangoUser): Django User object.
    username (str): Django User username (*Foursquare* user id).
    password (str): Django User password.
    first_name (str): User first name.
    last_name (str): User last name.
    gender (str): User gender, select one of `GENDER_CHOICES`,
      default to `NOT_AVAILABLE`.
    birth_date (date, optional): User birth date, default None.
    photo (str): User photo slug.
    city (str, optional): User city.
    bio (str, optional): User biography.
    email (str, optional): User email.
    facebook (str, optional): User `Facebook` slug.
    twitter (str, optional): User `Twitter` slug.
    friends (list of User, optional): User friends (another User objects).
    creation_date (datetime): User creation datetime.
    last_update (datetime): User last update datetime.

  '''
  MALE = 'ma'
  FEMALE = 'fe'
  NOT_AVAILABLE = 'na'
  GENDER_CHOICES = (
    (NOT_AVAILABLE, 'TOKEN_NA'),
    (MALE, 'TOKEN_MALE'),
    (FEMALE, 'TOKEN_FEMALE'),
  )

  id = models.AutoField(primary_key=True)
  user = models.OneToOneField(djangoUser, related_name='goz_user')
  username = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  gender = models.CharField(max_length=2,
                            choices=GENDER_CHOICES,
                            default=NOT_AVAILABLE)
  birth_date = models.DateField(blank=True, null=True, default=None)
  photo = models.SlugField(max_length=255)
  city = models.CharField(max_length=255, blank=True)
  bio = models.TextField(blank=True)
  email = models.EmailField(blank=True)
  facebook = models.SlugField(max_length=255, blank=True)
  twitter = models.SlugField(max_length=255, blank=True)
  friends = models.ManyToManyField('self', blank=True, symmetrical=True)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)

  def change_password(self, new_pw):
    '''Changes the current password by a given new one.

    Only changes the password if the user is saved (`user` attribute has a
    Django User object instance) and `new_pw` is a valid password.

    Note:
      Uses `set_password` methods of Django User model.

    Args:
      new_pw (str): New password.

    Raises:
      UserNotSaved: If the user is not saved (`user` attribute has a Django
        User object instance).
      ValidationError: If `new_pw` is not a valid password.

    '''
    if self.user_id:

      if is_valid_password(new_pw):
        old_pw = self.password

        try:

          self.user.set_password(new_pw)
          self.password = new_pw

          self.save()

        except Exception as e:

          self.user.set_password(old_pw)
          self.user.save()

      else:
        raise ValidationError

    else:
      raise UserNotSaved

  def enable(self):
    '''Sets the `is active` attribute of Django User model to True.

    Only enables the user if is saved (`user` attribute has a Django User
    object instance).

    Note:
      Uses `is_active` attribute of Django User model.

    Raises:
      UserNotSaved: If the user is not saved (`user` attribute has a Django
        User object instance).

    '''
    if self.user_id and not self.is_active:
      self.user.is_active = True
      self.user.save()
    elif not self.user_id:
      raise UserNotSaved

  def disable(self):
    '''Sets the `is active` attribute of Django User model to False.

    Only disables the user if is saved (`user` attribute has a Django User
    object instance).

    Note:
      Uses `is_active` attribute of Django User model.

    Raises:
      UserNotSaved: If the user is not saved (`user` attribute has a Django
        User object instance).

    '''
    if self.user_id and self.is_active:
      self.user.is_active = False
      self.user.save()
    elif not self.user_id:
      raise UserNotSaved

  @property
  def full_name(self):
    '''Gets the full name of the user.

    Returns:
      str: The first_name plus the last_name, separated by a space.

    '''
    return ' '.join([self.first_name, self.last_name])

  @property
  def is_active(self):
    '''Checks if the user is active.

    Note:
      Uses `is_active` attribute of Django User model.

    Returns:
      bool: True if successful, False otherwise.

    '''
    return self.user.is_active if self.user_id else False

  @property
  def is_female(self):
    '''Checks if the user is female.

    Returns:
      bool: True if successful, False otherwise.

    '''
    return self.gender == self.FEMALE

  def is_friend(self, user):
    '''Checks if a given User is friend or not.

    Args:
      user (User): User object to check.

    Returns:
      bool: True if successful, False otherwise.

    '''
    return user in self.friends

  @property
  def is_male(self):
    '''Checks if the user is male.

    Returns:
      bool: True if successful, False otherwise.

    '''
    return self.gender == self.MALE

  @property
  def last_login(self):
    '''Gets the datetime of the user's last login.

    Note:
      Uses `last_login` attribute of Django User model.

    Returns:
      datetime: User's last login.

    '''
    return self.user.last_login

  @property
  def num_badges(self):
    '''Gets the badges number of the user.

    Returns:
      int: Badges number.

    '''
    return self.badges.filter(user=self).count()

  @property
  def num_checkins(self):
    '''Gets the checkins number of the user.

    Returns:
      int: Checkins number.

    '''
    return self.checkins.filter(user=self).count()

  @property
  def num_friends(self):
    '''Gets the friends number of the user.

    Returns:
      int: Friends number.

    '''
    return self.friends.count()

  @property
  def num_kingdoms(self):
    '''Gets the kingdoms number of the user.

    Returns:
      int: Kingdoms number.

    '''
    return self.kingdoms.count()

  @property
  def num_purchases(self):
    '''Gets the purchases number of the user.

    Returns:
      int: Purchases number.

    '''
    return self.purchases.filter(user=self).count()

  def _process_gender(self, raw_gender):
    '''Processes a raw gender to store it in databse.

    Args:
      raw_gender (str): Raw gender.

    Returns:
      str: Processed gender.

    '''
    if raw_gender.lower() in ['male', 'masculine', 'man']:
      gender = self.MALE
    elif raw_gender.lower() in ['female', 'feminine', 'woman']:
      gender = self.FEMALE
    else:
      gender = self.NOT_AVAILABLE

    return gender

  def reset_password(self):
    '''Resets the current password by a random one.

    Only resets the password if the user is saved (`user` attribute has a
    Django User object instance).

    Note:
      Uses `set_password` methods of Django User model.

    Raises:
      UserNotSaved: If the user is not saved (`user` attribute has a Django
        User object instance).

    '''
    if self.user_id:
      old_pw = self.password

      try:

        random_pw = generate_password(size=8)

        self.user.set_password(random_pw)
        self.password = random_pw

        self.save()

      except Exception as e:

        self.user.set_password(old_pw)
        self.user.save()

    else:
      raise UserNotSaved

  def save(self, *args, **kwargs):
    '''Saves the User object creating/updating the Django User model.

    Args:
      *args: Variable length argument list.
      **kwargs: Arbitrary keyword arguments.

    '''
    if not self.user_id:
      # If User not has Django user object, creates a new one.
      self.password = generate_password(size=8)
      hashed_password = make_password(self.password)

      self.user = djangoUser.objects.create(username=self.username,
                                            password=hashed_password)

    # Updates Django user attributes.
    self.user.first_name = self.first_name
    self.user.last_name = self.last_name
    self.user.email = self.email
    self.user.save()

    self.gender = self._process_gender(self.gender)

    # Finally, saves User object.
    super(User, self).save(*args, **kwargs)

  def __str__(self):
    '''Displays a human-readable representation of the User object.

    Returns:
      str: Human-readable representation of the User object.

    '''
    return '[%s] %s %s' % (self.username,
                           self.first_name,
                           self.last_name)

  @property
  def total_score(self):
    '''Gets the total score of the user.

    Returns:
      int: Total score.

    '''
    return self.scores.filter(user=self).aggregate(sum=Sum('points'))['sum']


class Categorie(models.Model):
  '''This class models a *Foursquare* categorie.

  Attributes:
    id (int): Categorie id.
    name (str): Categorie name.
    icon (str): Categorie icon slug.
    creation_date (datetime): Categorie creation datetime.
    last_update (datetime): Categorie last update datetime.
    active (bool): If the categorie is active or not, default True.

  '''
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  icon = models.SlugField(max_length=255)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def enable(self):
    '''Sets the `active` attribute of the Categorie to True.

    '''
    if not self.is_active:
      self.active = True
      self.save()

  def disable(self):
    '''Sets the `active` attribute of the Categorie to False.

    '''
    if self.is_active:
      self.active = False
      self.save()

  @property
  def is_active(self):
    '''Checks if the Categorie is active.

    Returns:
      bool: True if active, False otherwise.

    '''
    return self.active

  @property
  def num_venues(self):
    '''Gets the venues number of the Categorie.

    Returns:
      int: Venues number.

    '''
    return self.venues.count()

  def __str__(self):
    '''Displays a human-readable representation of the Categorie object.

    Returns:
      str: Human-readable representation of the Categorie object.

    '''
    return self.name

  @property
  def related_events(self):
    '''Gets events related to the Categorie.

    Returns:
      QuerySet: Event objects related to the Categorie.

    '''
    return self.events.all()

  @property
  def related_venues(self):
    '''Gets venues related to the Categorie.

    Returns:
      QuerySet: Venue objects related to the Categorie.

    '''
    return self.venues.all()


class Zone(models.Model):
  '''This class models a *Game of Zones* zone.

  A zone is a part of a town/city where you can make checkins to get points.
  The user with the highest score in a zone is called king.

  Attributes:
    id (int): Zone id.
    name (str): Zone name.
    king (User): Zone king.
    stroke_colour (str): Zone border colour, default '#008800'.
    stroke_weight (str): Zone border weight, default '4',
    stroke_opacity (str): Zone border opacity, default '1',
    fill_colour (str): Zone fill colour, default '#008800',
    fill_opacity (str): Zone fill opacity, default '0.2',
    points (str): A list of points which mark off the zone.
    scores (list of Score): Scores in the Zone for many users.
    creation_date (datetime): Zone creation datetime.
    last_update (datetime): Zone last update datetime.
    active (bool): If the categorie is active or not, default True.

  '''
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  king = models.ForeignKey(User,
                          related_name='kingdoms',
                          related_query_name='kingdom')
  stroke_colour = models.CharField(max_length=7, default='#008800')
  stroke_weight = models.CharField(max_length=1, default='4')
  stroke_opacity = models.CharField(max_length=1, default='1')
  fill_colour = models.CharField(max_length=7, default='#008800')
  fill_opacity = models.CharField(max_length=3, default='0.2')
  points = models.TextField(blank=True)
  scores = models.ManyToManyField(User, through='Score')
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    '''Zone model metadata

    Attributes:
      ordering (list of str): Fields to order by in queries.

    '''
    ordering = ['id']

  def enable(self):
    '''Sets the `active` attribute of the Zone to True.

    '''
    if not self.is_active:
      self.active = True
      self.save()

  def disable(self):
    '''Sets the `active` attribute of the Zone to False.

    '''
    if self.is_active:
      self.active = False
      self.save()

  @property
  def is_active(self):
    '''Checks if the Zone is active.

    Returns:
      bool: True if active, False otherwise.

    '''
    return self.active

  @property
  def num_venues(self):
    '''Gets the venues number of the Zone.

    Returns:
      int: Venues number.

    '''
    return self.venues.count()

  def __str__(self):
    '''Displays a human-readable representation of the Zone object.

    Returns:
      str: Human-readable representation of the Zone object.

    '''
    return self.name

  @property
  def total_score(self):
    '''Gets the total score of the Zone.

    Returns:
      int: Total score.

    '''
    return self.scores.filter(zone=self).aggregate(sum=Sum('points'))['sum']

  @property
  def related_events(self):
    '''Gets events related to the Zone.

    Returns:
      QuerySet: Event objects related to the Zone.

    '''
    return self.events.all()

  @property
  def related_scores(self):
    '''Gets scores related to the Zone.

    Returns:
      QuerySet: Score objects related to the Zone.

    '''
    return self.score_set.all()

  @property
  def related_venues(self):
    '''Gets venues related to the Zone.

    Returns:
      QuerySet: Venue objects related to the Zone.

    '''
    return self.venues.all()


class Venue(models.Model):
  '''This class models a *Foursquare* venue.

  Attributes:
    id (int): Venue id.
    name (str): Venue name.
    lat (str): Venue latitude.
    lng (str): Venue longitude.
    foursquare_url (str): Venue *Foursquare* url slug.
    categorie (Categorie): Venue categorie.
    zone (Zone): Venue zone.
    checkins (list of Checkin): Checkins in the Zone for many users.
    creation_date (datetime): Venue creation datetime.
    last_update (datetime): Venue last update datetime.
    active (bool): If the Venue is active or not, default True.

  '''
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  lat = models.CharField(max_length=255)
  lng = models.CharField(max_length=255)
  foursquare_url = models.SlugField()
  categorie = models.ForeignKey(Categorie,
                                related_name='venues',
                                related_query_name='venue')
  zone = models.ForeignKey(Zone,
                          related_name='venues',
                          related_query_name='venue')
  checkins = models.ManyToManyField(User, through='Checkin')
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def enable(self):
    '''Sets the `active` attribute of the Venue to True.

    '''
    if not self.is_active:
      self.active = True
      self.save()

  def disable(self):
    '''Sets the `active` attribute of the Venue to False.

    '''
    if self.is_active:
      self.active = False
      self.save()

  @property
  def is_active(self):
    '''Checks if the Venue is active.

    Returns:
      bool: True if active, False otherwise.

    '''
    return self.active

  @property
  def num_checkins(self):
    '''Gets the checkins number of the Venue.

    Returns:
      int: Checkins number.

    '''
    return self.checkins.filter(venue=self).count()

  def __str__(self):
    '''Displays a human-readable representation of the Venue object.

    Returns:
      str: Human-readable representation of the Venue object.

    '''
    return self.name

  @property
  def related_checkins(self):
    '''Gets checkins related to the Venue.

    Returns:
      QuerySet: Checkin objects related to the Venue.

    '''
    return self.checkin_set.all()

  @property
  def related_events(self):
    '''Gets events related to the Venue.

    Returns:
      QuerySet: Event objects related to the Venue.

    '''
    return self.events.all()


class Item(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  attack = models.SmallIntegerField(default=0)
  defense = models.SmallIntegerField(default=0)
  speed = models.SmallIntegerField(default=0)
  reach = models.PositiveSmallIntegerField(default=0)
  price = models.PositiveSmallIntegerField(default=0)
  duration = models.PositiveSmallIntegerField(default=0)
  icon = models.SlugField(max_length=255)
  purchasers = models.ManyToManyField(User, through='Purchase')
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name

  @property
  def is_active(self):
    return self.active

  @property
  def num_purchaser(self):
    return self.purchasers.filter(item=self).count()


class Badge(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  unlock_message = models.CharField(max_length=255)
  level = models.PositiveSmallIntegerField(default=0)
  icon = models.SlugField(max_length=255)
  unlockings = models.ManyToManyField(User, through='Unlocking')
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    ordering = ['level']

  def __str__(self):
    return self.name

  @property
  def is_active(self):
    return self.active

  @property
  def num_unlockings(self):
    return self.unlockings.filter(badge=self).count()


class Score(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User,
                          related_name='scores',
                          related_query_name='score')
  zone = models.ForeignKey(Zone)
  points = models.PositiveIntegerField(default=0)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('user', 'zone')
    ordering = ['user', '-points']

  def __str__(self):
    return '%s:%s [%s]' % (self.user, self.zone, self.points)

  @property
  def is_king(self):
    return self.zone in self.user.kingdoms


class Checkin(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User,
                          related_name='checkins',
                          related_query_name='checkin')
  venue = models.ForeignKey(Venue)
  number = models.PositiveIntegerField(default=0)
  process = models.BooleanField(default=True)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('user', 'venue')
    ordering = ['user', '-number']

  def __str__(self):
    return '%s:%s [%s]' % (self.user, self.venue, self.number)

  @property
  def is_processed(self):
    return self.process


class Purchase(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User,
                          related_name='purchases',
                          related_query_name='purchase')
  item = models.ForeignKey(Item)
  number = models.PositiveIntegerField(default=0)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('user', 'item')
    ordering = ['user', '-number']

  def __str__(self):
    return '%s:%s [%s]' % (self.user, self.item, self.number)

  @property
  def is_expired(self):
    today = datetime.datetime.today()
    delta = datetime.timedelta(days=self.item.duration)

    return (self.creation_date + delta) < today if self.creation_date else None


class Unlocking(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User,
                          related_name='badges',
                          related_query_name='badge')
  badge = models.ForeignKey(Badge)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)

  class Meta:
    unique_together = ('user', 'badge')
    ordering = ['user', '-creation_date']

  def __str__(self):
    return '%s:%s' % (self.user, self.item)


class Event(models.Model):
  ON_EVENT = 'on'
  OFF_EVENT = 'off'
  STATUS_CHOICES = (
    (ON_EVENT, 'TOKEN_ON'),
    (OFF_EVENT, 'TOKEN_OFF'),
  )

  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  start_date = models.DateField()
  end_date = models.DateField()
  status = models.CharField(max_length=3,
                            choices=STATUS_CHOICES,
                            default=OFF_EVENT)
  venues = models.ForeignKey(Venue, blank=True,
                            related_name='events',
                            related_query_name='event')
  zones = models.ForeignKey(Zone, blank=True,
                            related_name='events',
                            related_query_name='event')
  items = models.ForeignKey(Item, blank=True,
                            related_name='events',
                            related_query_name='event')
  categories = models.ForeignKey(Categorie, blank=True,
                            related_name='events',
                            related_query_name='event')
  users = models.ForeignKey(User, blank=True,
                            related_name='events',
                            related_query_name='event')
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    ordering = ['-status', 'end_date']

  def __str__(self):
    return self.name

  @property
  def is_active(self):
    return self.active

  @property
  def is_expired(self):
    return self.end_date < datetime.datetime.today() if self.end_date else None

  @property
  def is_started(self):
    return self.start_date < datetime.datetime.today() if self.start_date else None

  @property
  def is_live(self):
    return self.is_started and not self.is_expired
