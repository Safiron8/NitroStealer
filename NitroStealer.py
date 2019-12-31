import requests, time, exrex, os, json
from bs4 import BeautifulSoup
from random import choice

def random_nitro():
    regex = exrex.getone('^[A-Za-z0-9]{16}$')
    return regex

class Response:
    response_list = []

    def __init__(self):
        if os.path.exists('./responses.json'):
            self.load()
        else:
            self.save()

    def save(self):
        responses = {
            'response_list': self.response_list
        }

        with open('responses.json', 'w') as f:
            json.dump(responses, f, indent=4)

    def load(self):
        with open('responses.json', 'r') as f:
            responses = json.load(f)
            self.response_list = responses['response_list']

Response = Response()

nalez = False

for r in Response.response_list:
    if int(r['code']) != 10038:
        print(r)
        nalez = True

if not nalez:
    print("V předchozích odpovědích nebyly nalezeny žádné nitra")

while True:
    code = random_nitro()
    url = "https://discordapp.com/api/v6/entitlements/gift-codes/{}?with_application=true&with_subscription_plan=true".format(code)
    response = requests.request('get', url)
    response_json = response.json()

    r = {
        'url': url,
        'url_code': code,
        'code': response_json['code'],
        'message': response_json['message']
    }

    Response.response_list.append(r)

    print(code)

    Response.save()

    time.sleep(5)