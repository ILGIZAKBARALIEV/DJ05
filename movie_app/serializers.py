from rest_framework import serializers
from .models import DirectorModel
from .models import MoviesModel
from .models import ReviewModel

class DirectorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields= 'name id '.split()

class DirectorModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields = '__all__'


class MoviesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesModel
        fields = ['title', 'description', 'duration']

class MoviesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesModel
        fields = '__all__'

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'

class ReviewModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'
