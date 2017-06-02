#old code for documentation
'''


from bs4 import BeautifulSoup
import requests


alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

def nextcode(oldcode):
    oldcode = list(oldcode)
    currentchar = 1
    done = 0
    while done == 0:
        if oldcode[-currentchar] == '9':
            oldcode[-currentchar] = 'a'
            currentchar += 1
        if oldcode[-currentchar] != '9':
            position = alphabet.index(oldcode[-currentchar])
            oldcode[-currentchar] = alphabet[position + 1]
            done = 1
    return "".join(oldcode)


def attempt(code, max_attempts):
    attempts = 1
    unvalid = '[<div class="welcome_font"></div>, <div class="welcome_font">Something bad happened!</div>]'
    while attempts <= max_attempts:
        try:
            url = 'http://tf2r.com/k' + str(code) + r'.html'
            plain_source_code = (requests.get(url)).text
            soup = BeautifulSoup(plain_source_code, "html.parser")
            validness = soup.findAll('div',{'class': 'welcome_font'})
            if attempts%50 == 0:
                print(str(attempts) + " attempts...")
                if attempts%500 == 0:
                    filew = open('raffles.txt', 'a')
                    filew.write(str(attempts) + " attempts...  \n")
                    filew.close()
            if str(validness) != unvalid:
                print("woop woop! You found one.")
                filew = open('raffles.txt', 'a')
                filew.write("tf2r.com/k" + str(code) + ".html\n")
                filew.close()
            attempts += 1
            code = nextcode(str(code))
        except:
            print("something went wrong... ohoh")
            print("current code for emergencies: " + str(code))

    return "done with processing, final code was " + str(code)



'''




from bs4 import BeautifulSoup
import requests
import time
import math

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

def sectohour(secondsI):
    hours = int(secondsI/ 3600)
    minutes = int((secondsI % 3600) / 60)
    seconds = int(secondsI % 60)
    return [hours, minutes, seconds]

def nextcode(oldcode):                  # generates the next code
    oldcode = list(oldcode)
    currentchar = 1
    done = 0
    while done == 0:
        if oldcode[-currentchar] == '9':        # if the current character we're looking at is a 9, make it an a and
            oldcode[-currentchar] = 'a'         # increment the character before
            currentchar += 1
        if oldcode[-currentchar] != '9':
            position = alphabet.index(oldcode[-currentchar])
            oldcode[-currentchar] = alphabet[position + 1]
            done = 1
    return "".join(oldcode)



def nextpuzzlecode(oldcode):
    oldcode = list(oldcode)
    currentchar = fillers[-1]
    fillerpos = 1
    done = 0
    while done == 0:
        if oldcode[currentchar] == (knownchars[currentchar])[-1]:
            oldcode[currentchar] = (knownchars[currentchar])[0]
            fillerpos +=1
            currentchar = fillers[-fillerpos]
        else:
            position = knownchars[currentchar].index(oldcode[currentchar])
            oldcode[currentchar] = (knownchars[currentchar])[position + 1]
            done = 1
    return "".join(oldcode)






def attempt(code, max_attempts, puzzle):
    attempts = 1
    found = 0
    actives = 0
    while attempts <= max_attempts - puzzle:
        try:
            url = 'http://tf2r.com/k' + str(code) + r'.html'        # makes a new string with the code
            r = requests.get(url, allow_redirects=False)            # gets results, 200 means it's not a redirect
            if attempts%100 == 0:                                    # print progress every 100 attempts
                print(str(attempts) + " attempts...")
                '''if attempts%500 == 0:
                    filew = open('raffles.txt', 'a')
                    filew.write(str(attempts) + " attempts...  \n")
                    filew.close()'''
            if r.status_code == 200:                                                    # 200 means no redirect
                print("woop woop! You found one.")
                found += 1
                source_code = (requests.get(url)).text                                  # if you found a raffle, get the
                soup = BeautifulSoup(source_code, "html.parser")                        # source code. Then search for
                validness = soup.findAll('script', {'type': 'text/javascript'})         # the var 'ended' and check
                wwn = str(validness[5].contents)[265:269]                               # whether it's true.
                if wwn == 'true':
                    ended = '(ended)'
                else:
                    ended = '(STILL ACTIVE!)'
                    print("This one is still active!")
                    actives += 1
                entries = soup.find('td',{'id':'entry'}).text
                filew = open('raffles.txt', 'a')                                        # note we open it with 'a'
                filew.write("tf2r.com/k" + str(code) + ".html    Entries: " + entries + '\t\t' + ended + '\n')       # writes down the raffle link
                filew.close()


            attempts += 1
            if puzzle is False:
                code = nextcode(str(code))
            elif puzzle is True:
                code = nextpuzzlecode(str(code))
        except Exception as e:
            print("something went wrong... ohoh")                       # in case of a disconnect or another problem,
            print("current code for emergencies: " + str(code))         # this'll make sure we don't lose progress.
            print("error: " + str(e))

    return "\ndone with processing, the final code is " + str(code) + ".\nFound " + str(found) + " existing raffles, whereof " + str(actives) + " active ones."


knownchars = [['p'],['4'],['z'],['7'],['*'],['*']]              # [['*'],['*'],['*'],['*'],['*'],['*']] in case you need it
if knownchars == [['*'],['*'],['*'],['*'],['*'],['*']]:
    puzzle = False
    starting_code = 'rbrvpa'
    max_attempts = 500000
else:
    starting_code = ""
    fillers = []
    puzzle = True
    max_attempts = 1
    for pos, i in enumerate(knownchars):
        if i == ['*']:
            max_attempts *= 36
            starting_code += 'a'
            knownchars[pos] = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
            fillers.append(pos)
        elif len(i) > 1:
            max_attempts *= len(i)
            starting_code += i[0]
            fillers.append(pos)
        else:
            starting_code += i[0]



starting_time = time.clock()
timeguess = max_attempts/21
timelist = sectohour(timeguess)
MB = (timeguess * 186)/1000

print("started with processing, parameters below.")
print("starting code: " + starting_code + "   max. attemtps: " + str(max_attempts))
print("Estimated duration: " + str(timelist[0]) + " hours, " + str(timelist[1]) + " minutes and " + str(timelist[2]) +" seconds.")
print("Estimated use of resources: " + str(round(MB,3)) + " MB")
filew = open('raffles.txt', 'a')
filew.write("\n\n------------------------------------------------------------\n")
filew.write("New processing started, using the following parameters:\n" + "starting code: " + starting_code + "   max. attempts: " + str(max_attempts) + "\n\n")
filew.close()

endcode = attempt(starting_code,max_attempts,puzzle)

print(endcode)
ending_time = time.clock()
time_elapsed = ending_time - starting_time
timelist = sectohour(time_elapsed)


MB2 = (time_elapsed * 186)/1000
print("The processing took " + str(timelist[0]) + " hours, " + str(timelist[1]) + " minutes and " + str(timelist[2]) +" seconds.")
print("Attempts per second rate: " + str(round(max_attempts/time_elapsed,3)))
print("Resources used: ~" + str(round(MB2,3)) + " MB. (" + ("+" if MB<MB2 else "") + str(round(MB2-MB,3)) + " MB)")
filew = open('raffles.txt', 'a')
filew.write(endcode + "\nThe processing took " + str(timelist[0]) + " hours, " + str(timelist[1]) + " minutes and " + str(timelist[2]) +" seconds.")
filew.close()

