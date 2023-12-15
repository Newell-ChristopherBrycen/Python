#! python3

import bs4, requests

def getDeskPrice(productURL):
    page = requests.get(productURL)
    page.raise_for_status() # did it work?
    
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    elemsCost = soup.select('#__next > div > section > main > div > div:nth-child(1) > div > div.ProductDetail_ProductDetailPage__col__UMAXq.col-xl-4.col-lg-12 > div > div.ProductInfo_PriceWrap__K6_rR > div > div > div:nth-child(1) > span')
    price = elemsCost[0].text.strip()
    return price

def getDeskName(productURL):
    page = requests.get(productURL)
    page.raise_for_status() #did it work?
    
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    elemsName = soup.select('head > title')
    name = elemsName[0].text.strip()
    return name

url = 'https://www.autonomous.ai/standing-desks/l-shaped-smartdesk'
price = getDeskPrice(url)
name = getDeskName(url)
print('The price of ' + name + ' is ' + price + '.')
