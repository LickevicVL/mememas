from os.path import join, dirname, basename
from time import time

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from memes.utils import TimeAgo


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def get_created_at(self):
        return TimeAgo.get_time_ago(self.created_at)


class Post(Base):
    title = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title.lower()) + str(int(time()))

        super().save(*args, **kwargs)

    def __str__(self):
        return f'<{self.__class__.__name__}:{self.title}>'

    @staticmethod
    def upload_to(instance, filename):
        return join(
            dirname(basename(__file__)), instance.__class__.__name__, filename
        )


class Mem(Post):
    body = models.TextField(blank=True, db_index=True)
    image = models.ImageField(default=None, upload_to=Post.upload_to)

    def get_absolute_url(self):
        return reverse('memes:mem', kwargs={'slug': self.slug})


class Movie(Post):
    url = models.CharField(max_length=256)


class Comment(Base):
    body = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    mem = models.ForeignKey(
        Mem, on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        ordering = ['-created_at']
