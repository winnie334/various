'''

if 4>5:
    print("long live the king")
elif 4<5:
    print("truepapedipapedoe")
elif 4<10:
    print("really else if?")

x=0.1
drinks = ["lists", "are", "awesome", "but","are","spaces","needed?"]

for i in drinks:
    print(i)
    if i == "awesome":
        print("awesome!")
    else:
        print("not awesome :(")

a=1

for x in range(-100,100):
    a = (x < 4) + a

print(a)

'''

'''
def lookforrest(first,last):
    return first%last


Gevonden = []

for a in range(0,100):
    Gevonden.insert(a,0)
print("done!")



for b in range(1,20):
    for a in range(1,100):
        if lookforrest(a,b) == 0:
            print(a,"is een veelvoud van",b)
            Gevonden[a] = 1+Gevonden[a]



print("het meestvonden cijfer is",Gevonden.index(max(Gevonden)),"en het is",max(Gevonden),"keer gebruikt.")
'''

'''
def Line():
    print("------------------------------------")


import random
Code = round(random.random() * 100000000, 0)
for x in range(1,100000000):
    if x == Code:
        Line()
        print("number found! it was", Code)
        Line()
        break
    elif x%1000000 == 0:
        print(x,"attempts...")

    if x%10000000 == 0:
        Line()
'''

'''
planes = {'mark':'red and big','shog':'japanese and robots','vlox':'friend and cool'}
ROB = ["SOUP","BREAD","EATING"]


for v in ROB:
    print(v)
for v,k in planes.items():
    print(v, " ", k)

'''


'''
import random
import urllib.request

def Download(url):
    number = random.randrange(1,1000)
    full_name = str(number) + ".png"
    urllib.request.urlretrieve(url, full_name)

filew = open('ooyoy.txt', 'w')
filew.write("OYOYOY\nEYEYEYEY")

filew.close()

filer = open('ooyoy.txt', 'r')
text = filer.read()
print(text)
filer.close()
'''

import requests
from bs4 import BeautifulSoup

'''
url = 'http://tf2r.com/kkj1ff8.html'
plain_source_code = (requests.head(url))
print(plain_source_code.status_code)
soup = BeautifulSoup(plain_source_code, "html.parser")
validness = soup.find('td',{'id':'entry'}).text
print(validness)
'''

'''
wordpath = 'C:\\Users\winand\Documents\Wordlist'

allwords = open('C:\\Users\winand\Documents\Wordlist\\allwords.txt', 'a')
textsource = requests.get('http://www.mit.edu/~ecprice/wordlist.10000').text
soup = BeautifulSoup(textsource, 'html.parser')
words = soup.text
for word in words:
    allwords.write(word)
#nou dat ging vlot
'''

class ExampleClass:
	def __init__(self, creation):
		print('yay, im created!')
		self.creation = creation

	x = 123


	def yay(self, inputnumber):
		print('you asked for:')
		print(inputnumber *2)

go = ExampleClass('mark')
go.yay(3)
print(go.creation)