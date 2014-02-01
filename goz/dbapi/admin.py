from django.contrib import admin
from dbapi.models import Badge, Categorie, Item, Score, \
  User, Checkin, Event, Purchase, Unlocking, Venue, Zone

# Register your models here.
admin.site.register(User)
admin.site.register(Categorie)
admin.site.register(Zone)
admin.site.register(Venue)
admin.site.register(Item)
admin.site.register(Badge)
admin.site.register(Score)
admin.site.register(Checkin)
admin.site.register(Purchase)
admin.site.register(Unlocking)
admin.site.register(Event)
