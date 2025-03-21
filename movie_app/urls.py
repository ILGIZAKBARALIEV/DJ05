from django.urls import path
from movie_app import views


urlpatterns = [
    path('',views.director_lis_create_view),
    path('<int:id>/',views.director_detail_api_view),
    path('',views.movies_list_create_api_view),
    path('<int:id>/',views.movies_detail_api_view),
    path('',views.reviews_list_create_api_view),
    path('<int:id>/',views.reviews_detail_api_view),
]