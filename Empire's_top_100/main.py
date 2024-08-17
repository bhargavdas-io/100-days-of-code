import requests
from bs4 import BeautifulSoup

site = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
text = site.text
soup = BeautifulSoup(text, 'html.parser')
movie_list = []

movie_title = soup.find_all("h3", class_='listicleItem_listicle-item__title__BfenH')
for title in movie_title:
    titles = title.getText()
    movie_list.append(titles)

reversed_list = list(reversed(movie_list))

with open('movie_names.txt', 'w') as file:
    for i in reversed_list:
        file.write(i + "\n")
