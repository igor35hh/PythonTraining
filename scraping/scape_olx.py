import requests
from bs4 import BeautifulSoup

base_url = 'https://www.olx.ua/transport/legkovye-avtomobili/?page=1'

url = base_url

print(url)

yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

cars = yelp_soup.findAll('td', {'class': 'offer'})

file_path = 'scape_olx.txt'.format()

with open(file_path, 'a') as textfile:

    for car in cars:

        for_print = ''

        #print(car)
                                                            
        #titles = car.findAll('h3', {'class': 'x-large lheight20 margintop5'})
        #print(titles)
        #title1 = titles.findAll('strong')[0].text
        #print(title1)
        
        title2 = car.findAll('small', {'class': 'breadcrumb x-normal'})[0].text
        title2.replace(' ', '')
        
        #price = car.findAll('p', {'class': 'price'})
        price1 = car.findAll('strong')[0].text
        price1.replace(' ', '')
        
        price2 = car.findAll('strong')[1].text
        price2.replace(' ', '')

        for_print = title2+' '+price1+' '+price2

        for_print = u' '.join((title2, price1, price2)).encode('utf-8').strip()
        
        print(for_print)
        #page_line = "{title}\n{price1}\n{price2}\n\n".format(title=title2,price1=price1,price2 = price2)

        #try:
       
        textfile.write(for_print+'\n')
            
        #except:
        #    pass


    
