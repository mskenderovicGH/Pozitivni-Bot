import time
import re
import requests
from mechanize import Browser
from bs4 import BeautifulSoup

br = Browser()

br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

response=br.open("https://www.klix.ba/prijava")

time.sleep(10.0)

for f in br.forms():
    if f.attrs['class'] == 'space-y-6':
        br.form = f
text = br.form.find_control(id="username")
text.value = "BotBotinski12"
text = br.form.find_control(id="password")
text.value = "lozinka123"
br.submit()

  
URL = "https://www.klix.ba/"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

r = requests.get(URL,headers=header)

  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
for link in soup.find_all(href=re.compile("scitech")):
    print(link.get('href'))
    try:
        response=br.open(link.get('href'))

        time.sleep(5.0)

        for f in br.forms():
            if f.attrs['id'] == 'samokomentar':
                br.form = f
        text = br.form.find_control(id="komentarinput")
        text.value = "Bosna i Hercegovina je najbolje mjesto za život."
        br.submit()
        print("komentar je ostavljen")
    except:
        print("komentari nisu dostupni")


