import bs4
from urllib.request import urlopen as uReq #grabs the webpage
from bs4 import BeautifulSoup as soup #passes the html url through text

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics+card'

#Opening up connection, grabbing the page
u_client = uReq(my_url)
page_html = u_client.read()
u_client.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

#grabs each product
containers = page_soup.findAll('div', {'item-container'})

filename = 'products.csv'
f = open(filename, 'w')

headers = 'Brand, Product_name, Shipping \n'

f.write(headers)

for container in containers:
    brand = container.div.div.a.img['title']

    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text

    shipping_container = container.findAll('li', {'class': 'price-ship'})
    shipping = shipping_container[0].text

    print('brand: ' + brand)
    print('product_name: ' + product_name)
    print('shipping: ' + shipping)

    f.write(brand + ',' + product_name.replace(',', '|') + shipping + '\n')

f.close()    