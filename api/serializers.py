from rest_framework import serializers
from api.models import Category, Game, Review, User, Manager

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name'


class GameSerializer(serializers.Serializer):
    name = serializers.CharField()
    id = serializers.IntegerField(required=False)
    description = serializers.CharField()
    image = serializers.CharField()
    category = CategorySerializer()
    price = serializers.FloatField()
    screenshots = serializers.CharField()
    text = serializers.CharField()

class ReviewSerializer(serializers.Serializer):
    username = serializers.CharField()
    id = serializers.IntegerField(required=False)
    game = GameSerializer()
    text = serializers.CharField()
    rating = serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User,
        fields = 'id','username','password','email'
        
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager,
        fields = 'id','username','password','email'