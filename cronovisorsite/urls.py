"""files_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include, patterns
from django.contrib import admin
from tfg.views import StreetViewSet, MarkerViewSet, ImageViewSet, ImageFromMarker, ImagesFromStreet 
from rest_framework import routers
from django.conf import settings
router = routers.SimpleRouter()
router.register(r'street', StreetViewSet)
router.register(r'marker', MarkerViewSet)
router.register(r'image', ImageViewSet)

urlpatterns = [ 
	url(r'^admin/', include(admin.site.urls)),
   	url(r'^', include(router.urls)),
	url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        	'document_root': settings.STATIC_ROOT
    	}),
   	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        	'document_root': settings.MEDIA_ROOT
    	}),
	url(r'^imagesmarker/(?P<marker>.+)/$', ImageFromMarker.as_view()),
	url(r'^imagesstreet/(?P<street>.+)/$', ImagesFromStreet.as_view()),
]

