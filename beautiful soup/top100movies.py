import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
empire_webpage = response.text #html code

soup = BeautifulSoup(empire_webpage, 'html.parser') #parse the html code
