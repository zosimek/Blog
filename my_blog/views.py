from django.shortcuts import render
from django.http import HttpResponse
from operator import attrgetter
from itertools import chain
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView
from .models import Expertise, CategoryArt, CategoryLiterature, CategoryScience, CategoryPost,\
    Author, Guest, Artwork, Pattern, Volume, Poem, Book, Chapter, Post, Quote

from .combine_views import AuthorQueryset, ArtQueryset, UltimateQueryset

# Create your views here.
def blog(request):
    return render(request, 'index.html')

#################################################    AUTHOR    #########################################################

class AuthorListView(ListView):
    template_name = 'about.html'
    context_object_name = 'combined'

    def get_queryset(self):
        authors = Author.objects.filter(readyToLaunch=True)

        art_seat = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        chapter_seat = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        poem_seat = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:2]
        post_seat = Post.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:3]

        roundabout = sorted(chain(art_seat, chapter_seat, poem_seat, post_seat),
                            key=attrgetter('date'), reverse=True)

        combined = AuthorQueryset(roundabout,authors)
        return combined

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
                             key=attrgetter('date'), reverse=True)[:10]

        art_finger1 = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        art_finger2 = Artwork.objects.filter(readyToLaunch=True, promote=False).order_by('-date')

        chapter_finger1 = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        chapter_finger2 = Chapter.objects.filter(readyToLaunch=True, promote=False).order_by('-date')

        poem_finger1 = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        poem_finger2 = Poem.objects.filter(readyToLaunch=True, promote=False).order_by('-date')

        post_finger1 = Post.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        post_finger2 = Post.objects.filter(readyToLaunch=True, promote=False).order_by('-date')

        thumbnail = sorted(chain(art_finger1, art_finger2, chapter_finger1, chapter_finger2, poem_finger1, poem_finger2,
                                   post_finger1, post_finger2), key=attrgetter('date'), reverse=True)[1:]


        art_latest = Artwork.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        chapter_latest = Chapter.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        poem_latest = Poem.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        post_latest = Post.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        latest = sorted(chain(art_latest, chapter_latest, poem_latest, post_latest),
                             key=attrgetter('date'), reverse=True)[:1]

        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')

        combined = UltimateQueryset(roundabout, thumbnail, latest, quote)
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
class Art(ListView):
    template_name = 'art.html'
    context_object_name = 'combined'

    def get_queryset(self):

        latest = Artwork.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        latest = sorted(chain(latest), key=attrgetter('date'), reverse=True)[:1]


        roundabout = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:10]

        if latest[0] in roundabout:
            roundabout = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[1:10]
        else:
            roundabout = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:10]

        roundabout = sorted(chain(roundabout), key=attrgetter('date'), reverse=True)[:10]

        thumbnail1 = Artwork.objects.filter(readyToLaunch=True, promote=True).order_by('-date')
        thumbnail2 = Artwork.objects.filter(readyToLaunch=True, promote=False).order_by('-date')

        thumbnail_art = sorted(chain(thumbnail1, thumbnail2), key=attrgetter('date'), reverse=True)

        if latest[0] in thumbnail_art:
            thumbnail_art = sorted(chain(thumbnail1, thumbnail2), key=attrgetter('date'),
                                   reverse=True)[1:]
        else:
            thumbnail_art = sorted(chain(thumbnail1, thumbnail2), key=attrgetter('date'),
                                   reverse=True)


        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        art_categories = CategoryArt.objects.all()

        combined = ArtQueryset(roundabout, thumbnail_art, latest, quote, art_categories)
        return combined

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

        merged_list = sorted(chain(artworks1, artworks2, post1, post2), key=attrgetter('date'), reverse=True)[1:10]
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
class Literature(ListView):
    template_name = 'literature.html'
    context_object_name = 'combined'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='literature')

        roundabout_poems = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:4]
        roundabout_chapters = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:4]
        roundabout_post = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise.id).order_by('-date')[:4]

        roundabout = sorted(chain(roundabout_poems, roundabout_chapters, roundabout_post), key=attrgetter('date'), reverse=True)

        thumbnail_poem1 = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        thumbnail_poem2 = Poem.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        thumbnail_chapter1 = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[2:]
        thumbnail_chapter2 = Chapter.objects.filter(readyToLaunch=True, promote=False).order_by('-date')[:3]

        thumbnail_post1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise.id).order_by('-date')[2:]
        thumbnail_post2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise.id).order_by('-date')[:3]

        thumbnail = sorted(chain(thumbnail_poem1, thumbnail_poem2, thumbnail_chapter1, thumbnail_chapter2,
                                 thumbnail_post1, thumbnail_post2), key=attrgetter('date'), reverse=True)[1:10]

        latest_poems = Poem.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        latest_chapters = Chapter.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        latest_post = Post.objects.filter(readyToLaunch=True, expertise=expertise.id).order_by('-date')[:1]

        latest = sorted(chain(latest_poems, latest_chapters, latest_post), key=attrgetter('date'), reverse=True)[:1]

        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        combined = UltimateQueryset(roundabout, thumbnail, latest, quote)
        return combined

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
                             reverse=True)[1:10]
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
class Science(ListView):
    template_name = 'science.html'
    context_object_name = 'combined'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='science')

        roundabout = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise.id).order_by('-date')[:5]

        thumbnail_model1_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise.id).order_by('-date')[2:]
        thumbnail_model1_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise.id).order_by('-date')[:3]

        thumbnail = sorted(chain(thumbnail_model1_qs1, thumbnail_model1_qs2), key=attrgetter('date'), reverse=True)[1:10]

        post = Post.objects.filter(readyToLaunch=True, expertise=expertise.id).order_by('-date')[:1]

        latest = sorted(chain(post), key=attrgetter('date'), reverse=True)[:1]

        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        combined = UltimateQueryset(roundabout, thumbnail, latest, quote)
        return combined

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
class Entertainment(ListView):
    template_name = 'entertainment.html'
    context_object_name = 'combined'

    def get_queryset(self):
        expertise1 = Expertise.objects.get(expertise='entertainment')
        expertise2 = Expertise.objects.get(expertise='art')

        roundabout1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise1.id).order_by('-date')[:5]
        roundabout2 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise2.id).order_by('-date')[:5]

        roundabout = sorted(chain(roundabout1, roundabout2), key=attrgetter('date'), reverse=True)[1:10]

        thumbnail_model1_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise1.id).order_by('-date')[2:]
        thumbnail_model1_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise1.id).order_by('-date')[:3]

        thumbnail_model2_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise2.id).order_by(
            '-date')[2:]
        thumbnail_model2_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise2.id).order_by(
            '-date')[:3]

        thumbnail = sorted(chain(thumbnail_model1_qs1, thumbnail_model1_qs2, thumbnail_model2_qs1, thumbnail_model2_qs2), key=attrgetter('date'),
                             reverse=True)[1:10]

        latest_post1 = Post.objects.filter(readyToLaunch=True, expertise=expertise1.id).order_by('-date')[:1]
        latest_post2 = Post.objects.filter(readyToLaunch=True, expertise=expertise2.id).order_by('-date')[:1]

        latest = sorted(chain(latest_post1, latest_post2), key=attrgetter('date'), reverse=True)[:1]

        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        combined = UltimateQueryset(roundabout, thumbnail, latest, quote)
        return combined

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
        case "Quote":
            post = get_object_or_404(Quote, pk=id)
        case _:
            post = None

    return render(request, 'detail.html', {'post': post})
