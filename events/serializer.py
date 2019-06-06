from rest_framework import serializers
from .models import Profile,Project
from django.contrib.auth.models import User




class ProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model = Profile
      fields = ('user','avatar','bio')

class  ProjectSerializer(serializers.ModelSerializer):
   class Meta:
      model = Project
      fields = ('title','image','owner')

