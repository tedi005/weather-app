from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("ab/", views.get_weather_data_for_js, name='prove'),
    path('delete/<str:city>/', views.delete_item, name='delete'),
]

