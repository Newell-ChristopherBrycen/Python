#! python3

import bs4, requests

custom_headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
'accept-language': 'en-GB,en;q=0.9',
}

def getPriceAmazon(productURL):
    page = requests.get(productURL, custom_headers)
    page.raise_for_status() # did it work?
    
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    elemsCost = soup.select('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole')
    price = elemsCost[0].text.strip()
    return price

def getPriceDre(productURL):
    page = requests.get(productURL, custom_headers)
    page.raise_for_status() # did it work?
    
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    elemsCost = soup.select('#bs3-pdp > div > div:nth-child(3) > section > div > div > div > div.experiencefragment.section > div > div > div.product-main__content > div > div.product-detail__price > span.price')
    price = elemsCost[0].text.strip()
    return price

def getPriceBestBuy(productURL):
    page = requests.get(productURL, custom_headers)
    page.raise_for_status() #did it work?
    
    soup = bs4.BeautifulSoup(page.text, "html.parser")
    elemsCost = soup.select('#pricing-price-69942782 > div > div > div > div > div > div.flex.gvpc-price-1-2343-25 > div:nth-child(1) > div:nth-child(1) > div > span:nth-child(1)')
    price = elemsCost[0].text.strip()
    return price
    

#priceAmazon = getPriceAmazon('https://www.amazon.com/Beats-Fit-Pro-Cancelling-Built/dp/B09JL41N9C?th=1')
priceDre = getPriceDre('https://www.beatsbydre.com/earbuds/beats-fit-pro/MK2F3/beats-black')
#priceBB = getPriceBestBuy('https://www.bestbuy.com/site/beats-fit-pro-true-wireless-noise-cancelling-in-ear-earbuds-black/6397391.p?skuId=6397391')
#print('The price of the Beats Fit Pro at Amazon is: ' + priceAmazon + '.')
print('The price of the Beats Fit Pro at BeatsByDre is: ' + priceDre + '.')
#print('The price of the Beats Fit Pro at BestBuy is: ' + priceBB + '.')
