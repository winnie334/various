from notifier import balloon_tip
from bs4 import BeautifulSoup
import requests, time

website = "http://rust.facepunch.com/commits/2017/June" 	# should be changed every month.
textfile = r"C:\Users\winnie33\PycharmProjects\testie\commits.txt"
icon = r"C:\Users\winnie33\PycharmProjects\testie\rusticon.ico"

def getcommits():
	source = requests.get(website)
	soup = BeautifulSoup(source.text, "html.parser")
	commitlist = soup.findAll('div', {'class' : 'pre'})		# we find all the commits
	for index, commit in enumerate(commitlist):
		commitlist[index] = commit.text.split('\n')		# we strip the commits from <div> tags and newlines
	commitlist = [item.strip('\r') for sublist in commitlist for item in sublist]	# flatten, also remove \r's
	return commitlist

if __name__ == '__main__':
	rclass = balloon_tip("I'm starting!", "Let's hope the commits will be plenty!", icon)
	while True:
		currentcommitlist = getcommits()
		loggedcommits = [x.strip('\n') for x in open(textfile, 'r').readlines()]	# loads in already checked commits
		for commit in currentcommitlist:
			if commit not in loggedcommits:
				commitfile = open(textfile, 'a')
				balloon_tip('New commit!', commit, icon, rclass)
				commitfile.write('\n' + commit)		# write the commit to a file so we don't notify again later
				commitfile.close()
		time.sleep(300)
