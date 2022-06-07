import unittest

from unittest import mock

from app.database import Session
from app.users.models import User


@mock.patch('app.users.accessors.get_user_by_id')
class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        session = Session()
        session.query(User).delete()
        session.commit()

    def setUp(self) -> None:
        self.session = Session()

    def tearDown(self) -> None:
        pass

    def test_creating_user(self, get_user_mock):
        new_user = User(username='Frank')
        self.session.add(new_user)
        self.session.commit()

        user_id = new_user.id

        self.assertEqual('Frank', self.session.query(User).get(user_id).username)


    def test_creating_user2(self, get_user_mock):
        self.session.query(User).delete()
        new_user = User(username='Alex')
        self.session.add(new_user)
        self.session.commit()

        user_id = new_user.id

        self.assertEqual('Alex', self.session.query(User).get(user_id).username)

