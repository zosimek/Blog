from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

# Create your models here.
class Expertise(models.Model):
    expertise = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)

    def __str__(self):
        return self.expertise

class User(models.Model):
    firstName = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)
    middleName = models.CharField(default='', max_length=64, unique=False, blank=True, null=True)
    lastName = models.CharField(default='', max_length=64, unique=False, blank=False, null=False)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    info = RichTextField(default='... haven\'t decided yet ...', blank=True, null=True)
    readyToLounch = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        if self.middleName != None:
            return "{} {} {}".format(self.firstName, self.middleName, self.lastName)
        else:
            return "{} {}".format(self.firstName, self.lastName)

    def __unicode__(self):
        return self.expertise

class Post(models.Model):
    title = models.CharField(default='', max_length=124, unique=True, blank=False, null=False)
    expertise = models.ForeignKey(Expertise, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now, blank=False, null=False)
    tags = models.CharField(default='', max_length=200, unique=True, blank=False, null=False)
    mainBody = RichTextField(default='... to be continued ...', blank=True, null=True)
    readyToLounch = models.BooleanField(default=False, blank=False, null=False)