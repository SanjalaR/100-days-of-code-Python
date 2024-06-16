from bs4 import BeautifulSoup
import lxml

# BASIC
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')  # or lxml after importing
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.a)
# print(soup.li)
# print(soup.p)
# print(soup.find_all(name='a'))  # list of all anchor tags using name of tag
# for tag in soup.find_all(name='a'):
#     print(tag.getText())  # Get text of anchor tag
#     print(tag.get('href'))  # Get link of anchor tag (or any attribute)
# print(soup.find(name='h1', id='name').getText())
# print(soup.find(name='h3', class_='heading').name)
# .name(tag)/ gettext(text)/ .get(attribute value)
# print(soup.select_one(selector='p a'))  # css selector
# print(soup.select_one(selector='#name'))
# print(soup.select(selector='.heading'))

# LIVE WEBSITE
# import requests
#
# response = requests.get("https://news.ycombinator.com/news")
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
# for tag in soup.find_all('a'):
#     print(tag.getText())
# print(soup.select(selector='.title'))
# print(soup.find(name='span', class_='titleline'))
# tags = soup.select(selector='td .titleline a')
# for tag in tags:
#     article_text = tag.getText()
#     article_link = tag.get('href')
#     print(article_link)

# MOVIES PROJECT
import requests
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

tags = soup.select(selector='.landscape')
movies = []
for tag in tags:
    movies.append(tag.get('title'))
print(movies)
movies = movies[::-1]
print(movies)
movies[58] = '59) E.T. - The Extra Terrestrial'
with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
