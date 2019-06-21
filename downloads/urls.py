from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from downloads import views

urlpatterns = [
	path('downloads', views.downloadList),
	path('downloads/download', views.downloadfile),
	path('soap', views.soap),
]

urlpatterns = format_suffix_patterns(urlpatterns)