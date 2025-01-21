from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),  
    path('weather/', views.weather_data, name='weather_data'),
    path("signin/", views.signin, name='signin'),
    path("signup/", views.signup, name='signup'),
    path("signout/", views.signout, name='signout'),
]
