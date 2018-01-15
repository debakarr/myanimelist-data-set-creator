'''
This script can be used to download user dataset from [**Myanimelist**](https://myanimelist.net/) using an API, [**Kuristina**](https://github.com/TimboKZ/kuristina).

Column metadata:

* userID: MAL user ID animeID, 
* animeID: id of anime as in anime url https://myanimelist.net/anime/ID
* score: score by the use for anime with id = animeID (if user haven't score the anime then this field is 0).
'''

# importing libraries
import requests
import json
import sys

count = 0 # keep count of user for current session

try:
	userListFile = str(sys.argv[1]) # file name for userlist
except IndexError:
	print('Please provide all arguments.\nSyntax:\npython getUser.py UserList.txt [User.csv]')
	sys.exit()
except:
	print('Unexpected error.')

# setting name of output file
if(len(sys.argv) == 3):
	outputFile = str(sys.argv[2])
else:
	outputFile = 'User.csv'

f = open(userListFile, 'r') # opening file containing username in read mode
w = open(outputFile, 'w') # open output file in write mode

# header
w.write('userID, animeID, score\n')

for line in f:
	username = line.strip() # getting username

	print('Reading', username, 'AnimeList...') # console message

	apiUrl = 'https://kuristina.herokuapp.com/anime/' + username +'.json' # base url

	# API call to get JSON
	page = requests.get(apiUrl)
	c = page.content

	# Decoding JSON
	jsonData = json.loads(c)

	# checking if json data
	if(jsonData['myanimelist'] != None and 'anime' in jsonData['myanimelist']):
		# print total number of anime in the user list to the console
		print('There are', len(jsonData['myanimelist']['anime']), 'anime in the list. Writing to CSV...')

		count = count + 1 # Increament user count

		# write data to the file. Didn't used csv.writter
		for j in range(0, len(jsonData['myanimelist']['anime'])):
			userID = jsonData['myanimelist']['myinfo']['user_id']
			anime_id = jsonData['myanimelist']['anime'][j]['series_animedb_id']
			score = jsonData['myanimelist']['anime'][j]['my_score']
			w.write(str(userID) + ',' + anime_id + ',' + score + '\n')

		print('Writing data for', username, 'complete.') # console message
		print('Fetching next....\n')
	else:
		print(username, 'don\'t have any anime in their list.\n') # console message for those user who don't have any anime in their list

# closing file
f.close()
w.close()

print('Total', count, 'user data fetched.No more user left in', userListFile, '\nDone.\nOutput file:', outputFile)
