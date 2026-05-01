from bs4 import BeautifulSoup
import requests

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, features="html.parser")

print(soup.prettify())

# print(soup.title)
# print(soup.p)

# response = requests.get("https://www.wikipedia.org/")
# print(response.text)

# print(soup.prettify())
# print(soup.title, '\n')
# print(soup.title.string)

# print(soup.p['class'])
# print(soup.a['href'])

# print(soup.find(href = "http://example.com/lacie"))
# print(soup.find(class_ = 'story'))
# a_tags = soup.find_all('a')
# print(a_tags[2])
# print(soup.find_all(['a', 'title']))

p = soup.find(class_= 'story')
print(p.contents)
# print(p.contents)
# for child in p.children:
#   print(child)
body = soup.find('body')
# print(body.contents)
# print(len(body.contents))

#--Printing-Descendants--
# print(list(body.descendants))
# print(len(list(body.descendants)))

#--Getting-Parent-Names--
# print(soup.a.parent)
# for p in soup.a.parents:
#     print(p.name)
    
#--Print-Siblings-In-Tree--
a = soup.a
# print(a.next_sibling.next_sibling)
# print(a.next_sibling.previous_sibling)

response = requests.gets('https://en.wikipedia.org/wiki/Bristlecone_pine')

soup = BeautifulSoup(response.text, "html.parser")

# print(soup.text)

# print(soup.h1.text)

# print(len(soup.find_all('h2')))

# print(soup.a['href'])