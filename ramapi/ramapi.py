import requests
base_url="https://rickandmortyapi.com/api/"
character_url=base_url+"character/"
location_url=base_url+"location/"
episode_url=base_url+"episode/"

class Base():
	def api_info():
		return requests.get(base_url).json()

	def schema():
		temp=requests.get(character_url).json()
		return temp['info'].keys()


class Character():

	def get_all():
		return requests.get(character_url).json()

	def get_page(number):
		return requests.get(character_url+'?page='+str(number)).json()

	def get(id=None):
		if id==None:
			print("You need to pass id of character to get output.")
			print("To get list of all characters, use getall() method.")
			return
		return requests.get(character_url+str(id)).json()

	def filter(**kwargs):
		for value in kwargs:
				kwargs[value]=value+"="+kwargs[value]
		query_url='&'.join([values for values in kwargs.values()])
		final_url=character_url+"?"+query_url
		return requests.get(final_url).json()

	def schema():
		temp=requests.get(character_url).json()
		return temp['results'][0].keys()

class Location():

	def get_all():
		return requests.get(location_url).json()

	def get(id=None):
		if id==None:
			print("You need to pass id of character to get output.")
			print("To get list of all characters, use getall() method.")
			return
		return requests.get(location_url+str(id)).json()

	def filter(**kwargs):
		for value in kwargs:
				kwargs[value]=value+"="+kwargs[value]
		query_url='&'.join([values for values in kwargs.values()])
		final_url=location_url+'?'+query_url
		return requests.get(final_url).json()

	def schema():
		temp=requests.get(location_url).json()
		return temp['results'][0].keys()


class Episode():

	def get_all():
		return requests.get(episode_url).json()

	def get(id=None):
		if id==None:
			print("You need to pass id of character to get output.")
			print("To get list of all characters, use getall() method.")
			return
		return requests.get(episode_url+str(id)).json()

	def filter(**kwargs):
		for value in kwargs:
				kwargs[value]=value+"="+kwargs[value]
		query_url='&'.join([values for values in kwargs.values()])
		final_url=episode_url+'?'+query_url
		return requests.get(final_url).json()

	def schema():
		temp=requests.get(episode_url).json()
		return temp['results'][0].keys()

		


			



