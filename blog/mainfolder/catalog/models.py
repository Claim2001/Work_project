import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser
from django.template.defaultfilters import slugify


class Article(models.Model):
    article_title = models.CharField(max_length=200, verbose_name='Название статьи')
    article_additional_title = models.CharField(max_length=400, verbose_name='Подзаголовок', blank=True)
    article_text = models.TextField(verbose_name='Статья')
    article_image = models.ImageField(upload_to='article/', blank=True, verbose_name='Картинка')
    article_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=False, unique=True, allow_unicode=False)

    class Meta:
        ordering = ["article_title"]

    def __str__(self):
        return self.article_text

    def get_author_username(self):
        return self.article_user.username

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.article_title)
        super(Article, self).save(*args,**kwargs)


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comments_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Profile(models.Model):
    CHOICES = {
        (1, "Администратор"),
        (2, "Модератор"),
        (3, "Гость")
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(choices=CHOICES)