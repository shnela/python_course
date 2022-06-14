import unittest
from json_placeholder import *


class TestJsonPlaceholder(unittest.TestCase):
    def test_get_posts(self):
        posts = get_posts()
        self.assertEqual(len(posts), 100)
        self.assertEqual(posts[0]['id'], 1)

    def test_get_post(self):
        expected_post = {
            'id': 1,
            'userId': 1,
            'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
            'body': 'quia et suscipit\n'
                    'suscipit recusandae consequuntur expedita et cum\n'
                    'reprehenderit molestiae ut ut quas totam\n'
                    'nostrum rerum est autem sunt rem eveniet architecto'
        }
        post1 = get_post(1)
        self.assertEqual(post1, expected_post)

    def test_get_user_posts(self):
        user_id = 1
        expected_posts = [post for post in get_posts() if post['userId'] == user_id]
        user_posts = get_user_posts(user_id)
        self.assertEqual(user_posts, expected_posts)
