



import telebot 
import requests
from bs4 import BeautifulSoup
import csv
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
   
       
        




token = '5408692322:AAGGT9CTD7ocH3ojBtsgnWH7CwbzgfuYVAg'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    with open('kaktus.csv','w') as f:  
        write = csv.writer(f)
        write.writerow(["title","link"])
    

    main()
    i = 1
    with open('kaktus.csv','r') as f:
        for line in f:
            try:
                x = line.split(',///,')
                print(x)
                bot.send_message(message.chat.id, f"{i}. {x[0].strip()}\n{x[1].strip()}")
                i = i +1
                if i == 21:
                    break
            except:
                None

bot.polling(none_stop=True)