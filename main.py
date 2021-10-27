from re import A
from selenium import webdriver
import requests
import time
import os
# def seleniumDemo():
#     #initializing selenium object to use Chrome
#     driver = webdriver.Chrome(executable_path=r'../resources/chromedriver.exe')
#     #navigating to the link I want
#     driver.get(grantsInitialLink)

#     #some setup that is complicated, rarely needed and not worth explaining
#     iframe = driver.find_element_by_css_selector('iframe#embeddedIframe')
#     driver.switch_to.frame(iframe)
#     time.sleep(3)
    
#     #finding the grant links
#     grantLinks = driver.find_elements_by_css_selector('a[title=\"Click to View Grant Opportunity\"')
#     time.sleep(2)

#     #clicking on the first grant link
#     grantLinks[0].click()

#     #holding the program until I press a key
#     input()
# def BSEbayDemo():
#     from bs4 import BeautifulSoup
#     ebayHtml = getHtml(ebayInitialLink)
#     soup = BeautifulSoup(ebayHtml, 'html.parser')
#     titleH1 = soup.find(id='itemTitle')
#     # titleSpan = titleH1.find('span')
#     print(titleH1.text)
#     # print(soup)
#     # element = soup.find(id='productTitle')
#     # print(element.text)

#for selenium
grantsInitialLink = r'https://www.grants.gov/web/grants/search-grants.html'

#for Beautiful Soup
# amazonInitialLink = r'https://www.amazon.com/s?k=childrens+books&crid=3IY6MOTBY8RZ4&sprefix=childrens+book%2Caps%2C94&ref=nb_sb_noss'
# amazonInitialLink = r'https://www.amazon.com/Notebook-Halloween-Thanksgiving-Christmas-Journal_6in/dp/B09HQ9CFDG/ref=sr_1_1_sspa?crid=3IY6MOTBY8RZ4&dchild=1&keywords=childrens+books&qid=1635252669&sprefix=childrens+book%2Caps%2C94&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE4RjdCTFVIQ0c3VUsmZW5jcnlwdGVkSWQ9QTA4Nzk3MDgzNU5OMzIxNVBXVVUzJmVuY3J5cHRlZEFkSWQ9QTA0MDM3ODE4SzQ1NERSWDNOM1Ymd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
ebayInitialLink = r'https://www.ebay.com/itm/265320344549?_trkparms=ispr%3D5&hash=item3dc6532be5:g:BWkAAOSwqI9hRw3e&amdata=enc%3AAQAGAAACcPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsStdebXPz4ZTXCT8FI9kPBh4Z3gvXXHchuSqokLIEVOttPn50Mc4JY0oP3PWpQ82lcfyealivrlKcmk6MkH4sa7CAJzFaqLs%252BeFX4DwlNNLqZmdyrzto7NCM8VlI83X03M1ye%252Fm10yD4qSFNLpZMLsDUfaq8K0v5HgHDkppuuq171GhhnB8SMW2xkcMMwZ7kQa4A9QgM0CXCjNHeOlNeSl41rNuXxW%252Fm3YLlaOGCynnymnNH8gHkBrZVvS2RmzgzOD1Fb6jqz54yqkHe5DHIYbvF1SYBmfDv7e41EauEYUxwaQbENpXsiVLx8pPt9BraNh114ryKvIy9ftS14ZI%252Fhf0G9E9r39oBnuWikQcL82ReNhAL4pj1Ut2RIs2ab5vFcNMt8sjZUsjEe2RBYnAhudoqvxFxnZGP4lbB6Chtz2rZKsHaWrh4VbfTCuik02ok4VDFyEdCDlBFITJduapo9Mt8232V%252FWTQrs0eLhXPXb49yCDGw0LSUFyySDZimKR5%252FMNQei3%252FIltVKHNlht6umsuRJjdib4s1c7OeM8WgdsCgV5%252FKYq9OE1orZCQCkDpta3i%252BnDp7qDROuxufbeqg4aUtO9DJJ0GnMqAHNy2cD%252BFCrT7i5wIWEDruQrK1DUmCpqRGRFmz%252BDzdd16rDPzJyc041c4pwx1lwsU7D9IAD5hsDI0bgiw%252FxoeyvcO4C5Jyv3qjE824eQsGegr6mCZq70nNewAG%252FmXdKlWFqJwy%252Fl85ksQBhuBazgnCStkVurielvEAJBmecdm5Bn1o9lfN6ChA%253D%253D%7Cclp%3A2334524%7Ctkp%3ABlBMUP6DmtKXXw'
companiesInitialLink = r'https://www.environmental-expert.com/companies/location-africa'

def getHtml(initialLink:str):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    # }
    response = requests.get(initialLink)
    print('Getting HTML Data...')
    # print(response.headers)
    response.raise_for_status()
    return response.content

def getXml(filePath:str):
    filePath = os.path.realpath(filePath)
    with open(filePath) as f:
        xml = f.read()
    return xml

def BSCompaniesDemo():
    from bs4 import BeautifulSoup

    #getting the html from the companies link
    companiesHtml = getHtml(companiesInitialLink)

    #loading the raw html string into a BeautifulSoup object which will help with parsing
    soup = BeautifulSoup(companiesHtml, 'html.parser')

    #finding an element in the html
    companiesSection = soup.find('section', class_='product-list')
    companiesList = companiesSection.find('ul', class_='list-unstyled')
    companiesElements = companiesList.find_all('h2', class_='h2 m-b-0')

    for element in companiesElements:
        link = element.find('a')['href']
        print(link)

        # elementHtml = getHtml(link)
        # elementSoup = BeautifulSoup(elementHtml, 'html.parser')
        # description = elementSoup.find('p', itemprop='description').text
        # print(description)
        # break



def BSXmlDemo():
    from bs4 import BeautifulSoup
    #getting the xml data from a file
    testXml = getXml('../resources/demo.xml')
    #loading the xml into a Beautiful Soup object for parsing (notice the second argument this time)
    soup = BeautifulSoup(testXml, 'xml')

    signature = soup.find('signature')
    print(signature.text)


if __name__=='__main__':
    BSCompaniesDemo()
    # BSXmlDemo()