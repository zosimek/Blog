from datetime import datetime, timedelta
from string import digits

from django.shortcuts import render
from django.http import HttpResponse
from operator import attrgetter
from itertools import chain
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView
from .models import Expertise, CategoryArt, CategoryLiterature, CategoryScience, CategoryPost, \
    Author, Guest, Artwork, Pattern, Volume, Poem, Book, Chapter, Post, Science, Quote

from .combine_views import AuthorQueryset, ArtQueryset, UltimateQueryset, LiteratureQueryset, BookVolumeQueryset, \
    LastPoemBook, Search, SearchResult


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

        combined = AuthorQueryset(roundabout, authors)
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


###############################################    LITERATURE    #######################################################
class Literature(ListView):
    template_name = 'literature.html'
    context_object_name = 'combined'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='literature')

        roundabout_poems = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:4]
        roundabout_chapters = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')[:4]

        roundabout = sorted(chain(roundabout_poems, roundabout_chapters), key=attrgetter('date'), reverse=True)

        books_volumes1 = Book.objects.filter(readyToLaunch=True)
        books_volumes2 = Volume.objects.filter(readyToLaunch=True)

        books_volumes = chain(books_volumes1, books_volumes2)

        thumbnail_poem1 = Poem.objects.filter(readyToLaunch=True, promote=True).order_by('-date')
        thumbnail_poem2 = Poem.objects.filter(readyToLaunch=True, promote=False).order_by('-date')

        thumbnail_chapter1 = Chapter.objects.filter(readyToLaunch=True, promote=True).order_by('-date')
        thumbnail_chapter2 = Chapter.objects.filter(readyToLaunch=True, promote=False).order_by('-date')

        thumbnail = sorted(chain(thumbnail_poem1, thumbnail_poem2, thumbnail_chapter1, thumbnail_chapter2),
                           key=attrgetter('number'))

        latest_poems = Poem.objects.filter(readyToLaunch=True).order_by('-date')[:1]
        latest_chapters = Chapter.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        latest = sorted(chain(latest_poems, latest_chapters), key=attrgetter('date'), reverse=True)[:1]

        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        literature_genre = CategoryLiterature.objects.all()

        current_date = datetime.now().date()
        two_weeks_back = current_date - timedelta(days=14)

        combined = LiteratureQueryset(roundabout, books_volumes, thumbnail, latest, quote, literature_genre,
                                      current_date, two_weeks_back)
        return combined


def book_volume(request, class_name, id):
    match class_name:
        case "Book":
            book_volume_info = get_object_or_404(Book, pk=id)
            book_volume_content = Chapter.objects.filter(readyToLaunch=True, book=book_volume_info).order_by('number')
        case "Volume":
            book_volume_info = get_object_or_404(Volume, pk=id)
            book_volume_content = Poem.objects.filter(readyToLaunch=True, volume=book_volume_info).order_by('number')
        case _:
            book_volume_info = None
            book_volume_content = None

    book_volume = BookVolumeQueryset(book_volume_info, book_volume_content)

    return render(request, 'detail_book_volume.html', {'book_volume': book_volume})


#############################################    ENTERTAINMENT    ######################################################
class Entertainment(ListView):
    template_name = 'entertainment.html'
    context_object_name = 'combined'

    def get_queryset(self):
        expertise1 = Expertise.objects.get(expertise='entertainment')
        expertise2 = Expertise.objects.get(expertise='art')
        expertise3 = Expertise.objects.get(expertise='literature')
        expertise4 = Expertise.objects.get(expertise='science')
        category_science = CategoryPost.objects.get(category='science')

        roundabout1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise1.id).order_by('-date')[
                      :5]
        roundabout2 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise2.id).order_by('-date')[
                      :5]
        roundabout3 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise3.id).order_by('-date')[
                      :5]
        roundabout4 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise4.id,
                                          category=category_science).order_by('-date')[:5]

        roundabout = sorted(chain(roundabout1, roundabout2, roundabout3, roundabout4), key=attrgetter('date'),
                            reverse=True)[1:10]

        thumbnail_model1_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise1.id).order_by(
            '-date')[2:]
        thumbnail_model1_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise1.id).order_by(
            '-date')

        thumbnail_model2_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise2.id).order_by(
            '-date')[2:]
        thumbnail_model2_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise2.id).order_by(
            '-date')

        thumbnail_model3_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise3.id).order_by(
            '-date')[2:]
        thumbnail_model3_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise3.id).order_by(
            '-date')

        thumbnail_model4_qs1 = Post.objects.filter(readyToLaunch=True, promote=True, expertise=expertise4.id,
                                                   category=category_science).order_by(
            '-date')[2:]
        thumbnail_model4_qs2 = Post.objects.filter(readyToLaunch=True, promote=False, expertise=expertise4.id,
                                                   category=category_science).order_by(
            '-date')

        thumbnail = sorted(chain(thumbnail_model1_qs1, thumbnail_model1_qs2, thumbnail_model2_qs1, thumbnail_model2_qs2,
                                 thumbnail_model3_qs1, thumbnail_model3_qs2, thumbnail_model4_qs1,
                                 thumbnail_model4_qs2), key=attrgetter('date'),
                           reverse=True)

        latest_post1 = Post.objects.filter(readyToLaunch=True, expertise=expertise1.id).order_by('-date')[:1]
        latest_post2 = Post.objects.filter(readyToLaunch=True, expertise=expertise2.id).order_by('-date')[:1]
        latest_post3 = Post.objects.filter(readyToLaunch=True, expertise=expertise3.id).order_by('-date')[:1]
        latest_post4 = Post.objects.filter(readyToLaunch=True, expertise=expertise4.id,
                                           category=category_science).order_by('-date')[:1]

        latest = sorted(chain(latest_post1, latest_post2, latest_post3, latest_post4), key=attrgetter('date'),
                        reverse=True)[:1]

        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        combined = UltimateQueryset(roundabout, thumbnail, latest, quote)
        return combined


