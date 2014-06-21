# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.birth_date'
        db.alter_column('dbapi_user', 'birth_date', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'User.birth_date'
        db.alter_column('dbapi_user', 'birth_date', self.gf('django.db.models.fields.DateField')(default=None))

    models = {
        'dbapi.badge': {
            'Meta': {'object_name': 'Badge', 'ordering': "['level']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'icon': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dbapi.checkin': {
            'Meta': {'object_name': 'Checkin', 'unique_together': "(('user', 'venue'),)", 'ordering': "['user', '-number']"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'process': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.User']", 'related_name': "'checkins'"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Venue']"})
        },
        'dbapi.event': {
            'Meta': {'object_name': 'Event', 'ordering': "['-status', 'end_date']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Categorie']", 'blank': 'True', 'related_name': "'events'"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Item']", 'blank': 'True', 'related_name': "'events'"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3', 'default': "'off'"}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.User']", 'blank': 'True', 'related_name': "'events'"}),
            'venues': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Venue']", 'blank': 'True', 'related_name': "'events'"}),
            'zones': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Zone']", 'blank': 'True', 'related_name': "'events'"})
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
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'purchasers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Purchase']"}),
            'reach': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'speed': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        },
        'dbapi.purchase': {
            'Meta': {'object_name': 'Purchase', 'unique_together': "(('user', 'item'),)", 'ordering': "['user', '-number']"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Item']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.User']", 'related_name': "'purchases'"})
        },
        'dbapi.score': {
            'Meta': {'object_name': 'Score', 'unique_together': "(('user', 'zone'),)", 'ordering': "['user', '-points']"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.User']", 'related_name': "'scores'"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Zone']"})
        },
        'dbapi.unlocking': {
            'Meta': {'object_name': 'Unlocking', 'unique_together': "(('user', 'badge'),)", 'ordering': "['user', '-creation_date']"},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Badge']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.User']", 'related_name': "'badges'"})
        },
        'dbapi.user': {
            'Meta': {'object_name': 'User'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dbapi.User']", 'blank': 'True', 'related_name': "'friends_rel_+'"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'default': "'na'"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'})
        },
        'dbapi.venue': {
            'Meta': {'object_name': 'Venue'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Categorie']", 'related_name': "'venues'"}),
            'checkins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Checkin']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foursquare_url': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Zone']", 'related_name': "'venues'"})
        },
        'dbapi.zone': {
            'Meta': {'object_name': 'Zone', 'ordering': "['id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fill_colour': ('django.db.models.fields.CharField', [], {'max_length': '7', 'default': "'#008800'"}),
            'fill_opacity': ('django.db.models.fields.CharField', [], {'max_length': '3', 'default': "'0.2'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'king': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.User']", 'related_name': "'kingdoms'"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'points': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'scores': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Score']"}),
            'stroke_colour': ('django.db.models.fields.CharField', [], {'max_length': '7', 'default': "'#008800'"}),
            'stroke_opacity': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'1'"}),
            'stroke_weight': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "'4'"})
        }
    }

    complete_apps = ['dbapi']