from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Expertise, User, Post


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['expertise']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'expertise']




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'expertise', 'date']

    # @admin.display(ordering='author__expertise', description='Expertise')
    # def get_expertise(self, obj):
    #     return Expertise.expertise_list[obj.author.expertise][1]
