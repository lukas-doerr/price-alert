import requests
from bs4 import BeautifulSoup
import smtplib


#Chose your Link
URL = '#' #your Link 
limit = 0 #choose a pricelimit



headers = {"User-Agent": "#"} #your User-Agent

def checkPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    #checkout for the id-tag 
    price = soup.find(id="#").get_text() #the id of the Price in the sourcecode of the website
    con_price =float(price[0:3])

    #chose your dream price
    if(con_price < limit):       
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('#source Email', '#your Password')

    subject = 'Hey Price fell down!'
    body = f'Check the link -> {URL}'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        '#source Email',
        '#target Email',
        msg
    )

    print('EMAIL HAS BEEN SENT!')

    server.quit()

checkPrice()