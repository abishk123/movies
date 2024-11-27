from django.urls import path

from hollywood.views import *

urlpatterns=[
    path('movies_seen/',movies_seen,name='movies_seen'),

]