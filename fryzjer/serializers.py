from rest_framework import serializers
from fryzjer.models import User, Visit, Servicee


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Name')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Email', 'Pass')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email', 'Name', 'LastName')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email', 'Pass', 'Name', 'LastName', 'Phone')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('UserId', 'Email', 'Pass', 'Name', 'LastName', 'Phone')

class ServiceeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Servicee
       fields = ('ServiceeId', 'Name', 'Price', 'Time')

class VisitAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('VisitId', 'userr', 'servicee', 'Ddate', 'Hhour', 'Status')

class VisitSerializer(serializers.ModelSerializer):
    servicee = ServiceeSerializer(many=False)
    class Meta:
       model = Visit
       fields = ('VisitId', 'userr', 'Ddate', 'Hhour', 'Status', 'servicee')

class VisitAllSerializer(serializers.ModelSerializer):
    servicee = ServiceeSerializer(many=False)
    userr = ProfileSerializer(many = False)
    class Meta:
       model = Visit
       fields = ('VisitId', 'userr', 'Ddate', 'Hhour', 'Status', 'servicee')

class VisitStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('VisitId', 'Status')