################################################    SCIENCE    #########################################################
class SciencePost(ListView):
    template_name = 'science.html'
    context_object_name = 'combined'

    def get_queryset(self):
        expertise = Expertise.objects.get(expertise='science')

        roundabout1 = Science.objects.filter(readyToLaunch=True, promote=True, expertise=expertise.id).order_by(
            '-date')[:8]

        roundabout = sorted(chain(roundabout1), key=attrgetter('date'), reverse=True)[1:10]

        thumbnail_model1_qs1 = Science.objects.filter(readyToLaunch=True, promote=True,
                                                      expertise=expertise.id).order_by('-date')[8:]
        thumbnail_model1_qs2 = Science.objects.filter(readyToLaunch=True, promote=False,
                                                      expertise=expertise.id).order_by('-date')

        thumbnail = sorted(chain(thumbnail_model1_qs1, thumbnail_model1_qs2), key=attrgetter('date'),
                           reverse=True)

        latest = Science.objects.filter(readyToLaunch=True, expertise=expertise.id).order_by('-date')[:1]

        quote = Quote.objects.filter(readyToLaunch=True).order_by('-date')[:1]

        combined = UltimateQueryset(roundabout, thumbnail, latest, quote)
        return combined


########################################################################################################################
##############################################       DETAIL      #######################################################
########################################################################################################################

def detail_post(request, class_name, id, state=None, number=None):
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
            book_volume_info = get_object_or_404(Volume, pk=id)
            book_volume_content = Poem.objects.filter(readyToLaunch=True, volume=book_volume_info).order_by('number')
            post = BookVolumeQueryset(book_volume_info, book_volume_content)
        case "Poem":
            if number == None:
                post = get_object_or_404(Poem, pk=id)
            else:
                if state == "prev":
                    number -= 1
                elif state == "next":
                    number += 1
                volume_info = get_object_or_404(Volume, id=id)
                post = get_object_or_404(Poem, readyToLaunch=True, number=number, volume=volume_info)
                last_poem = Poem.objects.filter(readyToLaunch=True, volume=volume_info).order_by('-number')[0]
                if post == last_poem:
                    last = "yes"
                    post = LastPoemBook(post, last)
        case "Book":
            book_volume_info = get_object_or_404(Book, pk=id)
            book_volume_content = Chapter.objects.filter(readyToLaunch=True, book=book_volume_info).order_by('number')
            post = BookVolumeQueryset(book_volume_info, book_volume_content)
        case "Chapter":
            if number == None:
                post = get_object_or_404(Chapter, pk=id)
                last_chapter = Chapter.objects.filter(readyToLaunch=True, book=post.book).order_by('-number')[0]
                if post == last_chapter:
                    last = "yes"
                    post = LastPoemBook(post, last)
            else:
                book_info = get_object_or_404(Book, id=id)
                if state == "prev":
                    number -= 1
                elif state == "next":
                    number += 1
                post = get_object_or_404(Chapter, readyToLaunch=True, number=number, book=book_info)
                last_chapter = Chapter.objects.filter(readyToLaunch=True, book=book_info).order_by('-number')[0]
                if post == last_chapter:
                    last = "yes"
                    post = LastPoemBook(post, last)
        case "Post":
            post = get_object_or_404(Post, pk=id)
        case "Science":
            post = get_object_or_404(Science, pk=id)
        case "Quote":
            post = get_object_or_404(Quote, pk=id)
        case _:
            post = None

    return render(request, 'detail.html', {'post': post})


########################################################################################################################
##############################################       SEARCH      #######################################################
########################################################################################################################

