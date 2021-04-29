from django.urls import path
from heelo import views

urlpatterns = [
    path('', views.heelo, name='heelo'),
]