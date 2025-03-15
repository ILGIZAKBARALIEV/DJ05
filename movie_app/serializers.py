from rest_framework import serializers
from .models import DirectorModel
from .models import MoviesModel
from .models import ReviewModel


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

