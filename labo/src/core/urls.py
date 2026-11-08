"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from src.core.controller import Controller as ctr

urlpatterns = [
    path('index', ctr.index, name='index'),
    path('search', ctr.search, name='search'),
    path('search_dataset', ctr.search_dataset, name='search_dataset'),
    path('answer', ctr.answer, name='answer'),
    path('answer_dataset', ctr.answer_dataset, name='answer_dataset'),
    path('test', ctr.test, name='test'),
]
