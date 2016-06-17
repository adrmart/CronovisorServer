from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def upload_to(instance, filename):
    return 'media/{}/{}'.format(instance.id, filename)

class Street(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField(null=True)
	represent = models.CharField(max_length=120, default="a")
	latitud = models.FloatField(default=41)
	longitud = models.FloatField(default=-4)

	def __unicode__(self):
		return self.name

class Image(models.Model):
	id_street = models.ForeignKey('Street')
	id_marker = models.ForeignKey('Marker')
	orientation = models.IntegerField()
    	image = models.ImageField(blank=True, null=True, upload_to=upload_to)
	title = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	year = models.IntegerField()
	autor = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title

class Marker(models.Model):
	latitud = models.FloatField()
	longitud = models.FloatField()
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=50, null=True)
	num_images = models.IntegerField(default=1)

	def __unicode__(self):
		return self.title
