import requests

URL = 'https://superheroapi.com/api/2619421814940190/search/'

def the_most_intelligence(superhero_list):
    """
   самый умный(intelligence) из трех супергероев- Hulk, Captain America, Thanos. Для определения id нужно использовать метод /search/name
    """
    max_intelligence = 0
    hero_dict = {}
    for hero in superhero_list:
    	hero_url = URL + hero
    	response = requests.get(hero_url)
    	json_ = response.json()
    	hero_dict[hero] = int(json_['results'][0]['powerstats']['intelligence'])
    	if hero_dict[hero] > max_intelligence:
    		max_intelligence = hero_dict[hero]
    		ret = hero
    print(hero_dict)
    return ret

if __name__ == '__main__':
    print('Самый умный -', the_most_intelligence({'Hulk', 'Captain_America', 'Thanos'}))