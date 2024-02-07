import json
import requests
from settings import json_data, headers
from schema import SLego

def get_lego_json():
    lego_json = []
    data = json.loads(requests.post('https://www.lego.com/api/graphql/ContentPageQuery', headers=headers, json=json_data).text)
    
  
    for lego in data.get('data').get('contentPage').get('contentBody')[-2].get('section').get('products')['results']:
                item = SLego(**lego)
                lego_json.append(item.model_dump())
    return lego_json

def get_simple_json_stracture():
    stracture = []
    for item in get_lego_json():          
            stracture.append({
                   'name': item.get('name'), 
                   'listingImages': item['listingImages'], 
                   'rating': item.get('variant').get('attributes').get('rating'), 
                   'ageRange': item.get('variant').get('attributes').get('ageRange'), 
                   'pieceCount': item.get('variant').get('attributes').get('pieceCount'), 
                   'formattedAmount': item.get('variant').get('price').get("formattedAmount")
            })

    return stracture