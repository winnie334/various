# from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import subprocess
from defs import steamlogin

nsfw_links = []
seen_messages = []
loop = 0



driver = steamlogin()
driver.get("http://tf2r.com/chat.html")


while 1:
    sourcecode = driver.page_source
    soup = BeautifulSoup(sourcecode, "html.parser")
    messages = soup.find_all('div', {'class':'ufmes'})
    linklist = open("links.txt", 'a')
    alllogs = open("chatlogs.txt", 'a')
    for post in messages:
        textpost = post.text
        if textpost not in seen_messages:
            try:
                alllogs.write(textpost + '\n')
                seen_messages.append(textpost)
            except UnicodeEncodeError:
                alllogs.write('woow, something went wrong!' + '\n')
        if ('nsfw' in textpost or 'NSFW' in textpost) and (textpost not in nsfw_links):
            nsfw_links.append(textpost)
            linklist.write(textpost + '\n')
            print("added " + textpost)
    linklist.close()
    alllogs.close()
    print("Scanned chat, already elapsed " + str(loop*10) + " minutes.")
    loop += 1
    sleep(600)



'''
codebox = driver.find_element_by_id("twofactorcode_entry")
code = input('mobile pass? ')
codebox.send_keys(code)
button2 = driver.find_element_by_css_selector('.auth_button.leftbtn')
print(button2)
button2.click()
'''

