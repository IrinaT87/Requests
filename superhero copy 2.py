import requests
from pprint import pprint
import json

intelligence={}
def get_heroes_info(name):
    URI='https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    request=' /id'
    response=list(filter(lambda person: person['name']==name, requests.get(url=URI+request).json()))
    # intelligegence_hero=
    pprint(response)
    
    # print(len(response))
    # for el in response:
    #     for key, value in el.items():
    #         for name, zn in value.items():

           
                # Thanos=int(name['intelligence'])
                # pprint(name)
get_heroes_info('Thanos')
# Hulk=get_heroes_info('Hulk')
# Captain_America=get_heroes_info('Captain America')




# def get_data(person_name, data):
# #     for key, value in data.items():
# #         if key==person_name:
#     with open (data.json) as f:
#         person_info=

