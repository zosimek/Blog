from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.

###########################################       CATEGORIES      ######################################################

class Expertise(models.Model):
    expertise = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)

    def __str__(self):
        return self.expertise

class CategoryArt(models.Model):
    category = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)

    def __str__(self):
        return self.category

class CategoryLiterature(models.Model):
    category = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)

    def __str__(self):
        return self.category

class CategoryScience(models.Model):
    category = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)

    def __str__(self):
        return self.category

class CategoryPost(models.Model):
    category = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)

    def __str__(self):
        return self.category
#############################################       MODELS      ########################################################

class Author(models.Model):
    firstName = models.CharField(default='', max_length=64, blank=False, null=False)
    middleName = models.CharField(default='', max_length=64, blank=True, null=True)
    lastName = models.CharField(default='', max_length=64, blank=False, null=False)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    info = RichTextField(default='... haven\'t decided yet ...', blank=True, null=True)
    image = models.ImageField(upload_to='authors', null=True, blank=True)
    frame = models.ImageField(upload_to='authors', null=True, blank=True)
    readyToLaunch = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        if self.middleName != None:
            return "{} {} {}".format(self.firstName, self.middleName, self.lastName)
        else:
            return "{} {}".format(self.firstName, self.lastName)

    def __unicode__(self):
        return self.expertise

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of an author.
        """
        return self.__class__.__name__

class Guest(models.Model):
    firstName = models.CharField(default='', max_length=64, blank=False, null=False)
    lastName = models.CharField(default='', max_length=64, blank=True, null=True)
    nickName = models.CharField(default='', max_length=64, blank=False, null=False)
    socialMedia = models.CharField(default='', max_length=300, unique=False, blank=True, null=True)
    image = models.ImageField(upload_to='authors', null=True, blank=True)
    readyToLaunch = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        if self.lastName != None:
            return "{} {} – {}".format(self.firstName, self.lastName, self.nickName)
        else:
            return "{} – {}".format(self.firstName, self.nickName)

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a guest.
        """
        return self.__class__.__name__

class Common(models.Model):
    title = models.CharField(max_length=150, unique=True)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    content = RichTextField(default='... to be continued ...', blank=True, null=True)
    readyToLaunch = models.BooleanField(default=False, blank=False, null=False)
    tags = models.CharField(default='', max_length=200, unique=False, blank=True, null=True)

    class Meta:
        abstract = True

class Artwork(Common):
    materials = models.CharField(max_length=100)
    dimentionX = models.SmallIntegerField(null=True)
    dimentionY = models.SmallIntegerField(null=True)
    category = models.ForeignKey(CategoryArt, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="artworks")
    promote = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return "{} ({})".format(self.title, self.category)

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a artwork.
        """
        return self.__class__.__name__

class Pattern(models.Model):
    filename = models.CharField(max_length=64, unique=True)
    file = models.FileField(upload_to="patterns")
    date = models.DateField(default=timezone.now)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryArt, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({} ---> {})".format(self.filename, self.expertise, self.category)

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a pattern.
        """
        return self.__class__.__name__

class Volume(Common):
    cover = models.ImageField(upload_to="covers", null=True, blank=True)

    def __str__(self):
        return self.title

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a volume.
        """
        return self.__class__.__name__

class Poem(Common):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    number = models.SmallIntegerField(null=True)
    promote = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.title

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a poem.
        """
        return self.__class__.__name__

class Book(Common):
    cover = models.ImageField(upload_to="covers", null=True, blank=True)
    genre = models.ForeignKey(CategoryLiterature, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a book.
        """
        return self.__class__.__name__

class Chapter(Common):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.SmallIntegerField(null=True)
    promote = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return "{} ({})".format(self.title, self.book)

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a chapter.
        """
        return self.__class__.__name__

class Post(Common):
    image = models.ImageField(upload_to="posts")
    featuring = models.ForeignKey(Guest, null=True, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(CategoryPost, on_delete=models.CASCADE, blank=True, null=True)
    promote = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return "{} ({})".format(self.title, self.expertise)

    def class_name(self):
        """
        This function enables transition from thumbnail, carousel or any other
        short "click-bite" form od a display to detail view of a post.
        """
        return self.__class__.__name__

#############################################       ADDONS      ########################################################
class Quote(models.Model):
    date = models.DateField(default=timezone.now)
    quote = models.CharField(default='', max_length=1000, blank=False, null=False)
    author = models.CharField(default='', max_length=100, blank=False, null=False)
    readyToLaunch = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return "{} ({}...)".format(self.author, self.quote[:30])