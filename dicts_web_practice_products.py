import requests
from pprint import pprint

url_products = 'https://dummyjson.com/products'
params = {
    "skip": 0,
    "limit": 1000,
}
response = requests.get(url=url_products, params=params)

response_json = response.json()

products = response_json['products']

total_cost = 0
for product in products:
    product_cost = product['price'] * product['stock']
    # total_cost = total_cost + product_cost
    total_cost += product_cost
    print(total_cost)

total_cost = round(total_cost, 2)
print(f'{total_cost=}')