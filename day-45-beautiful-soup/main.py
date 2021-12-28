from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

all_titles = [title.text for title in soup.find_all(name="h3", class_="title")][::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in all_titles:
        file.write(f"{title}\n")





# response = requests.get(url="https://news.ycombinator.com/news")
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.find_all(name="a", class_="titlelink")
# article_texts = []
# article_links = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#
# print(article_texts)
# print(article_links)
# print(article_upvotes)
#
# print("-------------")
#
# largest_number = article_upvotes.index(max(article_upvotes))
# print(article_texts[largest_number + 1])
# print(article_links[largest_number + 1])
# print(article_upvotes[largest_number])
#
#
















#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.text)
# # print(soup.title.string)
#
# # all_anchor_tags = soup.find_all("a")        # Get hold of all the anchor tags
# # for tag in all_anchor_tags:
# #     print(tag.getText())        # Getting a text in a tag
# #     print(tag.get("href"))
#
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)      # Can specify chosen attribute by using heading.get("id"), heading.text, heading.name
#
# # section_heading = soup.find(name="h3", class_="heading")      # The same as above, but more accurate specifying class_
# # print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")       # Here we looking at "a" tag, which is in "p" tag. Specific search
# name = soup.select_one(selector="#name")        # Searching by css attributes #name, also can use .class
#
# headings = soup.select(selector=".heading")     # All elements, that have .heading class
# print(headings)
