__all__ = (
    'get_user_by_id',
    'get_users_by_name',
)

from app.users.models import User


def get_user_by_id(user_id, session):
    return session.query(User).get(user_id)


def get_users_by_name(username, session):
    return session.query(User).filter(User.username == username).all()


def dummy_func():
    """Please don't use me"""
