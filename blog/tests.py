from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Blog
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.blog = Blog.objects.create(
            title='A good title',
            body='Body content',
            author=self.user,
        )

        def test_string_representation(self):
                blog = Blog(title='A sample title')
                self.assertEqual(str(blog), blog.title)

        def test_blog_content(self):
            self.assertEqual(f'{self.blog.title}', 'A good title')
            self.assertEqual(f'{self.blog.author}', 'testuser')
            self.assertEqual(f'{self.blog.body}', 'Body content')

        def test_blog_list_view(self):
            response = self.client.get(reverse('blog'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Body content')
            self.assertTemplateUsed(response, 'blog.html')

        def test_blog_detail_view(self):
            response = self.client.get('/post/1/')
            no_response = self.client.get('/post/100000/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(no_response.status_code, 404)
            self.assertContains(response, 'A good title')
            self.assertTemplateUsed(response, 'blog_detail.html')

            
