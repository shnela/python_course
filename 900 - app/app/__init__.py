from app.database import Session, metadata
from app.posts.models import Post
from app.users.models import User
from app.users.accessors import get_user_by_id, get_users_by_name, dummy_func


if __name__ == '__main__':
    session = Session()

    print(session.query(Post).all())
    print(session.query(User).all())

    print(get_user_by_id(1, session))
    print(get_users_by_name('Gary', session))
