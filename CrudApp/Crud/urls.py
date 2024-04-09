from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_log, name="create_log"),
]