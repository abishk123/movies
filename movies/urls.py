"""
URL configuration for movies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import bollywood,hollywood
from kollywood.views import *
from tollywood.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bollywood/',include('bollywood.urls')),
    path('hollywood/',include('hollywood.urls')),
    path('k_movies_seen/',k_movies_seen,name='k_movies_seen'),
    path('t_movies_seen/',t_movies_seen,name='t_movies_seen'),
    path('t_best_movies/',t_best_movies,name='t_best_movies'),
]
