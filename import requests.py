import requests

#payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://fr.openfoodfacts.org/api/v0/product/737628064502.json')
print(r.url)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)