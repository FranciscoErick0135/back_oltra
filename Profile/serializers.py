from rest_framework import serializers

#-------------MODELOS-------------
from Profile.models import ProfileModel
from Profile.models import ProfilePersons

class ProfileModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

class ProfilePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePersons
        fields = ('__all__')