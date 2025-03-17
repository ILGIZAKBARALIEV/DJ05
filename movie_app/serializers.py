from rest_framework import serializers
from .models import DirectorModel
from .models import MoviesModel
from .models import ReviewModel
from rest_framework.exceptions import ValidationError


class DirectorModelSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    class Meta:
        model = DirectorModel
        fields = 'name id movies_count '.split()
    def get_movies_count(self, director):
        return director.movies.count()

class MoviesModelSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = MoviesModel
        fields = '__all__'

    def get_average_rating(self, movie):
        review = movie.reviews.all()
        if review:
            sum_reviews = sum([review.stars for review in review])
            average = sum_reviews / len(review)
            return average
        return None

class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'



class DirectorsValidateSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate_name(self, name):
        try:
            director = DirectorModel.objects.get(name=name)
        except DirectorModel.DoesNotExist:
            raise ValidationError('Director does not exist')
        return name



class MoviesValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    directors = serializers.ListField(child=serializers.IntegerField(min_value=1),required=False,default=[])

    def validate_title(self, title):
        try:
                MoviesModel.objects.get(title=title)
        except MoviesModel.DoesNotExist:
            raise ValidationError('title does not exist')
        return title


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movies = serializers.IntegerField()


    def validate_text(self, text):
        try:
            ReviewModel.objects.get(text=text)
        except ReviewModel.DoesNotExist:
            raise ValidationError('text does not exist')
        return text





