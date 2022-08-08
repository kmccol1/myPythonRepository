import requests
from bs4 import BeautifulSoup

#********************************************************************************************

def strain_scraper():
    page_url = "https://www.leafly.com/dispensary-info/the-releaf-center---bentonville/menu"
    html = requests.get(page_url).text
    soup = BeautifulSoup(html,'html.parser')
    targetStrain = soup.find(id="clamped-content-product-id-1248798990")

    strainItems = targetStrain.find_all(class_="clamp-lines col-start-1 mb-2 font-medium leading-6 product-card-name text-normal md:mb-4 md:col-start-2")

    halfOz = strainItems[0]

    print('Done.')

#********************************************************************************************

def main ( ):
    print('Scraping..')
    strain_scraper()
    print('Done.') 

#********************************************************************************************

if __name__ == '__main__':
    main()