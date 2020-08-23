from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class NavBar(models.Model):
    NAVName = models.CharField(max_length=50)
    NAVHasFather = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    NAVHtml = RichTextUploadingField( blank=True, null=True)
    NAVSlug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.NAVName

    def save(self, *args, **kwargs):
        if not self.NAVSlug:
            self.NAVSlug = 'nav'+str(slugify(self.id))
        super(NavBar, self).save(*args, **kwargs)


class Question(models.Model):
    QQuestion = models.CharField(max_length=100)
    QAnswer = models.TextField( blank=True, null=True)

    def __str__(self):
        return self.QQuestion


class News(models.Model):
    NTitle = models.CharField(max_length=100, blank=True, null=True)
    NDetail = models.TextField( blank=True, null=True)
    NShort = models.TextField(blank=True, null=True)
    NImage = models.ImageField(upload_to='news/', blank=True, null=True)
    NDate = models.DateTimeField()

    def __str__(self):
        return self.NTitle

    def details(self):
        return self.NDetail[:50]+'.....'


class MotionImage(models.Model):
    MITitle = models.CharField(max_length=100, default="")
    MIDetail = models.TextField( blank=True, null=True)
    MIImage = models.ImageField(upload_to='motion/', blank=True, null=True)
    MIVisible = models.BooleanField()
    MIRelation = models.ForeignKey(NavBar, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.MITitle


class Adds(models.Model):
    ATitle = models.CharField(max_length=100, blank=True, null=True)
    ADetail = models.TextField( blank=True, null=True)
    AImage = models.ImageField(upload_to='adds/', blank=True, null=True)
    ADate = models.DateTimeField()

    def __str__(self):
        return self.ATitle

    def details(self):
        return self.ADetail[:50] + '.....'


class Success(models.Model):
    STitle = models.CharField(max_length=100)
    SDep = models.CharField(max_length=100)
    SDetail = models.TextField(blank=True, null=True)
    SImage = models.ImageField(upload_to='success/', blank=True, null=True)

    def __str__(self):
        return self.STitle


class Contact(models.Model):
    CFacebook = models.CharField(max_length=150, blank=True, null=True)
    CTwitter = models.CharField(max_length=150, blank=True, null=True)
    CTelegram = models.CharField(max_length=150, blank=True, null=True)
    CEmail = models.CharField(max_length=150, blank=True, null=True)
    CAddress = models.CharField(max_length=150, blank=True, null=True)
    CPhone = models.CharField(max_length=150, blank=True, null=True)


class Others(models.Model):
    OTitle = models.CharField(max_length=150, blank=True, null=True)
    ODetail = models.TextField(blank=True, null=True)
