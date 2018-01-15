'''
This script can be used to create user list from [**Myanimelist**](https://myanimelist.net/) using any forum post.
The idea is to extract user fro the post.

Output file contains list of username, one at each line.
'''

from bs4 import BeautifulSoup
import requests
import sys

# getting topic ID
# topic ID get be seen in the url of any forum post 
# Example: this url 'https://myanimelist.net/forum/?topicid=1582476' have a topic ID = 1582476
try:
	clubID = int(sys.argv[1])
except IndexError:
	print('Please provide all arguments.\nSyntax:\npython creteUserListFromPost.py topicID [UserList.txt]')
	sys.exit()
except:
	print('Unexpected error.')

# setting name of output file
if(len(sys.argv) == 3):
	outputFile = str(sys.argv[2])
else:
	outputFile = 'UserList.txt'

f = open(outputFile, 'w') # opening output file in write mode

i = 0 # initial user counter
count = 0 # storing number of users

while(True):
	print('\nFetching username from users number', i + 1, 'through user number', i + 36, '...') # console message indicating number of comments

	parameter = {"action":"view", "t":"members", "id":clubID, "show":i} # # Set up the parameters we want to pass

	url = 'https://myanimelist.net/clubs.php' # base url

	page = requests.get(url, params=parameter) # getting page

	if(page.status_code == 200):
		c = page.content
		soup = BeautifulSoup(c, 'html.parser') # parsing page

		print('Getting username:')
		# getting username in the page
		users = soup.find_all('td', 'borderClass')
		for j in range(0, len(users)):
			count = count + 1
			print(users[j].div.a.text)
			f.write(users[j].div.a.text + '\n') # Writing unique username in the output file

		i = i + 36 # increamenting user count
	else:
		print('No more page left in the forum. Done fetching...\n')
		break

print('Got', count, 'unique user.')

f.close() # closing file

print('Done writing username to output file.\nOutput:', outputFile) 