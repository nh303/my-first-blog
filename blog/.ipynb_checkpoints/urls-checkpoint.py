from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('', views.ola_blog, name='ola_blog'),
    path('', views.class, name='class'),
    path('', views.object, name='object'),
]