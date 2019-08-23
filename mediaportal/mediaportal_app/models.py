from django.conf import settings
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    return f'{instance.slug}/{filename}'


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to=generate_filename)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    date = models.DateField(default=timezone.now)
    objects = models.Manager()
    comments = GenericRelation('comment')
    users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                            blank=True)

    def __str__(self):
        return f'Статья {self.title} из категории {self.category.name}'

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={
            'category_slug': self.category.slug, 'article_slug': self.slug})


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class UserAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    favorite_articles = models.ManyToManyField(Article, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account_view', kwargs={'user': self.user.username})
