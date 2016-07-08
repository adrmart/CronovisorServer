from models import Street, Image, Marker
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

class StreetSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Street
		fields = ('id', 'name_es', 'description_es', 'description_en', 'represent')

class ImageSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Image
		fields = ('id', 'title_es', 'description_es', 'title_en', 'description_en', 'signatura', 'year', 'autor', 'image', 'id_marker', 'id_street')

class MarkerSerializer(ModelSerializer):
	class Meta:
		model = Marker
		fields = ('id', 'title_es', 'description_es', 'title_en', 'description_en', 'latitud', 'longitud', 'num_images')
