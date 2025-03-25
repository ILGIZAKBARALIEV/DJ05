from django.urls import path
from users import views

urlpatterns = [
    path('registration/',views.RegisterAPIView.as_view()),
    path('confirmation/',views.ConfirmAPIView.as_view()),
    path('authorization/', views.AuthAPIView.as_view()),

]

