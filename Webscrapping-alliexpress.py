import requests
import re
import BeautifulSoup
url = 'https://www.aliexpress.com/category/100003109/womenclothing.html?trafficChannel=main&catNam=women-clothing&CatId=100003109&ltype=wholesale&SortType=default&g=n'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'lxml')
clothing = soup.find('div', attrs={'class':'item-title-wrap'} ) 
title1 = clothing.text.strip()
print (name)
clothing_containers = soup.find_all('div', class_ = 'list product-card')
print(type(clothing_containers))
print(len(clothing_containers))
clothing_price = clothing_containers[8].find('span', class_ = 'price-current')
type(clothing_price)
len(clothing_price)
import pandas as pd
pages = [str(i) for i in range(1,10)]
from time import time 
from time import sleep
from random import randint
start_time = time()
requests = 0
for _ in range(5):
# A request would go here
    requests += 1
    sleep(randint(1,3))
    elapsed_time = time() - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    from IPython.core.display import clear_output
    start_time = time()
    requests = 0
    for _ in range(5):
        requests  += 1
        sleep(randint(1,3))
        current_time = time()
        elapsed_time = current_time - start_time
        print('Request:{};Frequency:{} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait=True)
#Redelcaring the lists to store data in
title = []
price  = []
rating = []
sold = []
from warnings import warn
#Preparing te mon =itoring of the loop
start_time = time()
requests = 0
#For every page in the interval 1-10
from requests import get
for page in pages:
    
    response = get('https://www.aliexpress.com/category/100003109/women-clothing.html?trafficChannel=main&catName=women-clothing&CatId=100003109&ltype=wholesale&SortType=default&page=' + page+ '&isrefine=')
    sleep(randint(8,15))
    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait = True)

        # Throw a warning for non-200 status codes
    if response.status_code != 200:
        warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Break the loop if the number of requests is greater than expected
    if requests > 500:
            warn('Number of requests was greater than expected.')
            break

        # Parse the content of the request with BeautifulSoup
    soup = bs4.BeautifulSoup(response.text, 'lxml')

        # Select all the products form a page
    clothing_containers = soup.find_all('div', class_ = 'list product-card')

        # For every product
    for container in clothing_containers:
        if container.find('span', class_= 'price-current') is not None:
            title1 = container.div.a.text
            title.append(title1)
            print(title)
            len(title)
        #price
            Price1 = container.find('span', class_ ='price-current')
            price.append(float(Price1)
            #Rating
            Rating1= container.find('span', class_='rating-value').text
            Rating.append(float(Rating1))
           
    #sold
            sold1 = container.find('span', class_ = 'sale-value').text
            sold.append(float(sold1))
           
    
Clothing = pd.DataFrame({'Title': title,
                        'Price': price,
                        'Rating' : Rating,
                        'Sold' : sold
                        })
print(Clothing.info())


