#%%
import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')
yc_webpage = response.text #html code
# print(yc_webpage)

soup = BeautifulSoup(yc_webpage, 'html.parser') #parse the html code

article_tag = soup.find_all(name='span', class_='titleline') #find the first article

article_upvote = soup.find_all(name='span', class_='score') #find the upvote of the article


article_tag_arr = [article.getText() for article in article_tag] #get the text of the article
article_link_arr = [article.find(name='a').get('href') for article in article_tag] #get the link of the article
article_upvote_arr = [int(article_score.getText().split()[0]) for article_score in article_upvote] #get the upvote of the article

print(article_tag_arr)
print(article_link_arr)
print(article_upvote_arr)




















