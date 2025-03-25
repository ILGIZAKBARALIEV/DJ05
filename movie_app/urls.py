from django.urls import path, include
from movie_app import views
from utils.constants import LIST_CREATE,RETRIEVE_UPDATE_DESTROY


urlpatterns = [
    path('DirectorModel/',views.DirectorListAPIView.as_view()),
    path('DirectorModel/<int:id>/',views.DirectorDetailAPIView.as_view()),
    path('MoviesModel/',views.MoviesListAPIView.as_view()),
    path('MoviesModel/<int:id>/',views.MoviesDetailAPIView.as_view()),
    path('ReviewModel/',views.ReviewsListAPIView.as_view()),
    path('ReviewModel/<int:id>/',views.ReviewsDetailAPIView.as_view()),
]