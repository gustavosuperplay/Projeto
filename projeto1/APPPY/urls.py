from django.urls import path
from APPPY import views

urlpatterns = [
path('', views.nomedafuncaoview, name='view1'),
]