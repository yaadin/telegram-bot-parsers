import requests
from bs4 import BeautifulSoup
import csv

def request(url):
    html = requests.get(url)
    return html.text

def data(html):
    soup = BeautifulSoup(html,"lxml")
    product = soup.find_all('div', class_="row")
    for i in product:
        try:
            title = i.find('span', class_='prouct_name').text.strip()
       
            
            price = i.find("span", class_="price").text.strip()
           
            
            img = 'https://enter.kg' + i.find('img').get('src')
           
        except:
            None
      
        

        dict_ = {'title':title, "price":price, "image": img}
        write_to_csv(dict_)
        
def write_to_csv(database):
    with open('enter.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([database['title'],database['price'],database['image']])

def last_page(html):
    soup = BeautifulSoup(html,'lxml')
    last = soup.find("span", class_="vm-page-counter").text
    x = last.split(' ')
    lastlast = int(x[-1])
    return lastlast
    
def main():
    url = "https://enter.kg/computers/noutbuki_bishkek"
    html = request(url)
    data(html)
    i = 1
    number = last_page(html)
    print(number)
    for i in range(1,number):
            url_new= f'{url}/results,{i}01-{i}00'
            html_new = request(url_new)
            data(html_new)
       
        


with open('enter.csv','w') as f:  
    write = csv.writer(f)
    write.writerow(["product","price","image",])
    

main()