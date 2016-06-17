from django.shortcuts import render
from models import Street, Marker, Image
from serializers import StreetSerializer, MarkerSerializer, ImageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

class StreetViewSet(ModelViewSet):
	queryset = Street.objects.all()
	serializer_class = StreetSerializer

class MarkerViewSet(ModelViewSet):
	queryset = Marker.objects.all()
	serializer_class = MarkerSerializer

class ImageViewSet(ModelViewSet):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer

class ImageFromMarker(ListAPIView):
	serializer_class = ImageSerializer
	def get_queryset(self):
        	marker = self.kwargs['marker']
        	return Image.objects.filter(id_marker=marker)
class ImagesFromStreet(ListAPIView):
	serializer_class = ImageSerializer
	def get_queryset(self):
		street = self.kwargs['street']
		return Image.objects.filter(id_street=street)

