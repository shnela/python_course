# [Requests: HTTP for Humans]

## Quick example
```python
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))

r.status_code
200

r.headers['content-type']
'application/json; charset=utf8'

r.encoding
'utf-8'

r.text
'{"type":"User"...'

r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}
```

## Requests debugging

### [More complicated POST requests][]

```python
import json
import requests

url = 'https://api.github.com/some/endpoint'

payload = {'some': 'data'}

r1 = requests.post(url, data=json.dumps(payload))
```
> Please note that the above code will NOT add the Content-Type header (so in particular it will NOT set it to application/json).
```python
r2 = requests.post(url, json=payload)
```

### [RequestsToCurl][]

```bash
data = {
    "title": 't',
    "body": 'b',
    "userId": 1,
}

# this POST won't send JSON serialized data
response1 = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    data=data
)
print(curl.parse(response1))

# this will, but without `Content-Type` header
response2 = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    data=json.dumps(data)
)
print(curl.parse(response2))

response3 = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)
print(curl.parse(response3))
```

#### Result:
```
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: python-requests/2.28.0' -d 'title=t&body=b&userId=1' https://jsonplaceholder.typicode.com:443/posts
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'User-Agent: python-requests/2.28.0' -d '{"title": "t", "body": "b", "userId": 1}' https://jsonplaceholder.typicode.com:443/posts
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.28.0' -d '{"title": "t", "body": "b", "userId": 1}' https://jsonplaceholder.typicode.com:443/posts
```

## Fake REST API [{JSON} Placeholder][]

Fake REST API for testing.

[{JSON} Placeholder - guide][]
> Important: resource will not be really updated on the server but it will be faked as if.

[json_placeholder.py](json_placeholder.py)


[Requests: HTTP for Humans]: https://requests.readthedocs.io/en/latest/
[RequestsToCurl]: https://pypi.org/project/requests-to-curl/
[More complicated POST requests]: https://requests.readthedocs.io/en/latest/user/quickstart/#more-complicated-post-requests
[{JSON} Placeholder]: https://jsonplaceholder.typicode.com/
[{JSON} Placeholder - guide]: https://jsonplaceholder.typicode.com/guide/
