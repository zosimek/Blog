from django.shortcuts import render
from django.http import HttpResponse
from operator import attrgetter
from itertools import chain
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView
from .models import Expertise, CategoryArt, CategoryLiterature, CategoryScience, CategoryPost,\
    Author, Guest, Artwork, Pattern, Volume, Poem, Book, Chapter, Post

from .combine_views import UltimateQueryset

# Create your views here.
def blog(request):
    return render(request, 'index.html')

#################################################    AUTHOR    #########################################################

class AuthorListView(ListView):
    # model = Author
    template_name = 'author_list.html'

    def get_queryset(self):
        authors = Author.objects.filter(readyToLaunch=True)
        return authors

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

################################################    ULTIMATE    ########################################################

class Ultimate(ListView):
    template_name = 'ultimate.html'
    context_object_name = 'combined'

    def get_queryset(self):
        art_seat = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        chapter_seat = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        poem_seat = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        post_seat = Post.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:3]

        roundabout = sorted(chain(art_seat, chapter_seat, poem_seat, post_seat),
                             key=attrgetter('date'), reverse=True)

        art_finger1 = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        art_finger2 = Artwork.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        chapter_finger1 = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        chapter_finger2 = Chapter.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        poem_finger1 = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        poem_finger2 = Poem.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        post_finger1 = Post.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        post_finger2 = Post.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        thumbnail = sorted(chain(art_finger1, art_finger2, chapter_finger1, chapter_finger2, poem_finger1, poem_finger2,
                                   post_finger1, post_finger2), key=attrgetter('date'), reverse=True)[1:10]


        art_latest = Artwork.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        chapter_latest = Chapter.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        poem_latest = Poem.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        post_latest = Post.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        latest = sorted(chain(art_latest, chapter_latest, poem_latest, post_latest),
                             key=attrgetter('date'), reverse=True)[:1]

        combined = UltimateQueryset(roundabout, thumbnail, latest)
        return combined


class UltimateRoundabout(ListView):
    template_name = 'ultimate_roundabout.html'
    context_object_name = 'roundabout_seats'

    def get_queryset(self):
        model1_qs = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        model2_qs = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        model3_qs = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        model4_qs = Post.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]

        merged_list = sorted(chain(model1_qs, model2_qs, model3_qs, model4_qs),
                             key=attrgetter('date'), reverse=True)
        return merged_list

class UltimateThumbnail(ListView):
    template_name = 'ultimate_thumbnail.html'
    context_object_name = 'thumbnails'

    def get_queryset(self):
        model1_qs1 = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        model1_qs2 = Artwork.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        model2_qs1 = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        model2_qs2 = Chapter.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        model3_qs1 = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        model3_qs2 = Poem.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        model4_qs1 = Post.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        model4_qs2 = Post.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        merged_list = sorted(chain(model1_qs1, model1_qs2, model2_qs1, model2_qs2, model3_qs1, model3_qs2,
                                   model4_qs1, model4_qs2),
                             key=attrgetter('date'), reverse=True)[1:10]
        return merged_list

class UltimateLatest(ListView):
    template_name = 'ultimate_latest.html'
    context_object_name = 'latest'

    def get_queryset(self):
        model1_qs = Artwork.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        model2_qs = Chapter.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        model3_qs = Poem.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        model4_qs = Post.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        merged_list = sorted(chain(model1_qs, model2_qs, model3_qs, model4_qs),
                             key=attrgetter('date'), reverse=True)[:1]
        return merged_list

################################################       ART      ########################################################

class ArtRoundabout(ListView):
    template_name = 'art_roundabout.html'
    context_object_name = 'roundabout_seats'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='art')
        artworks = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:5]
        post = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[:5]

        merged_list = sorted(chain(artworks, post), key=attrgetter('date'), reverse=True)[:10]
        return merged_list


class ArtThumbnail(ListView):
    template_name = 'art_thumbnail.html'
    context_object_name = 'thumbnails'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='art')

        artworks1 = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        artworks2 = Artwork.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        post1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[2:]
        post2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise= expertise.id).order_by('-date')[:3]

        merged_list = sorted(chain(artworks1, artworks2, post1, post2), key=attrgetter('date'), reverse=True)[:10]
        return merged_list

