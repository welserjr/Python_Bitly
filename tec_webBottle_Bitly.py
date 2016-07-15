import bottle
import urllib
from bs4 import BeautifulSoup
import json
import requests


@bottle.route('/')
def home_page():
    url = urllib.request.urlopen("http://www.tec.com.pe")
    html = BeautifulSoup(url)

    api_key = "API_KEY"
    query_params = {'access_token': api_key}
    endpoint = 'https://api-ssl.bitly.com/v3/shorten'

    array_img = []
    array_data = []
    for item in html.body.find_all("article", "omc-blog-two omc-half-width-category"):
        div1 = item.find_all("div", "omc-resize-290 omc-blog")
        for i in div1:
            imagen = i.img['src']
            array_img.append(imagen)

        div2 = item.find_all("div", "omc-blog-two-text")
        for i in div2:
            titulo = i.h2.a.string
            link = i.h2.a['href']
            query_params['longUrl'] = link
            response = requests.get(endpoint, params=query_params, verify=False)
            data = json.loads(response.text)
            link_short = data['data']['url']
            aut = i.p.em.string
            author = aut.replace("by ", "")
            a = {"titulo": titulo, "link": link_short, "author": author}
            array_data.append(a)

    aux = 0
    for item in array_data:
        item['imagen'] = array_img[aux]
        aux += 1

    data = json.dumps(array_data)
    return bottle.template(data)


bottle.debug(False)
bottle.run(host='0.0.0.0', port=2020)
