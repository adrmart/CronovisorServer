from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def upload_to(instance, filename):
    return 'media/{}/{}'.format(instance.id, filename)

class Street(models.Model):
	name_es = models.CharField(max_length=50, null=True)
	description_es = models.TextField(null=True)
	description_en = models.TextField(null=True)
	represent = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name_es

class Image(models.Model):
	id_street = models.ForeignKey('Street')
	id_marker = models.ForeignKey('Marker')
    	image = models.ImageField(blank=True, null=True, upload_to=upload_to)
	title_es = models.CharField(max_length=50)
	description_es = models.TextField(blank=True, null=True)
	title_en = models.CharField(max_length=50, null=True)
	description_en = models.TextField(blank=True, null=True)
	signatura = models.CharField(max_length=25, null=True)
	year = models.IntegerField()
	autor = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title_es

class Marker(models.Model):
	latitud = models.FloatField()
	longitud = models.FloatField()
	title_es = models.CharField(max_length=50)
	description_es = models.CharField(max_length=100, null=True)
	title_en = models.CharField(max_length=50, null=True)
	description_en = models.CharField(max_length=100, null=True)
	num_images = models.IntegerField(default=1)

	def __unicode__(self):
		return self.title_es