class ArtLatest(ListView):
    template_name = 'art_latest.html'
    context_object_name = 'latest'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='art')
        artwork = Artwork.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        post = Post.objects.filter(readyToLaunch=True, expertise= expertise.id).order_by('-date')[:1]

        merged_list = sorted(chain(artwork, post),
                             key=attrgetter('date'), reverse=True)[:1]
        return merged_list

###############################################    LITERATURE    #######################################################

class LiteratureRoundabout(ListView):
    template_name = 'literature_roundabout.html'
    context_object_name = 'roundabout_seats'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='literature')
        poems = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:4]
        chapters = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:4]
        post = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[:4]

        merged_list = sorted(chain(poems, chapters, post),
                             key=attrgetter('date'), reverse=True)
        return merged_list


class LiteratureThumbnail(ListView):
    template_name = 'literature_thumbnail.html'
    context_object_name = 'thumbnails'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='literature')

        poem1 = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        poem2 = Poem.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        chapter1 = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        chapter2 = Chapter.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        post1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[2:]
        post2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise= expertise.id).order_by('-date')[:3]

        merged_list = sorted(chain(poem1, poem2, chapter1, chapter2, post1, post2), key=attrgetter('date'),
                             reverse=True)[:10]
        return merged_list

class LiteratureLatest(ListView):
    template_name = 'literature_latest.html'
    context_object_name = 'latest'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='literature')
        poems = Poem.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        chapters = Chapter.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        post = Post.objects.filter(readyToLaunch=True, expertise= expertise.id).order_by('-date')[:1]

        merged_list = sorted(chain(poems, chapters, post),
                             key=attrgetter('date'), reverse=True)[:1]
        return merged_list

#################################################    SCIENCE    ########################################################

class ScienceRoundabout(ListView):
    template_name = 'science_roundabout.html'
    context_object_name = 'roundabout_seats'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='science')
        posts = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[:5]

        return posts


class ScienceThumbnail(ListView):
    template_name = 'science_thumbnail.html'
    context_object_name = 'thumbnails'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='science')
        model1_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[2:]
        model1_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise= expertise.id).order_by('-date')[:3]

        merged_list = sorted(chain(model1_qs1, model1_qs2), key=attrgetter('date'),
                             reverse=True)[:10]
        return merged_list


class ScienceLatest(ListView):
    template_name = 'science_latest.html'
    context_object_name = 'latest'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='science')
        post = Post.objects.filter(readyToLaunch=True, expertise= expertise.id).order_by('-date')[:1]

        merged_list = sorted(chain(post),
                             key=attrgetter('date'), reverse=True)[:1]
        return merged_list

##############################################    PERFORMANCE    #######################################################

class EntertainmentRoundabout(ListView):
    template_name = 'entertainment_roundabout.html'
    context_object_name = 'roundabout_seats'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='entertainment')
        posts = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[:5]

        return posts


class EntertainmentThumbnail(ListView):
    template_name = 'entertainment_thumbnail.html'
    context_object_name = 'thumbnails'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='entertainment')
        model1_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise= expertise.id).order_by('-date')[2:]
        model1_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise= expertise.id).order_by('-date')[:3]

        merged_list = sorted(chain(model1_qs1, model1_qs2), key=attrgetter('date'),
                             reverse=True)[:10]
        return merged_list


class EntertainmentLatest(ListView):
    template_name = 'entertainment_latest.html'
    context_object_name = 'latest'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='entertainment')
        post = Post.objects.filter(readyToLaunch=True, expertise= expertise.id).order_by('-date')[:1]

        merged_list = sorted(chain(post),
                             key=attrgetter('date'), reverse=True)[:1]
        return merged_list

########################################################################################################################
##############################################       DETAIL      #######################################################
########################################################################################################################

def detail_post(request, class_name, id):

    match class_name:
        case "Author":
            post = get_object_or_404(Author, pk=id)
        case "Guest":
            post = get_object_or_404(Guest, pk=id)
        case "Artwork":
            post = get_object_or_404(Artwork, pk=id)
        case "Pattern":
            post = get_object_or_404(Pattern, pk=id)
        case "Volume":
            post = get_object_or_404(Volume, pk=id)
        case "Poem":
            post = get_object_or_404(Poem, pk=id)
        case "Book":
            post = get_object_or_404(Book, pk=id)
        case "Chapter":
            post = get_object_or_404(Chapter, pk=id)
        case "Post":
            post = get_object_or_404(Post, pk=id)
        case _:
            post = None

    return render(request, 'detail.html', {'post': post})
