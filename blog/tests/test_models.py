import pytest
from mixer.backend.django import mixer
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
pytestmark = pytest.mark.django_db


class TestPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def test_model(self):
        obj = mixer.blend('blog.Post')
        assert obj.pk == 1, 'Should create a Post instance'


