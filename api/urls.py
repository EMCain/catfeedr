from django.urls import path

from . import views

urlpatterns = [
    path('next/', views.get_next_cat, name='Next Cat'),
    path('reset/', views.reset_index, name='Reset Index')
]
