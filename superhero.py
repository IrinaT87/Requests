import requests
import json

intelligence_dict={}
def get_heroes_info(*name):
    URI='https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    request='/all.json'
    for n in name:
        response=list(filter(lambda hero: hero['name']==n, requests.get(url=URI+request).json()))
        for el in response:
            intelligence=el['powerstats']['intelligence']
            intelligence_dict[n]=intelligence
    
get_heroes_info(*['Thanos','Hulk','Captain America'])

print(intelligence_dict)
max_intelligence = max(intelligence_dict, key=intelligence_dict.get)
print(f'Самый умный супергерой: {max_intelligence}')
