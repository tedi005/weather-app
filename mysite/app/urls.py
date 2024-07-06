from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('delete/<str:city>/', views.delete_item, name='delete'),
    path('see-more/<str:city>/', views.see_more, name='see_more'),
]