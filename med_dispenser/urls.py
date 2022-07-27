from django.urls import path, include
from .views import helloAPI, bloodSugar

urlpatterns = [
    path("hello/", helloAPI),
    path("<int:id>/", bloodSugar),
]