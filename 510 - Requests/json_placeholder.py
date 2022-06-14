import requests


def get_posts():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
    )
    assert response.status_code == 200
    response_object = response.json()
    return response_object


def get_post(post_id: int):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}",
    )
    assert response.status_code == 200
    response_object = response.json()
    return response_object


def publish_post(title, body, user_id):
    data = {
        "title": title,
        "body": body,
        "userId": user_id,
    }
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )
    assert response.status_code == 201
    response_object = response.json()
    return response_object


def delete_post(post_id):
    pass


if __name__ == "__main__":
    posts = get_posts()
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

