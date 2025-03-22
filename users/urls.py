from django.urls import path
from users import views

urlpatterns = [
    path('registration/',views.registration_api_view),
    path('confirmation/',views.confirmation_api_view),
    path('authorizationgit/', views.authorization_api_view),

]

