# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'RanklistOfProgram'
        db.delete_table('home_ranklistofprogram')

        # Deleting model 'RanklistOfCandidate'
        db.delete_table('home_ranklistofcandidate')

        # Adding model 'Ranking'
        db.create_table('home_ranking', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Candidate'])),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Program'])),
            ('rankofcandidate', self.gf('django.db.models.fields.IntegerField')()),
            ('rankofprogram', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['Ranking'])


    def backwards(self, orm):
        # Adding model 'RanklistOfProgram'
        db.create_table('home_ranklistofprogram', (
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Program'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Candidate'])),
            ('ranking', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['RanklistOfProgram'])

        # Adding model 'RanklistOfCandidate'
        db.create_table('home_ranklistofcandidate', (
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Program'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Candidate'])),
            ('ranking', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['RanklistOfCandidate'])

        # Deleting model 'Ranking'
        db.delete_table('home_ranking')


    models = {
        'home.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'home.program': {
            'Meta': {'object_name': 'Program'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'home.ranking': {
            'Meta': {'object_name': 'Ranking'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Candidate']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Program']"}),
            'rankofcandidate': ('django.db.models.fields.IntegerField', [], {}),
            'rankofprogram': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['home']