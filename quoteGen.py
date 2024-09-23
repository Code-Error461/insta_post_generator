import os
import json
import random
import requests



def quote():
    api = os.environ['API_KEY']
    category = ['alone', 'love', 'inspirational', 'forgiveness']
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(random.choice(category))
    response = requests.get(api_url, headers={'X-Api-Key':api})
    quote = ""
    if response.status_code == requests.codes.ok:
        quote = f'{json.loads(response.text)[0]["quote"]}\n- {json.loads(response.text)[0]["author"]}'
    else:
        quote = "💔"

    return quote
