#!/usr/bin/env python3
"""Urls for the posts app"""
from django.urls import path
from posts.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]
