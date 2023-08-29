from django.contrib import admin
from .models import Expertise, CategoryArt, CategoryLiterature, CategoryScience, CategoryPost, \
    Author, Guest, Artwork, Pattern, Volume, Poem, Book, Chapter, Post, Quote, Science


# Register your models here.
##############################################     CATEGORIES    #######################################################

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['expertise_en']

@admin.register(CategoryArt)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category_en']

@admin.register(CategoryLiterature)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category_en']

@admin.register(CategoryScience)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category_en']

@admin.register(CategoryPost)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category_en']

##############################################       MODELS      #######################################################

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'expertise']

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['__str__']

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'expertise', 'date']

@admin.register(Pattern)
class PatternAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'expertise', 'date']

@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date']

@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'volume', 'number']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'date']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['__str__', "book", 'number']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'expertise', 'date']

@admin.register(Science)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'date']


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['__str__']