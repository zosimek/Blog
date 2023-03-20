from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
####################################             FUNCTIONS            ##################################################
"""Pattern file uploat directory"""
def file_directory_path(filename):
    # file will be uploaded to MEDIA_ROOT / uploads / patterns / filename
    return 'uploads/patterns/{}'.format(filename)
def image_directory_path(filename):
    # file will be uploaded to MEDIA_ROOT / uploads / images / filename
    return 'uploads/images/{}'.format(filename)
def authorImg_directory_path(filename):
    # file will be uploaded to MEDIA_ROOT / uploads / authors / filename
    return 'uploads/images/{}'.format(filename)
##################################              CATEGORIES             #################################################
"""Category of the blog content"""
class Expertise(models.Model):
    expertise = models.CharField(default='', max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.expertise
########################################################################################################################
"""Category of the art content"""
class ArtCategory(models.Model):
    category = models.CharField(default='', max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category
########################################################################################################################
"""Category of the literature content"""
class LiteratureCategory(models.Model):
    category = models.CharField(default='', max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category
########################################################################################################################
"""Category of the science content"""
class ScienceCategory(models.Model):
    category = models.CharField(default='', max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category
########################################################################################################################
"""Category of the entertainment content"""
class EntertainmentCategory(models.Model):
    category = models.CharField(default='', max_length=64, unique=True, blank=False, null=False)

    def __str__(self):
        return self.category
####################################              MODELS             ###################################################
"""Authors of the blog content"""
class Author(models.Model):
    firstName = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)
    middleName = models.CharField(default='', max_length=64, unique=False, blank=True, null=True)
    lastName = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    info = RichTextField(default='... haven\'t decided yet ...', blank=True, null=True)
    image = models.ImageField(upload_to=authorImg_directory_path)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        if self.middleName != None:
            return "{} {} {}".format(self.firstName, self.middleName, self.lastName)
        else:
            return "{} {}".format(self.firstName, self.lastName)

    def __unicode__(self):
        return self.expertise
########################################################################################################################
class Guest(models.Model):
    firstName = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)
    lastName = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)
    nickName = models.CharField(default='', max_length=64, unique=True, blank=False, null=False)
    socialMedia = models.CharField(default='', max_length=300, unique=True, blank=False, null=False)
    image = models.ImageField(upload_to=image_directory_path, blank=True, null=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return "{} {} – {}".format(self.firstName, self.lastName, self.nickName)
########################################################################################################################
"""Common fields"""
class Common(models.Model):  # COMM0N
    title = models.CharField(max_length=150, unique=True)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, blank=False, null=False)
    content = mainBody = RichTextField(default='... to be continued ...', blank=True, null=True)
    readyToLounch = models.BooleanField(default=False, blank=False, null=False)
    tags = models.CharField(default='', max_length=200, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name()

    def name(self):
        return "{} {} {}".format(self.title, self.expertise, "test")

    class Meta:
        abstract = True
########################################################################################################################
"""Artwork gallery elements"""
class Artwork(Common):
    image = models.ImageField(upload_to=image_directory_path, blank=True, null=True)
    matherials = models.CharField(max_length=100)
    dimentionX = models.PositiveSmallIntegerField(blank=True)
    dimentionY = models.PositiveSmallIntegerField(blank=True)
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name()
    #
    # def name(self):
    #     return "{} ({}) : {}".format(self.title, self.category, self.date)
########################################################################################################################
"""Pattern file"""
class Pattern(models.Model):
    filename = models.CharField(max_length=150, unique=True)
    date = models.DateField(default=timezone.now, blank=False, null=False)
    file = models.FileField(upload_to=file_directory_path, blank=False, null=False)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name()
    #
    # def name(self):
    #     return "{} ({}--->{}) : {}".format(self.filename, self.expertise, self.category, self.date)
########################################################################################################################
class Volume(Common):
    cover = models.ImageField(upload_to=file_directory_path, blank=True, null=True)
    #TODO: override author field to add multiple

    # def __str__(self):
    #     return self.title
########################################################################################################################
"""A single poem."""
class Poem(Common):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name()
    #
    # def name(self):
    #     return "{} ({})".format(self.title, self.volume)
########################################################################################################################
"""Book. All but content."""
class Book(Common):
    cover = models.ImageField(upload_to=file_directory_path, blank=True, null=True)
    genre = models.ForeignKey(LiteratureCategory, on_delete=models.CASCADE)
    # TODO: override author field to add multiple

    # def __str__(self):
    #     return self.title
########################################################################################################################
""" The chapters of the book"""
class Chapter(Common):
    book = models.ForeignKey(Volume, on_delete=models.CASCADE)
    number = models.SmallIntegerField(blank=False, null=True)

    # def __str__(self):
    #     return self.name()
    #
    # def name(self):
    #     return "{} chapter: {}".format(self.book, self.number)
########################################################################################################################
class Entertainment(Common):
    image = models.ImageField(upload_to=file_directory_path, blank=True, null=True)
    featuring = models.ForeignKey(Guest, on_delete=models.CASCADE)
    category = models.ForeignKey(EntertainmentCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name()

    def name(self):
        return "{} ({} ---> {})".format(self.title, self.expertise, self.category)
########################################################################################################################
class Post(Common):
    image = models.ImageField(upload_to=file_directory_path, blank=True, null=True)
    featuring = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name()

    def name(self):
        return "{} ({})".format(self.title, self.expertise)
