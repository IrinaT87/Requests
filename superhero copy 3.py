import requests
from pprint import pprint
import json
heroes_list=['Hulk','Captain america', 'Thanos']
intelligence_dict = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}

# def get_heroes_info(name):
URI='https://akabab.github.io/superhero-api/api'
request='/all.json'
# response=list(filter(lambda person: person['name']==name, requests.get(url=URI+request).json()))

for hero in heroes_list:
    all_hero = requests.get(url=URI+request+hero)
    # intelligence_dict[hero] = int(all_hero['powerstats']['intelligence'])   
    pprint(all_hero)
    # print(intelligence_dict)    
    # print(len(response))
    # for el in response:
    #     for key, value in el.items():
    #         for name, zn in value.items():

           
                # Thanos=int(name['intelligence'])
                # pprint(name)
# get_heroes_info('Thanos')
# Hulk=get_heroes_info('Hulk')
# Captain_America=get_heroes_info('Captain America')




# def get_data(person_name, data):
# #     for key, value in data.items():
# #         if key==person_name:
#     with open (data.json) as f:
#         person_info=

