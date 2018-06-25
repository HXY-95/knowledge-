from django.db import models
from django.contrib import admin

# Create your models here.
class RecommendPost(models.Model):
    surl = models.CharField(max_length=150)
    name = models.CharField(max_length = 150)
    director = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    thumbnail = models.ImageField()
    #birthDate = models.DateField()
    abstract = models.TextField()
    subject = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class RecommendPostAdmin(admin.ModelAdmin):
    list_display = ('surl', 'name', 'director', 'country', 'thumbnail', 'subject', 'abstract')
    search_fields = ['name']


class FilmRecommendPost(models.Model):
    surl = models.CharField(max_length=150)
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class FilmRecommendPostAdmin(admin.ModelAdmin):
    list_display = ('surl', 'name')
    search_fields = ['name']

class BookRecommendPost(models.Model):
    surl = models.CharField(max_length=150)
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class BookRecommendPostAdmin(admin.ModelAdmin):
    list_display = ('surl', 'name')
    search_fields = ['name']

class GameRecommendPost(models.Model):
    surl = models.CharField(max_length=150)
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class GameRecommendPostAdmin(admin.ModelAdmin):
    list_display = ('surl', 'name')
    search_fields = ['name']

admin.site.register(RecommendPost, RecommendPostAdmin)
admin.site.register(FilmRecommendPost, FilmRecommendPostAdmin)
admin.site.register(BookRecommendPost, BookRecommendPostAdmin)
admin.site.register(GameRecommendPost, GameRecommendPostAdmin)