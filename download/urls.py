from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
	path('api/v1/', include(('downloads.urls', 'downloads'), namespace='downloads')),
    #path('admin/', admin.site.urls),
    path('admin/', admin.site.urls)
]

urlpatterns += [
	path('api/v1/auth', include('rest_framework.urls', namespace='rest_framework'))
]