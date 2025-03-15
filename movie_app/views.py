from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import MoviesModel, DirectorModel, ReviewModel
from  django.db import transaction
from .serializers import (DirectorModelSerializer,
                          MoviesModelSerializer,
                          ReviewModelSerializer)

@api_view(http_method_names=['GET','POST'])
def director_lis_create_view(request):
    if request.method == 'GET':
        directors = DirectorModel.objects.all()
        serializer = DirectorModelSerializer(directors, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        with transaction.atomic():

            name =request.data.get('name')

            print(name)
            directors =DirectorModel.objects.create(name=name)
            return Response(data=DirectorModelSerializer(directors).data,
                            status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def director_detail_api_view(request, id):
    try:
        director = DirectorModel.objects.get(id=id)
    except DirectorModel.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data =DirectorModelSerializer(director).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        with transaction.atomic():
            director.name =request.data.get('name')
            director.save()
            return Response(data=DirectorModelSerializer(director).data,
                            status=status.HTTP_201_CREATED)



@api_view(['GET','POST'])
def movies_list_create_api_view(request):
    if request.method == 'GET':
        movies = MoviesModel.objects.all()
        serializer = MoviesModelSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        with transaction.atomic():
            title =request.data.get('title')
            description =request.data.get('description')
            director =DirectorModel.objects.get(id=request.data.get('director'))
            movies =MoviesModel.objects.create(title=title,description=description,director=director)
            movies.save()
            return Response(data = MoviesModelSerializer(movies).data,
                            status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def movies_detail_api_view(request,id):
    try:
        movie = MoviesModel.objects.get(id=id,)
    except MoviesModel.DoesNotExist:
        return Response(data={'error':'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data =MoviesModelSerializer(movie).data
        return Response(data=data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        with transaction.atomic():
            movie.title =request.data.get('title')
            movie.description =request.data.get('description')
            movie.director =DirectorModel.objects.get(id=request.data.get('director'))
            movie.save()
            return Response(data=MoviesModelSerializer(movie).data,
                            status=status.HTTP_201_CREATED)



@api_view(['GET','POST'])
def reviews_list_create_api_view(request):
    if request.method == 'GET':
        reviews = ReviewModel.objects.all()
        serializer = ReviewModelSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        with transaction.atomic():
            review = ReviewModel.objects.create(review=request.data.get('review'))
            review.review=request.data.get('review')
            review.save()
            return Response(data=ReviewModelSerializer(review).data,
                            status=status.HTTP_201_CREATED)




@api_view(['GET','PUT','DELETE'])
def reviews_detail_api_view(request,id):
    try:
        review = ReviewModel.objects.get(id=id)
    except ReviewModel.DoesNotExist:
        return Response(data={'error':'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewModelSerializer(review).data
        return Response(data=data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        with transaction.atomic():
            review.review = request.data.get('review')
            review.save()
            return Response(data=ReviewModelSerializer(review).data,
                            status=status.HTTP_201_CREATED)






