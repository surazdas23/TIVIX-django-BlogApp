import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
from .. import views
pytestmark = pytest.mark.django_db


class TestPostListView:
    def test_list(self):
        req = RequestFactory().get('/')
        res = views.PostListView.as_view()(req)
        assert res.status_code == 200, 'Should be callable'


class TestPostCreateView:
    def test_create_post(self):
        req = RequestFactory().get('/')
        res = views.PostCreateView.as_view()(req)
        assert res.status_code == 200, 'Should be callable'


class TestPostUpdateView:
    def test_get(self):
        req = RequestFactory().get('/')
        obj = mixer.blend('blog.Post')
        res = views.PostUpdateView.as_view()(req, pk=obj.pk)
        assert res.status_code == 200, "Should work all the time"

    @pytest.mark.skip(reason='Attention required')
    def test_post(self):
        post = mixer.blend('blog.Post')
        data = {'title': 'content'}
        req = RequestFactory().post('/', data=data)
        res = views.PostUpdateView.as_view()(req, pk=post.pk)
        assert res.status_code == 200, 'Success'
        post.refresh_from_db()
        assert post.title == 'content', 'updated post should be visible'


