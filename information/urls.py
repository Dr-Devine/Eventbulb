from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="information_home"),
    path('django_meetup/', views.django_meetup, name="information_django_meetup")
]