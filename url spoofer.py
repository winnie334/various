
from urllib import request
import random
import os.path
import shutil

url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=8&b=12&c=2016&d=9&e=12&f=2016&g=d&ignore=.csv'
url=list("http://chart.finance.yahoo.com/table.csv?s=GOOG&a=8&b=12&c=2016&d=9&e=12&f=2016&g=d&ignore=.csv")
alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
vowels=list("AEIOU")
path = r'C:\Users\winand\PycharmProjects\testie\stocks'

if not os.path.exists(path):
    os.makedirs(path)

def download(link,number):
    try:
        response = request.urlopen(link)
        csv = response.read()
        csv_str = str(csv)
        lines = csv_str.split("\\n")
        name = 'stock ' + link[43:47] + r'.csv'
        stock = os.path.join(path, name)
        fw = open(stock, "w")
        for x in lines:
            fw.write(x + "\n")
        fw.close()
        print(link[43:47] + "  succesfully downloaded!")
        return 1
    except:
        print(link[43:47] + "  is not valid  (try " + str(number) + ", " + str(succes) +" found so far)")
        return 0

def newletter():
    if random.randrange(1,3) > 1:
        letter = random.randrange(0,25)
        return("".join(alphabet[letter:letter+1]))
    else:
        letter = random.randrange(0,4)
        return ("".join(vowels[letter:letter + 1]))


succes = 0
for x in range(1,300):

    code = newletter() + newletter() + newletter() + newletter()
    url[43:47] = code
    succes = download("".join(url),x) + succes


'''
number = 1
download("".join(url))
number = 2
url[43:47] = "IXIC"
download("".join(url))
'''



percent = succes/x
roundpercent = round(percent,3) *100

print("done, " + str(succes) + " codes have been found!")
print(str(roundpercent) + "% of the codes were correct ones.")

shutil.rmtree(path)