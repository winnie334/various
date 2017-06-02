
import requests
from bs4 import BeautifulSoup

def crawler(max_pages):
    page = 1
    while page <= max_pages:
            url = 'http://wtffunfact.com/page/' + str(page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text)
            for link in soup.findAll('div', {'class' : 'note-count'}):
                href = link.find('a')['href']
                print(href)
            page = page + 1


def madness(facturl):
    source_code = requests.get(facturl)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)

madness('http://wtffunfact.com/post/151684820813/tipperary-hill-ny-wtf-fun-facts')