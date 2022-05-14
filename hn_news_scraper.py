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

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# lets send the email
print('Composing Email...')

# update your email details
SERVER = 'smtp.gmail.com' # "your smtp server"
PORT = 597 # your port number
FROM = '' # "your email id"
TO = '' # "your to email ids" # can be a list of email ids
PASS = '' # "your email ids password"

# fp = open(file_name, 'rb')

# Create a text/plain message 
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition', 'attachment; filename='empty.txt')
msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
# fp.close()

print('Initializing Server...')

server = smtplib.SMTP(SERVER, PORT)
# server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
# server.ehlo
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')

server.quit()





