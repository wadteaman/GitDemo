from django.urls import path
from . import views
urlpatterns = [
    path('python',views.pythonfile),
]
