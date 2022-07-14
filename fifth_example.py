import requests

def calc(a, b, op):
	url = 'http://webscrapingfordatascience.com/calchttp'
	params = {'a':a, 'b':b, 'op':op}
	r = requests.get(url, params=params)

print(calc(4, 6, '*'))
print(calc(4, 6, "/"))