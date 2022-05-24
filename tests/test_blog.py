import unittest
from app.models import Blog, User,
from app import db


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_jessy = User(username='jessy', password='pipis', email='jessy@test.com')
        self.new_blog = Blog(id=1, title='Test', post='test blog', user_id=self.user_jessy.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.post, ' A test blog')
        self.assertEquals(self.new_blog.user_id, self.user_jessy.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        got_blog = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)
