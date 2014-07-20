# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table('dbapi_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, related_name='goz_user', to=orm['auth.User'])),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2, default='na')),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, default=None, blank=True)),
            ('photo', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('facebook', self.gf('django.db.models.fields.SlugField')(max_length=255, blank=True)),
            ('twitter', self.gf('django.db.models.fields.SlugField')(max_length=255, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('dbapi', ['User'])

        # Adding M2M table for field friends on 'User'
        m2m_table_name = db.shorten_name('dbapi_user_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm['dbapi.user'], null=False)),
            ('to_user', models.ForeignKey(orm['dbapi.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding model 'Categorie'
        db.create_table('dbapi_categorie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('icon', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dbapi', ['Categorie'])

        # Adding model 'Zone'
        db.create_table('dbapi_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('king', self.gf('django.db.models.fields.related.ForeignKey')(related_name='kingdoms', to=orm['dbapi.User'])),
            ('stroke_colour', self.gf('django.db.models.fields.CharField')(max_length=7, default='#008800')),
            ('stroke_weight', self.gf('django.db.models.fields.CharField')(max_length=1, default='4')),
            ('stroke_opacity', self.gf('django.db.models.fields.CharField')(max_length=1, default='1')),
            ('fill_colour', self.gf('django.db.models.fields.CharField')(max_length=7, default='#008800')),
            ('fill_opacity', self.gf('django.db.models.fields.CharField')(max_length=3, default='0.2')),
            ('points', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dbapi', ['Zone'])

        # Adding model 'Venue'
        db.create_table('dbapi_venue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lng', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('foursquare_url', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(related_name='venues', to=orm['dbapi.Categorie'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(related_name='venues', to=orm['dbapi.Zone'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dbapi', ['Venue'])

        # Adding model 'Item'
        db.create_table('dbapi_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('attack', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('defense', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('speed', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('reach', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('price', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('duration', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('icon', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dbapi', ['Item'])

        # Adding model 'Badge'
        db.create_table('dbapi_badge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('unlock_message', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('level', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('icon', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dbapi', ['Badge'])

        # Adding model 'Score'
        db.create_table('dbapi_score', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scores', to=orm['dbapi.User'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbapi.Zone'])),
            ('points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('dbapi', ['Score'])

        # Adding unique constraint on 'Score', fields ['user', 'zone']
        db.create_unique('dbapi_score', ['user_id', 'zone_id'])

        # Adding model 'Checkin'
        db.create_table('dbapi_checkin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='checkins', to=orm['dbapi.User'])),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbapi.Venue'])),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('process', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('dbapi', ['Checkin'])

        # Adding unique constraint on 'Checkin', fields ['user', 'venue']
        db.create_unique('dbapi_checkin', ['user_id', 'venue_id'])

        # Adding model 'Purchase'
        db.create_table('dbapi_purchase', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='purchases', to=orm['dbapi.User'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbapi.Item'])),
            ('number', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('dbapi', ['Purchase'])

        # Adding unique constraint on 'Purchase', fields ['user', 'item']
        db.create_unique('dbapi_purchase', ['user_id', 'item_id'])

        # Adding model 'Unlocking'
        db.create_table('dbapi_unlocking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='badges', to=orm['dbapi.User'])),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dbapi.Badge'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('dbapi', ['Unlocking'])

        # Adding unique constraint on 'Unlocking', fields ['user', 'badge']
        db.create_unique('dbapi_unlocking', ['user_id', 'badge_id'])

        # Adding model 'Event'
        db.create_table('dbapi_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=3, default='off')),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', blank=True, to=orm['dbapi.Venue'])),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', blank=True, to=orm['dbapi.Zone'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', blank=True, to=orm['dbapi.Item'])),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', blank=True, to=orm['dbapi.Categorie'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', blank=True, to=orm['dbapi.User'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('dbapi', ['Event'])


    def backwards(self, orm):
        # Removing unique constraint on 'Unlocking', fields ['user', 'badge']
        db.delete_unique('dbapi_unlocking', ['user_id', 'badge_id'])

        # Removing unique constraint on 'Purchase', fields ['user', 'item']
        db.delete_unique('dbapi_purchase', ['user_id', 'item_id'])

        # Removing unique constraint on 'Checkin', fields ['user', 'venue']
        db.delete_unique('dbapi_checkin', ['user_id', 'venue_id'])

        # Removing unique constraint on 'Score', fields ['user', 'zone']
        db.delete_unique('dbapi_score', ['user_id', 'zone_id'])

        # Deleting model 'User'
        db.delete_table('dbapi_user')

        # Removing M2M table for field friends on 'User'
        db.delete_table(db.shorten_name('dbapi_user_friends'))

        # Deleting model 'Categorie'
        db.delete_table('dbapi_categorie')

        # Deleting model 'Zone'
        db.delete_table('dbapi_zone')

        # Deleting model 'Venue'
        db.delete_table('dbapi_venue')

        # Deleting model 'Item'
        db.delete_table('dbapi_item')

        # Deleting model 'Badge'
        db.delete_table('dbapi_badge')

        # Deleting model 'Score'
        db.delete_table('dbapi_score')

        # Deleting model 'Checkin'
        db.delete_table('dbapi_checkin')

        # Deleting model 'Purchase'
        db.delete_table('dbapi_purchase')

        # Deleting model 'Unlocking'
        db.delete_table('dbapi_unlocking')

        # Deleting model 'Event'
        db.delete_table('dbapi_event')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'db_table': "'django_content_type'", 'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dbapi.badge': {
            'Meta': {'object_name': 'Badge', 'ordering': "['level']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'icon': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dbapi.checkin': {
            'Meta': {'object_name': 'Checkin', 'unique_together': "(('user', 'venue'),)", 'ordering': "['user', '-number']"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'process': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'checkins'", 'to': "orm['dbapi.User']"}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Venue']"})
        },
        'dbapi.event': {
            'Meta': {'object_name': 'Event', 'ordering': "['-status', 'end_date']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categories': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'blank': 'True', 'to': "orm['dbapi.Categorie']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'blank': 'True', 'to': "orm['dbapi.Item']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '3', 'default': "'off'"}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'blank': 'True', 'to': "orm['dbapi.User']"}),
            'venues': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'blank': 'True', 'to': "orm['dbapi.Venue']"}),
            'zones': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'blank': 'True', 'to': "orm['dbapi.Zone']"})
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Item']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'purchases'", 'to': "orm['dbapi.User']"})
        },
        'dbapi.score': {
            'Meta': {'object_name': 'Score', 'unique_together': "(('user', 'zone'),)", 'ordering': "['user', '-points']"},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scores'", 'to': "orm['dbapi.User']"}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Zone']"})
        },
        'dbapi.unlocking': {
            'Meta': {'object_name': 'Unlocking', 'unique_together': "(('user', 'badge'),)", 'ordering': "['user', '-creation_date']"},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dbapi.Badge']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'badges'", 'to': "orm['dbapi.User']"})
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
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'blank': 'True', 'to': "orm['dbapi.User']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2', 'default': "'na'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'twitter': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'related_name': "'goz_user'", 'to': "orm['auth.User']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'dbapi.venue': {
            'Meta': {'object_name': 'Venue'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': "orm['dbapi.Categorie']"}),
            'checkins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dbapi.User']", 'through': "orm['dbapi.Checkin']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foursquare_url': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'venues'", 'to': "orm['dbapi.Zone']"})
        },
        'dbapi.zone': {
            'Meta': {'object_name': 'Zone', 'ordering': "['id']"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fill_colour': ('django.db.models.fields.CharField', [], {'max_length': '7', 'default': "'#008800'"}),
            'fill_opacity': ('django.db.models.fields.CharField', [], {'max_length': '3', 'default': "'0.2'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'king': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'kingdoms'", 'to': "orm['dbapi.User']"}),
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
