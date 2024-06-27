from django.urls import path
from . import views

urlpatterns = [
    path("", views.index2, name="index"),
    path('delete/<str:city>/', views.delete_item, name='delete_item')
]