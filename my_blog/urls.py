"""blog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include


#from my_blog.views import test_one, blog, PostDetailView, PostListView
from my_blog.views import blog, AuthorListView, Ultimate, Art, Literature, SciencePost, Entertainment, detail_post, book_volume, search

urlpatterns = [
    path('blog/', blog),
    path('about/', AuthorListView.as_view(), name="about"),

    path('ultimate/', Ultimate.as_view(), name="ultimate"),

    path('art/', Art.as_view(), name="art"),

    path('literature/', Literature.as_view(), name="literature"),
    path('literature/book-volume/<str:class_name>/<int:id>/', book_volume, name="book_volume"),

    path('science/', SciencePost.as_view(), name="science"),

    path('entertainment/', Entertainment.as_view(), name="entertainment"),

    path('details/<str:class_name>/<int:id>/', detail_post, name='details'),
    path('details/<str:class_name>/<int:id>/<str:state>/', detail_post, name="details"),
    path('details/<str:class_name>/<int:id>/<str:state>/<int:number>/', detail_post, name="details"),

    path('search/', search, name="search"),
]