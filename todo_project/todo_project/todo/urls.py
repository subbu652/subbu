from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('display/', views.display, name="display"),
    path('remove/<int:id>/', views.remove, name="remove"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('finish/<int:id>/', views.finish, name="finish"),
    path("signin/", views.signin, name='signin'),
    path("signup/", views.signup, name='signup'),
    path("signout/", views.signout, name='signout'),
    path("completed/<str:inpt>/", views.completed, name="completed"),
    path('not_started/<str:inpt>/', views.not_started, name="not_started"),
    path('started/<str:inpt>/', views.started, name="started"),
]
