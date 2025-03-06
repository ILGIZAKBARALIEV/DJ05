from rest_framework import serializers
from .models import DirectorModel
from .models import MovieModel
from .models import ReviewModel

class DirectorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields= 'name'.split()

class DirectorModelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorModel
        fields = '__all__'


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ['title', 'description', 'duration']

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = '__all__'

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'
