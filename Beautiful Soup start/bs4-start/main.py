from pprint import pprint
from typing import Any

from bs4 import BeautifulSoup
import requests
# import lxml
#
#
# with open("website.html", 'r') as f:
#     content = f.read()
#     # print(content)
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.prettify())
# anchor_tags= soup.find_all(name="a")
# # print(anchor_tags)
# # print(soup.title)
# # print(soup.title.name)
# for anchor in anchor_tags:
#     print(anchor.getText())
#     print(anchor.get('href'))
#
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
# h3 = soup.find(name="h3", class_="heading")
# print(h3.getText())
# company_url = soup.select_one(selector="p a")
# print(company_url)
response = requests.get(url='https://news.ycombinator.com/news')
response.raise_for_status()
yc_web= response.text
# pprint(yc_web)
soup = BeautifulSoup(yc_web,'html.parser')
print(soup.title.string)
title_spans = soup.find_all("span", class_="titleline")
# print(articles)
article_text=[]

article_links=[]
# one_more = soup.find(name='a', class_='titleline')
for span in title_spans:
    article = span.find("a")
    article_text.append(article.getText())
    article_links.append(article["href"])

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]
print(article_text)
print(article_upvotes)
print(article_links)
largest = max(article_upvotes)
largest_index = article_upvotes.index(largest)
print(article_text[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])




# print(article_text)


# print(article_upvotes.get_text())

# anchore =first.find('a')


