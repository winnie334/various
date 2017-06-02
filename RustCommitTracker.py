from notifier import balloon_tip
from bs4 import BeautifulSoup
import requests

website = "http://rust.facepunch.com/commits/2017/June" 	# should be changed every month.

def getcommits():
	source = requests.get(website)
	soup = BeautifulSoup(source.text, "html.parser")
	commitlist = soup.findAll('div', {'class' : 'pre'})		# we find all the commits
	for index, commit in enumerate(commitlist):
		commitlist[index] = commit.text.split('\n')		# we strip the commits from <div> tags and newlines
	commitlist = [item.strip('\r') for sublist in commitlist for item in sublist]	# flatten, also remove \r's
	return commitlist

if __name__ == '__main__':
	currentcommitlist = getcommits()
	loggedcommits = [x.strip('\n') for x in open('commits.txt', 'r').readlines()]	# loads in already checked commits
	commitfile = open('commits.txt', 'a')
	for commit in currentcommitlist:
		if commit not in loggedcommits:
			balloon_tip('New commit!', commit, 'rusticon.ico')
			commitfile.write('\n' + commit)
