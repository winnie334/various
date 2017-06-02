from selenium import webdriver
import pyautogui as pag
import time
from selenium.common.exceptions import NoSuchElementException, InvalidElementStateException, StaleElementReferenceException

def log(logtext):
	filew = open('chatlogs\chatlog.txt', 'a')
	filew.write(logtext + '\n')
	filew.close()


def waitthenclick(filename, click=1): # clicks on something as soon as it sees it.
	path = r'images\\' + filename + '.png'
	loc = None
	while loc is None:
		print('trying to find ' + filename)
		loc = pag.locateCenterOnScreen(path)
	if click == 1:
		pag.click(loc)
		print('clicked on ' + filename)


def startomegle(): # launch omegle and all that
	browser.get('http://www.omegle.com')
	time.sleep(1)
	waitthenclick('selecteer')
	waitthenclick('engels')
	time.sleep(0.5)
	waitthenclick('text')
	print('launched omegle!')
	return browser


def waittillchatstart(): # waits till we know the chat has begun
	found = None
	print('waiting till chat start...')
	while found != "You're now chatting with a random stranger. Say hi!":
		try:
			found = browser.find_element_by_class_name('statuslog').get_attribute('innerHTML')
		except NoSuchElementException:
			time.sleep(0.5)
			pass
		except StaleElementReferenceException:
			pass
	print('chat started!')
	time.sleep(0.5)


def sendmessage(message): # sends a message
	try:
		textbox = browser.find_element_by_class_name('chatmsg')
		sendbutton = browser.find_element_by_class_name('sendbtn')
		textbox.send_keys(message)
		sendbutton.click()
		return 0
	except InvalidElementStateException:
		# print("eeeh, too fast? Or they disconnected. Who knows, they're dead to us now.")
		return 1

def gettextamount(): # gets the amount of replies we've already gotten
	elements = browser.find_elements_by_class_name('strangermsg')
	return len(elements)

def gettexts(): # gets the value of their last message
	elements = browser.find_elements_by_class_name('strangermsg')
	htmlshit = elements[-1].get_attribute('innerHTML')
	message = htmlshit[htmlshit.index('<span>') + 6: htmlshit.index('</span>')]
	if message != theirmessages[-1]:
		theirmessages.append(message)
		log(message)
		return message

def waitforresponse(): # wait till the other person answers
	currentamount = gettextamount()
	timeout = time.time() + 30
	while currentamount == gettextamount() and time.time() < timeout:
		time.sleep(1)
	if time.time() > timeout:
		print('timed out!')
		return 1
	return 0


def checkifdone(): # checks if we're done yet with the chat
	newbutton = 0
	try:
		browser.find_element_by_class_name('newchatbtnwrapper')
		newbutton = 1
	except:
		pass
	return newbutton

def sendandwait(message): # handy wrapper
	if sendmessage(message) == 1:
		return
	if waitforresponse() == 1:
		return
	gettexts()

def newchat():
	try:
		browser.find_element_by_class_name('newchatbtnwrapper')
	except NoSuchElementException:
		print("apparently we hadn't disconnected yet. Well, now we have.")
		disco = browser.find_element_by_class_name('disconnectbtn')
		disco.click(); time.sleep(0.5); disco.click(); time.sleep(0.5)
	newchat = browser.find_element_by_class_name('disconnectbtn')
	newchat.click()


def chat():
	# while checkifdone() == 0:
	sendandwait('hey')
	sendandwait("I have to admit something. I'm a bot, and I'm trying to gather data. Would you like to help?")
	sendandwait("Awesome! Please, enter a random number from 1-100.")
	sendandwait("Thanks a lot. That was it, if there's anything you'd like to say please do it now.")
	sendmessage("Alrighty, see you next time!")

if __name__ == '__main__':
	theirmessages = ['Pass~']
	browser = webdriver.Chrome('D:\\Users\winand\AppData\Local\Programs\Python\Python35-32\selenium\webdriver\chrome\chromedriver.exe')
	startomegle()
	waittillchatstart()
	time.sleep(1)
	while True:
		chat()
		print('done with chatting')
		newchat()
		waittillchatstart()


