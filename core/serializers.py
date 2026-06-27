from rest_framework import serializers
from . models import Job,User,Application
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','created_at']
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title','company','posted_at']
class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id','job','user']