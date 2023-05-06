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
from my_blog.views import blog, AuthorListView, UltimateRoundabout, UltimateThumbnail, UltimateLatest, \
    ArtRoundabout, ArtThumbnail, ArtLatest, LiteratureRoundabout, LiteratureThumbnail, LiteratureLatest, \
    ScienceRoundabout, ScienceThumbnail, ScienceLatest, EntertainmentRoundabout, EntertainmentThumbnail, EntertainmentLatest

urlpatterns = [
    #path('test_one/', test_one),
    # path('post_detail/', PostDetailView.as_view()),
    # path('post_list/', PostListView.as_view()),
    path('blog/', blog),
    path('author/', AuthorListView.as_view()),

    path('ultimate_roundabout/', UltimateRoundabout.as_view()),
    path('ultimate_thumbnail/', UltimateThumbnail.as_view()),
    path('ultimate_latest/', UltimateLatest.as_view()),

    path('art_roundabout/', ArtRoundabout.as_view()),
    path('art_thumbnail/', ArtThumbnail.as_view()),
    path('art_latest/', ArtLatest.as_view()),

    path('literature_roundabout/', LiteratureRoundabout.as_view()),
    path('literature_thumbnail/', LiteratureThumbnail.as_view()),
    path('literature_latest/', LiteratureLatest.as_view()),

    path('science_roundabout/', ScienceRoundabout.as_view()),
    path('science_thumbnail/', ScienceThumbnail.as_view()),
    path('science_latest/', ScienceLatest.as_view()),

    path('entertainment_roundabout/', EntertainmentRoundabout.as_view()),
    path('entertainment_thumbnail/', EntertainmentThumbnail.as_view()),
    path('entertainment_latest/', EntertainmentLatest.as_view()),
]