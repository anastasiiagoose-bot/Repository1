import requests

url = 'https://www.ukr.net/'
response = requests.get(url=url)
# print(response.content)
# print(response.text)
print(response.jason())
