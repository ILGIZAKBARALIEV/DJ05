from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import MoviesModel, DirectorModel, ReviewModel
from .serializers import (DirectorModelSerializer,
                          DirectorModelDetailSerializer,
                          MoviesModelSerializer,
                          ReviewModelSerializer,
                          ReviewModelDetailSerializer,
                          MoviesDetailSerializer,)

@api_view(http_method_names=['GET'])
def director_lis_view(request):
    directors = DirectorModel.objects.all()
    serializer = DirectorModelSerializer(directors, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = DirectorModel.objects.get(id=id)
    except DirectorModel.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data =DirectorModelDetailSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movies_list_api_view(request):
    movies = MoviesModel.objects.all()
    serializer = MoviesModelSerializer(movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movies_detail_api_view(request,id):
    try:
        movie = MoviesModel.objects.get(id=id,)
    except MoviesModel.DoesNotExist:
        return Response(data={'error':'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MoviesDetailSerializer(movie).data
    return Response(data=data)



@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = ReviewModel.objects.all()
    serializer = ReviewModelSerializer(reviews, many=True)
    return Response(data=serializer.data)



@api_view(['GET'])
def reviews_detail_api_view(request,id):
    try:
        review = ReviewModel.objects.get(id=id)
    except ReviewModel.DoesNotExist:
        return Response(data={'error':'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewModelDetailSerializer(review).data
    return Response(data=data)



