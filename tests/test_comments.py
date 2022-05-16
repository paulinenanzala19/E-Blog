import unittest
from app.models import Comments, Blog, User
from app import db

class CommentsModelTest(unittest.TestCase):
    def setUp(self):
        
        self.new_comment = Comments(id = 1, comment = 'Test comment', user = self.user_yvonne, blog_id = self.new_blog)
        
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_yvonne)
        self.assertEquals(self.new_comment.blog_id,self.new_blog)


class CommentsModelTest(unittest.TestCase):
    def setUp(self):
        self.user_jessy = User(username='jessy', password='pipi', email='jessy@test.com')
        self.new_blog = Blog(id=1, title='Test', post='A test blog', user_id=self.user_jessy.id)
        self.new_comment = Comments(id=1, comment ='A test comment', user_id=self.user_jessy.id, blog_id = self.new_blog.id )

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()
        Comments.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment, 'A test comment')
        self.assertEquals(self.new_comment.user_id, self.user_jessy.id)
        self.assertEquals(self.new_comment.blog_id, self.new_blog.id)

    def test_save_comment(self):
        self.new_comment.save()
        self.assertTrue(len(Comments.query.all()) > 0)

    def test_get_comment(self):
        self.new_comment.save()
        got_comment = Comments.get_comment(1)
        self.assertTrue(get_comment is not None)