import requests
from bs4 import BeautifulSoup
import csv

# def request(url):
#     html = requests.get(url)
#     return html.text

# def data(html):
#     soup = BeautifulSoup(html,"lxml")
#     product = soup.find_all('div', class_="list-item list-label")
#     for i in product:
#         try:
#             title = i.find('h2', class_='name').text.strip()
              
            
#             price = i.find("div", class_="block price").find('strong').text.strip()
           
            
#             descr = i.find("p",class_='year-miles').text.strip() + ' ' + i.find("p",class_='body-type').text.strip()+ ' ' + i.find("p",class_='volume').text.strip()
           
            
#             img = i.find('img').get('data-src')
         
           
#         except:
#             None
      
        

#         dict_ = {'title':title, "price":price, "image": img,'description':descr}
#         write_to_csv(dict_)
        
# def write_to_csv(database):
#     with open('mashina.csv', 'a+') as file:
#         writer = csv.writer(file)
#         writer.writerow([database['title'],database['price'],database['image'],database['description']])

# # def last_page(html):
# #     soup = BeautifulSoup(html,'lxml')
# #     last = soup.find("span", class_="vm-page-counter").text
# #     x = last.split(' ')
# #     lastlast = int(x[-1])
# #     return lastlast
    
# def main():
#     url = "https://www.mashina.kg/search/?currency=2&price_from=&price_to="
#     html = request(url)
#     data(html)
#     # i = 1
#     # number = last_page(html)
#     # print(number)
#     lastpage = 1201
#     page = 2
#     while True:
#             url_new= f'{url}+&page={page}'
#             html_new = request(url_new)
#             data(html_new)
#             page = page +1 
       
        


# with open('mashina.csv','w') as f:  
#     write = csv.writer(f)
#     write.writerow(["product","price","image",'description'])
    

# main()













def request(url):
    html = requests.get(url)
    return html.text

def data(html):
    soup = BeautifulSoup(html,"lxml")
    product = soup.find_all('div', class_="ArticleItem")
    for i in product:
        try:
            title = i.find('a', class_="ArticleItem--name").text.strip()

            link = i.find("a", class_="ArticleItem--image").get('href')
    
           
        except:
            None
      
        

        dict_ = {'title':title,'sep':'///', 'link':link}
        write_to_csv(dict_)
        
def write_to_csv(database):
    with open('kaktus.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([database['title'],database["sep"],database['link']])


    
def main():
    url = "https://kaktus.media/?lable=8&date=2022-11-23&order=time"
    html = request(url)
    data(html)
   
       
        


with open('kaktus.csv','w') as f:  
    write = csv.writer(f)
    write.writerow([])
    

main()

with open('kaktus.csv','r') as f:
        for line in f:
            x = line.split(',///,')
            # print(x[0])
            print(len(x))