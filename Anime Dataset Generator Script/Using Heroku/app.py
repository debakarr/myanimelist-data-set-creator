import gspread
from oauth2client.service_account import ServiceAccountCredentials
import cfscrape
from bs4 import BeautifulSoup
import json
import sys
import re

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

requests = cfscrape.create_scraper()
lastUrl = "https://myanimelist.net/anime.php?em=0&ed=0&ey=0&o=2&c[0]=a&c[1]=d&cv=1&w=0&sd=21&sm=4&sy=2018&o=2&w=1"
page = requests.get(lastUrl)
soup = BeautifulSoup(page.content, 'html.parser')
x = soup.findAll("a", {"class": "hoverinfo_trigger fw-b fl-l"})[0]['href']
lastAnimeID = re.search(r'anime/([0-9]+)/', x).group(1)

# Paste the data given below in the spreadsheet and the split it into columns
# animeID, name, premiered, genre, type, episodes, producer, licensor, studio, source, scored, scoredBy, members
sheet = client.open('animeData').sheet1

last_row = len(sheet.col_values(1))
print(last_row)
if(last_row < 2):
	lastAnimeInsertedInSheet = 0
else:
	lastAnimeInsertedInSheet = sheet.cell(last_row, 1).value

if int(lastAnimeInsertedInSheet) == int(lastAnimeID):
	sys.exit(0)

start = int(lastAnimeInsertedInSheet)

for i in range(start + 1, start + 1000):
	apiUrl = 'http://api.jikan.moe/anime/' + str(i)

	page = requests.get(apiUrl)

	retry = 0

	print('STATUS CODE:', page.status_code)

	while page.status_code == 429:
		retry = retry + 1
		print('Limit reached. Too many request. Retrying..')
		print('Retry count:', retry)
		page = requests.get(apiUrl)

	c = page.content

	try:
		print('Fetching JSON...')
	except:
		print("Unexpected error:", sys.exc_info()[0])
		continue

	jsonData = json.loads(c)

	if('error' not in jsonData):
		l = []

		name = jsonData['title']

		print('Reading', name, 'animelist...')

		studio = []
		genre = []
		producer = []
		licensor = []

		for j in range(0, len(jsonData['licensor'])):
			licensor.append(jsonData['licensor'][j]['name'])

		for j in range(0, len(jsonData['producer'])):
			producer.append(jsonData['producer'][j]['name'])

		for j in range(0, len(jsonData['studio'])):
			studio.append(jsonData['studio'][j]['name'])

		for j in range(0, len(jsonData['genre'])):
			genre.append(jsonData['genre'][j]['name'])

		l.append(str(i))
		l.append(str(name))
		l.append(str(jsonData['premiered']))
		l.append(str(genre))
		l.append(str(jsonData['type']))
		l.append(str(jsonData['episodes']))
		l.append(str(producer))
		l.append(str(licensor))
		l.append(str(studio))
		l.append(str(jsonData['source']))
		l.append(str(jsonData['score']))
		l.append(str(jsonData['scored_by']))
		l.append(str(jsonData['members']))
		print(l)
		sheet.append_row(l, value_input_option='RAW')