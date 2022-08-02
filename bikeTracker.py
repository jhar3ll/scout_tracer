import bs4
import time

from datetime import datetime
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from tweetLogic import sendDM, sendTweet
#from notification import sendNotification

service = Service('C:\\Users\\kapti\\.vscode\Workspace\\building\\FE_Tracker\\chromedriver.exe')
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--start-maximized")
options.add_argument("--user-data-dir=C:\\Users\\kapti\\PycharmProjects\\lbt\\pd3070")

status = True
url = "https://www.polaris.com/en-us/account/orders/details/?orderId=375036"
driver = webdriver.Chrome(service=service, options=options)
driver.get(url)
html = driver.page_source
soup = bs4.BeautifulSoup(html, "html.parser")
bikeStatuses = soup.find_all("li", {"class": "progress-bar-status__list-item"})
currentPhase = "Scheduled"

def getStatus():
    global newPhase
    for s in bikeStatuses:
        if s.get("data-status-active") == 'True':
            currentStatus = s 
    newPhase = currentStatus.find("div").getText()

def getTime():
    global timestamp
    date = datetime.now(timezone('US/Central'))
    central_hour = int(date.strftime("%H"))
    if central_hour >= 12:
        time_hour = str(central_hour - 12)
        timestamp = date.strftime(time_hour + ":%M:%Spm" + " %b %d, %G")
    elif central_hour == 12:
        timestamp = date.strftime("%H:%M:%Spm" + " %b %d, %G")
    else:
        timestamp = date.strftime("%H:%M:%Sam" + " %b %d, %G")
    

while status:
    getStatus()
    getTime()
    print(f'{newPhase} at {timestamp}')
    if currentPhase != newPhase:
        sendDM(f'Your Scout Rogue build status has changed to {newPhase}!', 135039188)
    time.sleep(3600)
    driver.refresh()