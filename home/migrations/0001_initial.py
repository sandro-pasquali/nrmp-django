# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Candidate'
        db.create_table('home_candidate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('home', ['Candidate'])

        # Adding model 'Program'
        db.create_table('home_program', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('home', ['Program'])

        # Adding model 'CandidateRanklist'
        db.create_table('home_candidateranklist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('candidate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Candidate'])),
            ('program_rank', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['CandidateRanklist'])

        # Adding M2M table for field program on 'CandidateRanklist'
        db.create_table('home_candidateranklist_program', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('candidateranklist', models.ForeignKey(orm['home.candidateranklist'], null=False)),
            ('program', models.ForeignKey(orm['home.program'], null=False))
        ))
        db.create_unique('home_candidateranklist_program', ['candidateranklist_id', 'program_id'])

        # Adding model 'ProgramRanklist'
        db.create_table('home_programranklist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Program'])),
            ('candidate_rank', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('home', ['ProgramRanklist'])

        # Adding M2M table for field candidate on 'ProgramRanklist'
        db.create_table('home_programranklist_candidate', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programranklist', models.ForeignKey(orm['home.programranklist'], null=False)),
            ('candidate', models.ForeignKey(orm['home.candidate'], null=False))
        ))
        db.create_unique('home_programranklist_candidate', ['programranklist_id', 'candidate_id'])


    def backwards(self, orm):
        # Deleting model 'Candidate'
        db.delete_table('home_candidate')

        # Deleting model 'Program'
        db.delete_table('home_program')

        # Deleting model 'CandidateRanklist'
        db.delete_table('home_candidateranklist')

        # Removing M2M table for field program on 'CandidateRanklist'
        db.delete_table('home_candidateranklist_program')

        # Deleting model 'ProgramRanklist'
        db.delete_table('home_programranklist')

        # Removing M2M table for field candidate on 'ProgramRanklist'
        db.delete_table('home_programranklist_candidate')


    models = {
        'home.candidate': {
            'Meta': {'object_name': 'Candidate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'home.candidateranklist': {
            'Meta': {'object_name': 'CandidateRanklist'},
            'candidate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Candidate']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Program']", 'symmetrical': 'False'}),
            'program_rank': ('django.db.models.fields.IntegerField', [], {})
        },
        'home.program': {
            'Meta': {'object_name': 'Program'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'home.programranklist': {
            'Meta': {'object_name': 'ProgramRanklist'},
            'candidate': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Candidate']", 'symmetrical': 'False'}),
            'candidate_rank': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Program']"})
        }
    }

    complete_apps = ['home']