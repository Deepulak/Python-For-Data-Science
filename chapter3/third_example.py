import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
	'?title=List_of_Game_of_Thrones_wpisodes&oldid=802553687'

r = requests.get(url)
html_contents = r.text 
html_soup =	BeautifulSoup(html_contents, "html.parser")
# Find the first h1 tag
first_h1 = html_soup.find('h1')
print(first_h1.name)	# h1
print(first_h1.contents)	# ['Lisr of ', [...], 'episodes']
print(str(first_h1))

print(first_h1.text)	# List of Games of Thrones episodes
print(first_h1.get_text())	# DOes the same
print(first_h1.attrs)

print(first_h1.attrs['id'])		# firstHeading
print(first_h1['id'])	# Does the same
print(first_h1.get('id'))	# Does the same

print('----------------CITATIONS----------')
# find the first five cite elements with citation class
cites = html_soup.find_all('cite', class_='citation', limit=5)
for citation in cites:
	print(citation.get_text())
	# INside if this cite element, find the first a tag
	link = citation.find('a')
	# ... and show its URL
	print(link.get('href'))
	print()
	