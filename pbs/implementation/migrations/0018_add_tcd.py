# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from pbs.implementation.models import TrafficControlDiagram

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        l = [
             ['DPAW001A', 'DPAW001A.pdf'],
             ['DPAW002', 'DPAW002.pdf'],
             ['DPAW003', 'DPAW003.pdf'],
             ['DPAW004', 'DPAW004.pdf'],
             ['DPAW005', 'DPAW005.pdf'],
             ['DPAW006', 'DPAW006.pdf'],
             ['DPAW007', 'DPAW007.pdf'],
             ['DPAW008', 'DPAW008.pdf'],
             ['DPAW008A', 'DPAW008A.pdf'],
             ['DPAW009', 'DPAW009.pdf'],
             ['DPAW001', 'DPAW001.pdf']
            ]

        for i in l:
            TrafficControlDiagram.objects.get_or_create(name=i[0], path=i[1])


    def backwards(self, orm):
        "Write your backwards methods here."

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
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
            'fuel_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.FuelType']", 'null': 'True', 'blank': 'True'}),
            'gfdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gfdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grassland_curing_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grassland_curing_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'Meta': {'ordering': "[u'created']", 'object_name': 'EdgingPlan'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_edgingplan_created'", 'to': u"orm['auth.User']"}),
            'desirable_season': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'ffdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ffdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuel_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.FuelType']", 'null': 'True', 'blank': 'True'}),
            'gfdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gfdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grassland_curing_max': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'grassland_curing_min': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
        u'implementation.ignitiontype': {
            'Meta': {'object_name': 'IgnitionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'implementation.lightingsequence': {
            'Meta': {'ordering': "[u'id']", 'object_name': 'LightingSequence'},
            'cellname': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_lightingsequence_created'", 'to': u"orm['auth.User']"}),
            'ffdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'ffdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'fuel_age': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fuel_age_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fuel_description': ('django.db.models.fields.TextField', [], {}),
            'gfdi_max': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'gfdi_min': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'grassland_curing_max': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'grassland_curing_min': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignition_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['implementation.IgnitionType']", 'symmetrical': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_lightingsequence_modified'", 'to': u"orm['auth.User']"}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']"}),
            'resources': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ros_max': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'ros_min': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'seqno': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'strategies': ('django.db.models.fields.TextField', [], {}),
            'wind_dir': ('django.db.models.fields.TextField', [], {}),
            'wind_max': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'wind_min': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        },
        u'implementation.operationaloverview': {
            'Meta': {'object_name': 'OperationalOverview'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_operationaloverview_created'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'implementation_operationaloverview_modified'", 'to': u"orm['auth.User']"}),
            'overview': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'prescription': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prescription.Prescription']"})
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
            'archive_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
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
        u'prescription.fueltype': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'FuelType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'prescription.prescription': {
            'Meta': {'object_name': 'Prescription'},
            'aircraft_burn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approval_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'approval_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'area': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '1'}),
            'burn_id': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'bushfire_act_zone': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'carried_over': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'closure_officer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'closure'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'contentious': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'contentious_rationale': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'contingencies_migrated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_prescription_created'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['prescription.District']", 'null': 'True', 'blank': 'True'}),
            'endorsement_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'endorsement_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'endorsing_roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['prescription.EndorsingRole']", 'symmetrical': 'False'}),
            'endorsing_roles_determined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'financial_year': ('django.db.models.fields.CharField', [], {'default': "u'2016/2017'", 'max_length': '10'}),
            'forecast_areas': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.ForecastArea']", 'null': 'True', 'blank': 'True'}),
            'forest_blocks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fuel_types': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['prescription.FuelType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ignition_completed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ignition_status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'ignition_status_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_season': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'last_season_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_year': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'last_year_unknown': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': "u'320'", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modifier': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'prescription_prescription_modified'", 'to': u"orm['auth.User']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'perimeter': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '12', 'decimal_places': '1'}),
            'planned_season': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '8', 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'planned_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'blank': 'True'}),
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
            'treatment_percentage': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
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
        }
    }

    complete_apps = ['implementation']
    symmetrical = True
