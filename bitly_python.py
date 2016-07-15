import requests
import json

query_params = {'access_token': 'API_KEY',
                'longUrl': 'https://myignite.microsoft.com/#/videos/9438cd59-cab2-e411-b87f-00155d5066d7'} 

endpoint = 'https://api-ssl.bitly.com/v3/shorten'
response = requests.get(endpoint, params=query_params, verify=False)
data = json.loads(response.text)
print(data['data']['url'])