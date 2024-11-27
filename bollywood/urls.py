from django.urls import path

from bollywood.views import *

urlpatterns=[
    path('movies_seen/',movies_seen,name='movies_seen'),

]