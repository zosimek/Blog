from django.contrib import admin
from .models import Expertise, CategoryArt, CategoryLiterature, CategoryScience, CategoryPost,\
    Author, Guest, Artwork, Pattern, Volume, Poem, Book, Chapter, Post
# Register your models here.
##############################################     CATEGORIES    #######################################################

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['expertise']

@admin.register(CategoryArt)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(CategoryLiterature)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(CategoryScience)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(CategoryPost)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['category']

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
    list_display = ['__str__', 'volume', 'date']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'date']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['__str__', "book", 'date']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'expertise', 'date']