import bs4
import requests

#customer headers needed to allow for use with Amazon web services. Without these headers, get() returns an error 500
custom_headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 
'accept-language': 'en-GB,en;q=0.9',
}
url = 'http://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922'
page = requests.get(url, headers = custom_headers)


soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('#corePrice_feature_div > div > div > span.a-price.a-text-price.header-price.a-size-base.a-text-normal > span:nth-child(2)')
print(elems[0].text.strip())
