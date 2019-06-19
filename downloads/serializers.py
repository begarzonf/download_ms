from rest_framework import serializers
from .models import download

class downloadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = download
		fields = ('id', 'path', 'description', 'owner')