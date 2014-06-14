# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.active'
        db.add_column('dbapi_item', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Badge.active'
        db.add_column('dbapi_badge', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Event.active'
        db.add_column('dbapi_event', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Venue.active'
        db.add_column('dbapi_venue', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Categorie.active'
        db.add_column('dbapi_categorie', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Zone.active'
        db.add_column('dbapi_zone', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.active'
        db.delete_column('dbapi_item', 'active')

        # Deleting field 'Badge.active'
        db.delete_column('dbapi_badge', 'active')

        # Deleting field 'Event.active'
        db.delete_column('dbapi_event', 'active')

        # Deleting field 'Venue.active'
        db.delete_column('dbapi_venue', 'active')

        # Deleting field 'Categorie.active'
        db.delete_column('dbapi_categorie', 'active')

        # Deleting field 'Zone.active'
        db.delete_column('dbapi_zone', 'active')


    models = {
        'dbapi.badge': {
            'Meta': {'ordering': "['level']", 'object_name': 'Badge'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'icon': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unlock_message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'unlockings': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Unlocking']"})
        },
        'dbapi.categorie': {
            'Meta': {'object_name': 'Categorie'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'icon': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dbapi.checkin': {
            'Meta': {'unique_together': "(('user', 'venue'),)", 'ordering': "['user', '-number']", 'object_name': 'Checkin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'process': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'checkins'", 'to': "orm['dbapi.User']"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Venue']"})
        },
        'dbapi.event': {
            'Meta': {'ordering': "['-status', 'end_date']", 'object_name': 'Event'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['dbapi.Categorie']", 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'items': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['dbapi.Item']", 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'off'", 'max_length': '3'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['dbapi.User']", 'blank': 'True'}),
            'venues': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['dbapi.Venue']", 'blank': 'True'}),
            'zones': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': "orm['dbapi.Zone']", 'blank': 'True'})
        },
        'dbapi.item': {
            'Meta': {'object_name': 'Item'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'attack': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'defense': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'duration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'icon': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'purchasers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Purchase']"}),
            'reach': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'speed': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'dbapi.purchase': {
            'Meta': {'unique_together': "(('user', 'item'),)", 'ordering': "['user', '-number']", 'object_name': 'Purchase'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Item']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchases'", 'to': "orm['dbapi.User']"})
        },
        'dbapi.score': {
            'Meta': {'unique_together': "(('user', 'zone'),)", 'ordering': "['user', '-points']", 'object_name': 'Score'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scores'", 'to': "orm['dbapi.User']"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Zone']"})
        },
        'dbapi.unlocking': {
            'Meta': {'unique_together': "(('user', 'badge'),)", 'ordering': "['user', '-creation_date']", 'object_name': 'Unlocking'},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Badge']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badges'", 'to': "orm['dbapi.User']"})
        },
        'dbapi.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': "orm['dbapi.User']", 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'na'", 'max_length': '2'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'})
        },
        'dbapi.venue': {
            'Meta': {'object_name': 'Venue'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': "orm['dbapi.Categorie']"}),
            'checkins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Checkin']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foursquare_url': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'primary_key': 'True', 'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': "orm['dbapi.Zone']"})
        },
        'dbapi.zone': {
            'Meta': {'ordering': "['id']", 'object_name': 'Zone'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fill_colour': ('django.db.models.fields.CharField', [], {'default': "'#008800'", 'max_length': '7'}),
            'fill_opacity': ('django.db.models.fields.CharField', [], {'default': "'0.2'", 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'king': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'kingdoms'", 'to': "orm['dbapi.User']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'scores': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Score']"}),
            'stroke_colour': ('django.db.models.fields.CharField', [], {'default': "'#008800'", 'max_length': '7'}),
            'stroke_opacity': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            'stroke_weight': ('django.db.models.fields.CharField', [], {'default': "'4'", 'max_length': '1'})
        }
    }

    complete_apps = ['dbapi']