#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

headings_ny = []

for story_heading in soup.find_all(class_="story-heading"): 
	if story_heading.a:
		headings_ny.append(story_heading.a.text.replace("\n", " ").strip())
	else:
		headings_ny.append(story_heading.contents[0].strip())

for x in headings_ny[:11]:
	print(x)

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.michigandaily.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")

for most_read in soup.find_all(class_="panel-pane pane-mostread"): 
	for li in most_read.find_all('li'):
		print(li.get_text())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
import requests
from bs4 import BeautifulSoup

base_url = "http://newmantaylor.com/gallery.html"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

for img in soup.find_all('img'):
	has_alt_text = 'No alternative text provided!!'	
	if (img.has_attr('alt')):
		has_alt_text = img['alt']
	print(has_alt_text)

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup 

url = 'https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
req = urllib.request.Request(url, None, {'User-Agent': 'SI_CLASS'})
response_str = None
with urllib.request.urlopen(req, context=ctx) as response:
	response_str = response.read().decode()
	soup = BeautifulSoup(response_str, 'html.parser')
#print(response_str)

def print_email_tags(soup):
	email_tags = soup.find_all('div', class_ = 'field-item even')
	email_titles = [t for t in email_tags]

	for i, t in enumerate(email_titles):
		print (i+1, t)		
print(print_email_tags(soup))
