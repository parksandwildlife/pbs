# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'EdgingPlan.ffdi_min'
        db.alter_column(u'implementation_edgingplan', 'ffdi_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'EdgingPlan.wind_max'
        db.alter_column(u'implementation_edgingplan', 'wind_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'EdgingPlan.ffdi_max'
        db.alter_column(u'implementation_edgingplan', 'ffdi_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'EdgingPlan.desirable_season'
        db.alter_column(u'implementation_edgingplan', 'desirable_season', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=64, null=True))

        # Changing field 'EdgingPlan.ros_max'
        db.alter_column(u'implementation_edgingplan', 'ros_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'EdgingPlan.location'
        db.alter_column(u'implementation_edgingplan', 'location', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'EdgingPlan.strategies'
        db.alter_column(u'implementation_edgingplan', 'strategies', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'EdgingPlan.ros_min'
        db.alter_column(u'implementation_edgingplan', 'ros_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'EdgingPlan.sdi'
        db.alter_column(u'implementation_edgingplan', 'sdi', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'EdgingPlan.wind_dir'
        db.alter_column(u'implementation_edgingplan', 'wind_dir', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'EdgingPlan.wind_min'
        db.alter_column(u'implementation_edgingplan', 'wind_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.pmc_min'
        db.alter_column(u'implementation_burningprescription', 'pmc_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.rh_max'
        db.alter_column(u'implementation_burningprescription', 'rh_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.temp_min'
        db.alter_column(u'implementation_burningprescription', 'temp_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.wind_max'
        db.alter_column(u'implementation_burningprescription', 'wind_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.max_area'
        db.alter_column(u'implementation_burningprescription', 'max_area', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.temp_max'
        db.alter_column(u'implementation_burningprescription', 'temp_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.ros_max'
        db.alter_column(u'implementation_burningprescription', 'ros_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.ffdi_min'
        db.alter_column(u'implementation_burningprescription', 'ffdi_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.ffdi_max'
        db.alter_column(u'implementation_burningprescription', 'ffdi_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.ros_min'
        db.alter_column(u'implementation_burningprescription', 'ros_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.sdi'
        db.alter_column(u'implementation_burningprescription', 'sdi', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'BurningPrescription.wind_dir'
        db.alter_column(u'implementation_burningprescription', 'wind_dir', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'BurningPrescription.wind_min'
        db.alter_column(u'implementation_burningprescription', 'wind_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.rh_min'
        db.alter_column(u'implementation_burningprescription', 'rh_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.min_area'
        db.alter_column(u'implementation_burningprescription', 'min_area', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.smc_min'
        db.alter_column(u'implementation_burningprescription', 'smc_min', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.glc_pct'
        db.alter_column(u'implementation_burningprescription', 'glc_pct', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.pmc_max'
        db.alter_column(u'implementation_burningprescription', 'pmc_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.scorch'
        db.alter_column(u'implementation_burningprescription', 'scorch', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

        # Changing field 'BurningPrescription.smc_max'
        db.alter_column(u'implementation_burningprescription', 'smc_max', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.ffdi_min'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.ffdi_min' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.wind_max'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.wind_max' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.ffdi_max'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.ffdi_max' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.desirable_season'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.desirable_season' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.ros_max'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.ros_max' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.location'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.location' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.strategies'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.strategies' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.ros_min'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.ros_min' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.sdi'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.sdi' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.wind_dir'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.wind_dir' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'EdgingPlan.wind_min'
        raise RuntimeError("Cannot reverse this migration. 'EdgingPlan.wind_min' and its values cannot be restored.")

        # Changing field 'BurningPrescription.pmc_min'
        db.alter_column(u'implementation_burningprescription', 'pmc_min', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.rh_max'
        db.alter_column(u'implementation_burningprescription', 'rh_max', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.temp_min'
        db.alter_column(u'implementation_burningprescription', 'temp_min', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.wind_max'
        db.alter_column(u'implementation_burningprescription', 'wind_max', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.max_area'
        db.alter_column(u'implementation_burningprescription', 'max_area', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.temp_max'
        db.alter_column(u'implementation_burningprescription', 'temp_max', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.ros_max'
        db.alter_column(u'implementation_burningprescription', 'ros_max', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.ffdi_min'
        db.alter_column(u'implementation_burningprescription', 'ffdi_min', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.ffdi_max'
        db.alter_column(u'implementation_burningprescription', 'ffdi_max', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.ros_min'
        db.alter_column(u'implementation_burningprescription', 'ros_min', self.gf('django.db.models.fields.PositiveIntegerField')())

        # User chose to not deal with backwards NULL issues for 'BurningPrescription.sdi'
        raise RuntimeError("Cannot reverse this migration. 'BurningPrescription.sdi' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'BurningPrescription.wind_dir'
        raise RuntimeError("Cannot reverse this migration. 'BurningPrescription.wind_dir' and its values cannot be restored.")

        # Changing field 'BurningPrescription.wind_min'
        db.alter_column(u'implementation_burningprescription', 'wind_min', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.rh_min'
        db.alter_column(u'implementation_burningprescription', 'rh_min', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.min_area'
        db.alter_column(u'implementation_burningprescription', 'min_area', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.smc_min'
        db.alter_column(u'implementation_burningprescription', 'smc_min', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.glc_pct'
        db.alter_column(u'implementation_burningprescription', 'glc_pct', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.pmc_max'
        db.alter_column(u'implementation_burningprescription', 'pmc_max', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.scorch'
        db.alter_column(u'implementation_burningprescription', 'scorch', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'BurningPrescription.smc_max'
        db.alter_column(u'implementation_burningprescription', 'smc_max', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'implementation.burningprescription': {
            'Meta': {'object_name': 'BurningPrescription'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_burningprescription_created'", 'to': u"orm['auth.User']"}),
            'ffdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ffdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuel_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['implementation.FuelType']"}),
            'glc_pct': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_area': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'min_area': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_burningprescription_modified'", 'to': u"orm['auth.User']"}),
            'pmc_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pmc_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']"}),
            'rh_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rh_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ros_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ros_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'scorch': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sdi': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'smc_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'smc_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temp_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'temp_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wind_dir': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wind_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wind_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'implementation.edgingplan': {
            'Meta': {'object_name': 'EdgingPlan'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_edgingplan_created'", 'to': u"orm['auth.User']"}),
            'desirable_season': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'ffdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ffdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuel_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['implementation.FuelType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_edgingplan_modified'", 'to': u"orm['auth.User']"}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']"}),
            'ros_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ros_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sdi': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'strategies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wind_dir': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'wind_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wind_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'implementation.exclusionarea': {
            'Meta': {'object_name': 'ExclusionArea'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_exclusionarea_created'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'detail': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_exclusionarea_modified'", 'to': u"orm['auth.User']"}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']"})
        },
        u'implementation.fueltype': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'FuelType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_fueltype_created'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_fueltype_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'implementation.ignitiontype': {
            'Meta': {'object_name': 'IgnitionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'implementation.lightingsequence': {
            'Meta': {'unique_together': "((u'prescription', u'seqno'),)", 'object_name': 'LightingSequence'},
            'cellname': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_lightingsequence_created'", 'to': u"orm['auth.User']"}),
            'ffdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ffdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fuel_age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuel_age_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fuel_description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignition_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['implementation.IgnitionType']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_lightingsequence_modified'", 'to': u"orm['auth.User']"}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']"}),
            'resources': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ros_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'ros_min': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'seqno': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'strategies': ('django.db.models.fields.TextField', [], {}),
            'wind_dir': ('django.db.models.fields.TextField', [], {}),
            'wind_max': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'wind_min': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'implementation.roadsegment': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'RoadSegment', '_ormbases': [u'implementation.Way']},
            'road_type': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'traffic_considerations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'traffic_diagram': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['implementation.TrafficControlDiagram']", 'null': 'True', 'blank': 'True'}),
            u'way_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['implementation.Way']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'implementation.signinspection': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'SignInspection'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_signinspection_created'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspected': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'inspector': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_signinspection_modified'", 'to': u"orm['auth.User']"}),
            'way': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['implementation.Way']"})
        },
        u'implementation.trafficcontroldiagram': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'TrafficControlDiagram'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'path': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'implementation.trailsegment': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'TrailSegment', '_ormbases': [u'implementation.Way']},
            'diversion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_signage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stop': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'stop_signage': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'way_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['implementation.Way']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'implementation.way': {
            'Meta': {'object_name': 'Way'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_way_created'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_way_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']"}),
            'signs_installed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'signs_removed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'prescription.district': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'District'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Region']"})
        },
        u'prescription.endorsingrole': {
            'Meta': {'ordering': "[u'index']", 'object_name': 'EndorsingRole'},
            'disclaimer': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '320'})
        },
        u'prescription.forecastarea': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'ForecastArea'},
            'districts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.District']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.prescription': {
            'Meta': {'object_name': 'Prescription'},
            'aircraft_burn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allocation': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'approval_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'approval_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'area': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '1'}),
            'burn_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'bushfire_act_zone': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contentious': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'contentious_rationale': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_prescription_created'", 'to': u"orm['auth.User']"}),
            'district': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['prescription.District']", 'null': 'True', 'blank': 'True'}),
            'endorsement_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'endorsement_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'endorsing_roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.EndorsingRole']", 'symmetrical': 'False'}),
            'endorsing_roles_determined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'forecast_areas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.ForecastArea']", 'null': 'True', 'blank': 'True'}),
            'forest_blocks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignition_completed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ignition_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'ignition_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_season': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'last_season_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'last_year_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': "u'320'", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_prescription_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'perimeter': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '1'}),
            'planned_season': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '64'}),
            'planned_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4'}),
            'planning_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'planning_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'prescribing_officer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'prohibited_period': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purposes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.Purpose']", 'symmetrical': 'False'}),
            'rationale': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Region']"}),
            'regional_objectives': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.RegionalObjective']", 'null': 'True', 'blank': 'True'}),
            'remote_sensing_priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '4'}),
            'shires': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.Shire']", 'null': 'True', 'blank': 'True'}),
            'short_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'tenures': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.Tenure']", 'symmetrical': 'False', 'blank': 'True'}),
            'treatment_percentage': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'vegetation_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.VegetationType']", 'null': 'True', 'blank': 'True'})
        },
        u'prescription.purpose': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Purpose'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'prescription.regionalobjective': {
            'Meta': {'object_name': 'RegionalObjective'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_regionalobjective_created'", 'to': u"orm['auth.User']"}),
            'fma_names': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'impact': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_regionalobjective_modified'", 'to': u"orm['auth.User']"}),
            'objectives': ('django.db.models.fields.TextField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Region']"})
        },
        u'prescription.shire': {
            'Meta': {'ordering': "[u'name']", 'unique_together': "((u'name', u'district'),)", 'object_name': 'Shire'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.tenure': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Tenure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.vegetationtype': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'VegetationType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['implementation']