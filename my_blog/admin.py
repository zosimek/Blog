from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Expertise, ArtCategory, LiteratureCategory, ScienceCategory,\
    EntertainmentCategory, Author, Guest, Artwork, Pattern, Volume, Poem, Book,\
    Chapter, Entertainment, Post

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['expertise']

@admin.register(ArtCategory)
class ArtCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(LiteratureCategory)
class LiteratureCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(ScienceCategory)
class ScienceCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(EntertainmentCategory)
class LiteratureCategoryAdmin(admin.ModelAdmin):
    list_display = ['category']

@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    list_display = ['expertise']

@admin.register(Guest)
class UserAdmin(admin.ModelAdmin):
    list_display = ['firstName']

@admin.register(Artwork)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Pattern)
class UserAdmin(admin.ModelAdmin):
    list_display = ['filename']

@admin.register(Volume)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Poem)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Chapter)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Entertainment)
class UserAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

    # @admin.display(ordering='author__expertise', description='Expertise')
    # def get_expertise(self, obj):
    #     return Expertise.expertise_list[obj.author.expertise][1]
