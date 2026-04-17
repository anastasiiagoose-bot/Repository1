import requests
from pprint import pprint

url = 'https://dummyjson.com/posts'
params = {
    "skip": 0,
    "limit": 1000,
}
response = requests.get(url=url, params=params)
# print(response.content)
# print(response.text)
# pprint(response.json(), indent=4)
# print(response.json())

# print('dfgvbhjfd\nkvgdfhgvjhfdh\nkerhgjfr')
# print('"mbhg"')
response_json = response.json()
posts = response_json['posts']
# pprint(posts, indent=4)
dude_user_id = 47
likes_min_level = 380
search_text = 'dream'

friends_favorite_posts = []
search_text_results = []
counter = 0

for post in posts:
    counter = counter + 1
    # common data
    title = post['title']
    body = post['body']

    # user friend part
    user_id = post['userId']
    reactions = post['reactions']
    likes = reactions['likes']
    if user_id == dude_user_id and likes >= likes_min_level:
        friends_favorite_posts.append(title)

    # search text part
    if search_text in title.lower() or search_text in body.lower():
        search_text_results.append(post)


print(friends_favorite_posts)
pprint(search_text_results)
print(counter)