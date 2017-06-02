from bs4 import BeautifulSoup
import requests
from defs import steamlogin, makesoup
from selenium import webdriver
import time


def getfriendurls(steamurl):                             # this will update your list of friends
    sourcecode = requests.get(steamurl).text
    soup = BeautifulSoup(sourcecode, "html.parser")
    steamlinkson = soup.find_all('div', {'class': 'friendBlock persona online'})
    steamlinksoff = soup.find_all('div', {'class': 'friendBlock persona offline'})
    steamlinks = steamlinksoff + steamlinkson
    print(str(len(steamlinks)) + ' friends found!')
    links = []
    for link in steamlinks:
        href = link.find('a')
        url = href['href']
        links.append(url)
    return links


def sendwishes(steamurls):
    driver = steamlogin()
    for friend in steamurls:
        if friend not in open('ppl_messaged.txt').read():
            driver.get(friend)
            try:
                textarea = driver.find_element_by_class_name('commentthread_textarea')
                textarea.send_keys('Merry Christmas!')
                button = driver.find_element_by_css_selector('.btn_green_white_innerfade.btn_small')
                button.click()
                print('Wished ' + friend + ' a merry christmas!')
                time.sleep(1)
            except Exception as e:
                print('error: ' + str(e))
                print(friend + ' did not want to receive wishes!')
            ppl = open('ppl_messaged.txt', 'a')
            ppl.write(friend + '\n')
            ppl.close()
        else:
            print(friend + ' already messaged.')


links = getfriendurls('http://steamcommunity.com/profiles/76561198091623271/friends/')
sendwishes(links)