def search(request):
    if request.method == "POST":
        searched = request.POST['input-search-sentence']
        searched_words = searched.split()
        expertise_art = request.POST.get('form-expertise-art', "off")
        expertise_literature = request.POST.get('form-expertise-literature', "off")
        expertise_science = request.POST.get('form-expertise-science', "off")
        expertise_entertainment = request.POST.get('form-expertise-entertainment', "off")
        content_title = request.POST.get('form-content-title', "off")
        content_content = request.POST.get('form-content-content', "off")
        if (len(searched_words) != 0):
            if (content_title == "on" and content_content == "on"):
                if expertise_art == "on":
                    art1 = Artwork.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    art2 = Artwork.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        art1 &= Artwork.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        art2 &= Artwork.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                    art = chain(art1, art2)
                    art = list(dict.fromkeys(art))
                else:
                    art = None
                if expertise_literature == "on":
                    book1 = Book.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    book2 = Book.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    volume1 = Volume.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    volume2 = Volume.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    chapter1 = Chapter.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    chapter2 = Chapter.objects.filter(readyToLaunch=True,
                                                      content__icontains=searched_words[0]).order_by('-date')
                    poem1 = Poem.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    poem2 = Poem.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        book1 &= Book.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        book2 &= Book.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                        volume1 &= Volume.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        volume2 &= Volume.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                        chapter1 &= Chapter.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        chapter2 &= Chapter.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                        poem1 &= Poem.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        poem2 &= Poem.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                    book = chain(book1, book2)
                    book = list(dict.fromkeys(book))
                    volume = chain(volume1, volume2)
                    volume = list(dict.fromkeys(volume))
                    chapter = chain(chapter1, chapter2)
                    chapter = list(dict.fromkeys(chapter))
                    poem = chain(poem1, poem2)
                    poem = list(dict.fromkeys(poem))
                else:
                    book = None
                    volume = None
                    chapter = None
                    poem = None
                if expertise_science == "on":
                    science1 = Science.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    science2 = Science.objects.filter(readyToLaunch=True,
                                                      content__icontains=searched_words[0]).order_by('-date')
                    for word in searched_words[1:]:
                        science1 &= Science.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        science2 &= Science.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                    science = chain(science1, science2)
                    science = list(dict.fromkeys(science))
                else:
                    science = None
                if expertise_entertainment == "on":
                    post1 = Post.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    post2 = Post.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        post1 &= Post.objects.filter(readyToLaunch=True, title__icontains=word).order_by('-date')
                        post2 &= Post.objects.filter(readyToLaunch=True, content__icontains=word).order_by('-date')
                    post = chain(post1, post2)
                    post = list(dict.fromkeys(post))
                else:
                    post = None
            elif content_title != "on" and content_content == "on":
                if expertise_art == "on":
                    art = Artwork.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        art &= Artwork.objects.filter(readyToLaunch=True, content__icontains=word).order_by('-date')
                else:
                    art = None
                if expertise_literature == "on":
                    book = Book.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    volume = Volume.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    chapter = Chapter.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    poem = Poem.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        book &= Book.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                        volume &= Volume.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                        chapter &= Chapter.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                        poem &= Poem.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                else:
                    book = None
                    volume = None
                    chapter = None
                    poem = None
                if expertise_science == "on":
                    science = Science.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        science &= Science.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                else:
                    science = None
                if expertise_entertainment == "on":
                    post = Post.objects.filter(readyToLaunch=True, content__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        post &= Post.objects.filter(readyToLaunch=True, content__icontains=word).order_by(
                            '-date')
                else:
                    post = None
            elif content_title == "on" and content_content != "on":
                if expertise_art == "on":
                    art = Artwork.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        art &= Artwork.objects.filter(readyToLaunch=True, title__icontains=word).order_by('-date')
                else:
                    art = None
                if expertise_literature == "on":
                    book = Book.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by('-date')
                    volume = Volume.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    chapter = Chapter.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    poem = Poem.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by('-date')
                    for word in searched_words[1:]:
                        book &= Book.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        volume &= Volume.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        chapter &= Chapter.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                        poem &= Poem.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                else:
                    book = None
                    volume = None
                    chapter = None
                    poem = None
                if expertise_science == "on":
                    science = Science.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by(
                        '-date')
                    for word in searched_words[1:]:
                        science &= Science.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                else:
                    science = None
                if expertise_entertainment == "on":
                    post = Post.objects.filter(readyToLaunch=True, title__icontains=searched_words[0]).order_by('-date')
                    for word in searched_words[1:]:
                        post &= Post.objects.filter(readyToLaunch=True, title__icontains=word).order_by(
                            '-date')
                else:
                    post = None
            else:
                art = None
                book = None
                volume = None
                chapter = None
                poem = None
                science = None
                post = None

            # conbined = Search(searched, expertise_art, expertise_literature, expertise_science, expertise_entertainment,
            #                   content_title, content_content)

            combined = {'art': art, 'book': book, 'volume': volume, 'chapter': chapter, 'poem': poem, 'science': science,
                        'post': post}
            empty_combined = 0
            for val in combined.values():
                if val == []:
                    empty_combined += 1
            print(str(empty_combined) + "   " + str(len(combined)))
            if empty_combined == len(combined):
                combined = 'empty'
                print(combined)
            return render(request, 'search.html', {'combined': combined, 'sentence':searched, 'records': len(combined)})
        else:
            return render(request, 'search.html', {})
    else:
        return render(request, 'search.html', {})
