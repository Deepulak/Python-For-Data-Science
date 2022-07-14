import requests
from urllib.parse import quote, quote_plus

raw_string = 'a query with /, spaces and ?&'
print(quote(raw_string))
print(quote_plus(raw_string))

url = 'http://webscrapingfordatascience.com/paramhttp/?query='
print('\nUsing quote: ')
# Nothing is safe, not even '/' characters, so encode everything
r = requests.get(url + quote(raw_string, safe=''))
print(r.url)
print(r.text)

print('\nUsing quote_plus: ')
r = requests.get(url + quote_plus(raw_string))
print(r.url)
print(r.text)

