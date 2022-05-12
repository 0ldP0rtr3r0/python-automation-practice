import requests # http requests
import smtplib # send the mail 
import datetime # system date and time manipulation

from bs4 import BeautifulSoup # web scraping

# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now = datetime.datetime.now()

# email content placeholder
content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(URL)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    
    # use web inspector to identify how to prepare your soup
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text!='More' else '')
        #print(tag.prettify) #find all('span'.attrs={'class':'sitestr'}))
        return(cnt)

    