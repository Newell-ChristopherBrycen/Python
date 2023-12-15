from selenium import webdriver

PATH = "C:\SeleniumDriver\chromedriver.exe"
browser = webdriver.Chrome(PATH)
browser.get('https://automatetheboringstuff.com/')

elem = browser.find_elements_by_css_selector('.main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(19) > a:nth-child(1)')
elem.click()
