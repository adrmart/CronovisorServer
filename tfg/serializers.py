from models import Street, Image, Marker
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

class StreetSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Street
		fields = ('id', 'name', 'description', 'represent', 'latitud', 'longitud')

class ImageSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Image
		fields = ('id', 'title', 'description', 'orientation', 'year', 'autor', 'image', 'id_marker', 'id_street')

class MarkerSerializer(ModelSerializer):
	class Meta:
		model = Marker
		fields = ('id', 'title', 'description', 'latitud', 'longitud', 'num_images')
