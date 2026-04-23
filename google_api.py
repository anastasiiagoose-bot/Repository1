import requests
from pprint import pprint

url = 'https://script.google.com/macros/s/AKfycbwji4nSgUtkNCXLjtPBfffP-q05P0VHd4SXJ6_9DWYELVeDL3ein_4xLONO9l-1jKnh/exec'
response = requests.get(url=url, params={})
response_json = response.json()

pprint(response_json)

trip = response_json['trip']

total_charity = 0
for row in trip:
    total_charity += row['charity']

print(f'{total_charity}')