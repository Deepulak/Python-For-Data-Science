import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'
r = requests.get(url)

# Which HTTP status code did we get back from the server
print(r.status_code)
# What is the textual status code?
print(r.reason)
# What were the HTTP response headers?
print(r.headers)
# The request information is saved as a Python object in r.request:
print(r.request)
# What were the HTTP request headers?
print(r.request.headers)
# The HTTP response content
print(r.text)

url2 = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test'
r2 = requests.get(url2)
print(r2.text)
# Will show: O don't have any information on "test"
url3 = 'http://webscrapingfordatascience.com/paramhttp/?query=a query with spaces'
r3 = requests.get(url3)
# Parameter will be encoded as 'a%20query%20with%20spaces'
# You can verify this be looking at the prepared request URL:
print(r3.request.url3)
# Will show [...]/paramhttp/?query=a%20query%20with%20spaces
print(r3.text)
# Will show: I don't have any information on "a query with spaces"
