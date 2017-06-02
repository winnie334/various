#document.getElementById("enbut").click()       #doet alsof je op de enter knop drukt

from bs4 import BeautifulSoup
import requests, random

url = 'https://www.aap.org/en-us/about-the-aap/aap-press-room/pages/AAP-Advises-Against-Recreational-Trampoline-Use.aspx'
linklist = []
visited = []



for x in range(1,150):
    linklist = []
    print("Jumped to " + url)
    visited.append(url)
    while True:     #keeps retrying to connect until it gets the source code. Often not needed though
        try:
            sc = requests.get(url)
            if sc.status_code == 404:
                print("404 - page not found")
            break
        except requests.exceptions.ConnectionError:
            print("connection timed out")
        except requests.exceptions.InvalidSchema:
            print("heh? some weird schema error")
    pt = sc.text
    soup = BeautifulSoup(pt, "html.parser")
    for link in soup.findAll('a'):
        href = link.get('href')
        try:
            if ('http://' not in href) and (href[0] != '/'):
                continue
            if 'imgur' in href:
                continue
            if href[-4:] == '.xml':
                continue
        except:
            continue
        if href[0] == '/':
            linklist.append(url + href)
        else:
            linklist.append(href)

    print("Got " + str(len(linklist)) + " urls!")
    try:
        randnum = random.randrange(1, len(linklist))
    except ValueError:
        print("aww, we're out of urls!")
        break
    loopstopper = 0
    while linklist[randnum-1] in visited:
        randnum = random.randrange(1,len(linklist))
        loopstopper += 1
        if loopstopper > 100:
            print("we've visited all these links already!")
            break
    url = linklist[randnum-1]
