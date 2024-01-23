import requests

def get_courses(url):
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'caeaf258-9e3c-4301-872a-6c164d8dca6e',        
    }
    full_page = requests.get(url, headers=headers)

    return str(full_page.content)

request_file = open('request.json', 'w')
request_file.write(get_courses("https://pro-api.coinmarketcap.com/v2/tools/price-conversion?amount=1&id=1"))
