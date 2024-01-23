import aiohttp
import asyncio

async def scrapping_bitcoin(url, headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            await response.text()

def main():
    url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion?amount=1&id=1'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'caeaf258-9e3c-4301-872a-6c164d8dca6e',   
    }
    asyncio.run(scrapping_bitcoin(url, headers))
    response_file = open('response_file.json', 'w')
    response_file.write()

main()
