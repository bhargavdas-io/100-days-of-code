# with open("website.html", encoding="utf8") as website:
#     contents = website.read()
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.prettify())
# #print(soup.ul)
# #print(soup.title.string)
# all_p_tags = soup.find_all(name="p")
# # for i in all_p_tags:
# #     text = i.get_text()
# #     print(text)
# all_anchor_tags = soup.find_all(name="a")
#
# # for links in all_anchor_tags:
# #     print(links.get("href"))
#
# # finding_by_attribute = soup.find("h1", id="name")
# #
# # print(finding_by_attribute.string)
#
# finding_by_attribute = soup.find(name="h3", class_="heading")
# print(finding_by_attribute)


from bs4 import BeautifulSoup

import requests
import numpy as np

response = requests.get(url="https://news.ycombinator.com/news")
yc_page = response.text
soup = BeautifulSoup(yc_page, "html.parser")

article_list = []
links_list = []

a_tag = soup.find_all(name="span", class_="titleline")
for articles in a_tag:
    article_text = articles.getText()
    article_list.append(article_text)

article_link = soup.find_all("span", class_="titleline")
for span in article_link:
    links = span.find_all('a')
    for link in links:
        web_links = link.get("href")
        links_list.append(web_links)

new_links = links_list[0:len(links_list):2]
upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_list)
# print(upvotes)

largest_number = max(upvotes)
largest_index = upvotes.index(largest_number)

print(article_list[largest_index])
print(new_links[largest_index])
print(f"Total upvotes: {largest_number}")

