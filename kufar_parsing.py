from bs4 import BeautifulSoup
import requests

def save():
	with open('parse_info.txt', 'a') as file:
		file.write(f'{comp["title"]} -> Price: {comp["price"]}\n')
def parse():

	URL = 'https://www.kufar.by/listings?cat=16040&ot=1&query=macbook&rgn=all'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
		
	}
	responce = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(responce.content, 'html.parser')
	items = soup.findAll('div', class_ ='k-cOXq-12dd7')
	comps = []


	for item in items:
		comps.append({
			'title': item.find('h3', class_ = 'k-cOXJ-93f0b').get_text(strip = True),
			'price': item.find('span', class_ = 'k-XrmR-9e791').get_text(strip = True)
			})
		global comp
		for comp in comps:
			print(f'{comp["title"]} -> Price: {comp["price"]}')
			save()
			

parse()