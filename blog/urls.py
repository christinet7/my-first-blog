from django.urls import path
from . import views

# add first url pattern
urlpatterns = [
    path( '', views.post_list, name = 'post_list' ) ,
]