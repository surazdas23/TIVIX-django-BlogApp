from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

'''class Post model is created to deal with the database, Post model will be a table in the database
 and each attributes will be the fields in the database'''


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Magic method is used to make the queryset for the post objects more descriptive
    def __str__(self):
        return self.title

    # returns the string version of the URL when user views each post details.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

