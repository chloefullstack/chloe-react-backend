from rest_framework import serializers

from .models import PuppyInfo

class PuppyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuppyInfo
        fields = '__all__'