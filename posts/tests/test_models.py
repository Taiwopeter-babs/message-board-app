from django.test import TestCase
from django.urls import reverse
from posts.models import Post


class PostModelTest(TestCase):
    """Post Model test"""

    def setUp(self):
        """setUp method"""
        Post.objects.create(text='test text content')

    def test_text_content(self):
        """test text creation"""
        post_obj = Post.objects.get(id=1)
        expected = "{}".format(post_obj.text)
        self.assertEqual(expected, 'test text content')


class HomePageViewTest(TestCase):
    """Test home page"""

    def setUp(self):
        """setUp method"""
        Post.objects.create(text='test home page content')

    def test_home_page_url_exists_at_proper_location(self):
        """Home page test"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_name_and_template(self):
        """Test correct url name"""
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
