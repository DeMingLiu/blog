# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models hefrom django.contrib.auth.
from django.utils.six import python_2_unicode_compatible

# @python_2_unicode_compatible
class Category(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length = 100)

# @python_2_unicode_compatible
class Tag(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length = 100 )

# @python_2_unicode_compatible
class Post(models.Model):
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk })

    title = models.CharField(max_length = 100 )
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length = 200, blank = True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank = True)
    author = models.ForeignKey(User)

