from django.urls import path

from . import views

urlpatterns = [
    path('cat_list/', views.cat_list, name='Cat List'),
]
