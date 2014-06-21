# dbapi/models.py

import datetime

from django.db import models


class User(models.Model):
  MALE = 'ma'
  FEMALE = 'fe'
  NOT_AVAILABLE = 'na'
  GENDER_CHOICES = (
    (NOT_AVAILABLE, 'TOKEN_NA'),
    (MALE, 'TOKEN_MALE'),
    (FEMALE, 'TOKEN_FEMALE'),
  )

  id = models.CharField(max_length=255, primary_key=True)
  # user = models.OneToOneField(djangoUser, related_name='goz_user')
  # username = models.CharField(max_length=255, unique=True)
  # password = models.CharField(max_length=255)
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

  def __str__(self):
    return '%s %s' % (self.first_name, self.last_name)

  @property
  def num_friends(self):
    return self.friends.count()

  @property 
  def num_kingdoms(self):
    return self.kingdoms.count()

  @property
  def scores(self):
    return self.scores.filter(user=self).aggregate(sum=Sum('points'))['sum']

  @property
  def num_purchases(self):
    return self.purchases.filter(user=self).count()

  @property
  def num_checkins(self):
    return self.checkins.filter(user=self).count()

  @property
  def num_badges(self):
    return self.badges.filter(user=self).count()

  @property
  def is_male(self):
    return self.gender == self.MALE

  @property
  def is_female(self):
    return self.gender == self.FEMALE


class Categorie(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
  name = models.CharField(max_length=255)
  icon = models.SlugField(max_length=255)
  creation_date = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.name

  @property
  def is_active(self):
    return self.active

  @property
  def num_venues(self):
    return self.venues.count()


class Zone(models.Model):
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
    ordering = ['id']

  def __str__(self):
    return self.name

  @property
  def is_active(self):
    return self.active

  @property
  def num_venues(self):
    return self.venues.count()

  @property
  def total_score(self):
    return self.scores.filter(zone=self).aggregate(sum=Sum('points'))['sum']


class Venue(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
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

  def __str__(self):
    return self.name

  @property
  def is_active(self):
    return self.active

  @property
  def num_checkins(self):
    return self.checkins.filter(venue=self).count()


class Item(models.Model):
  id = models.CharField(max_length=255, primary_key=True)
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
  id = models.CharField(max_length=255, primary_key=True)
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
  id = models.CharField(max_length=255, primary_key=True)
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
  id = models.CharField(max_length=255, primary_key=True)
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
  id = models.CharField(max_length=255, primary_key=True)
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
  id = models.CharField(max_length=255, primary_key=True)
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

  id = models.CharField(max_length=255, primary_key=True)
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
