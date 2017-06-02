from bs4 import BeautifulSoup
import requests, time, threading
from operator import itemgetter
alphabet = "abcdefghijklmnopqrstuvwxyz"     #always comes in handy
wordpath = "C:\\Users\winand\Documents\Wordlist\\allwords.txt"
totalresults = {}

def nextword(currentpos):
    words = open(wordpath, 'r')
    for pos, word in enumerate(words):
        if pos == currentpos + 1:
            words.close()
            return pos, word
        elif pos > currentpos + 2:
            print('something went wrong!')
            break



def increase(startstring):
    startlist = list(startstring)
    currentchar = -1
    while currentchar>-10:
        if startlist[currentchar] != 'z':
            if startlist[currentchar] == ' ':
                startlist[currentchar] = 'a'
            else:
                startlist[currentchar] = chr(ord(startlist[currentchar])+1)
            break
        elif startlist[currentchar] == 'z':
            startlist[currentchar] = 'a'
            currentchar -= 1
    return "".join(startlist)

def getresults(keyword):
    page_source = requests.get('https://www.google.be/search?q=' + keyword)
    source_code = page_source.text
    soup = BeautifulSoup(source_code, "html.parser")
    result = soup.find('div', {'id' : 'resultStats'}).text
    amount = []
    for char in result:
        if char in '0123456789':
            amount.append(char)
    amount = int(''.join(amount))
    totalresults[keyword] = amount



def mainloop(startpos, maxtries):

    tries = 0
    starttime = time.clock()
    lasttime = starttime
    while tries < maxtries:
        startpos, word = nextword(startpos)
        thread = threading.Thread(target = getresults, args = (word,))
        thread.start()
        tries += 1
        if round(tries/maxtries, 0) % 5 == 0 and round(tries/maxtries, 0) != 0:
            print('already at ' + str(round(tries/maxtries, 0)) + ' percent!')
        if time.clock() >= lasttime + 60:
            lasttime = time.clock()
            print('currently at word ' + str(startpos) + ', the word: ' + word)
    sortedresults = sorted(totalresults.items(), key=itemgetter(1), reverse=True)
    for key, value in sortedresults:
        print(key + '\t' + str(value))

mainloop(1, 500)






