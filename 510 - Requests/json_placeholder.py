import requests


def get_posts():
    pass


def get_post(post_id: int):
    pass


def publish_post(title, body, user_id):
    pass


def delete_post(post_id):
    pass


def get_user_posts(user_id: int):
    pass


if __name__ == "__main__":
    get_user_posts(1)

    all_posts = get_posts()
    post_one = get_post(1)
    assert post_one == {
        'userId': 1,
        'id': 1,
        'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
        'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\n'
                'reprehenderit molestiae ut ut quas totam\n'
                'nostrum rerum est autem sunt rem eveniet architecto'
    }
    publish_post("title", "Lore impsum", 1)

