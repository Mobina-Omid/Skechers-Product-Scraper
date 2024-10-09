import requests
from bs4 import BeautifulSoup
import pandas as pd

url_site = "https://www.skechers.de/damen/schuhe/?start=0&sz=576"
site = requests.get(url_site)

soup = BeautifulSoup(site.text, 'html.parser')

div1 = soup.find('div', {'class': 'row product-grid js-product-tile-container'})
# print(div1.text)

div2 = div1.find_all('div', {'class': 'product'})
# print(div2[0])
# print(len(div2))
# print(div2[0].find('div',{'class':'d-flex justify-content-between align-items-center c-product-tile__swatches-label-also-in'}).text)
# print(div2[0].find('div',{'class':'pdp-link c-product-tile__title__wrap'}).text)
# print(div2[0].find('span',{'class':'value'}).text)

titles = []
prices = []
colors = []

for item in range(len(div2)):
    title = div2[item].find('div', {'class': 'pdp-link c-product-tile__title__wrap'}).text.strip()
    titles.append(title.replace('\n','').replace(',',''))

    color = div2[item].find('div', {'class': 'd-flex justify-content-between align-items-center c-product-tile__swatches-label-also-in'}).text.strip()
    colors.append(color.replace('\n','').replace(',','').replace('Farben','').replace('Farbe','').replace('                                         Auch in weit',''))

    price = div2[item].find('span',{'class':'value'}).text.strip()
    prices.append(price.replace('\n','').replace('€','').replace('Reduziert von                                        ','').replace(' auf',''))

print(titles)
print(colors)
print(prices)

myDictionary = {
    'Title':titles,
    'Price':prices,
    'Color':colors
}
df = pd.DataFrame(myDictionary)
df.to_csv('SKECHERS.csv')
df.insert(0, 'Index', range(1, len(df) + 1))
df.to_csv('SKECHERS.csv', index=False)
SkechetsDataList = pd.read_csv('SKECHERS.csv')
print(SkechetsDataList.columns)
print(SkechetsDataList.shape)
print(SkechetsDataList.head())
print(SkechetsDataList.to_string())

