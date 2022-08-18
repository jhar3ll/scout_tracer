from turtle import goto
import bs4
import time
from datetime import datetime
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tweetLogic import sendDM

def initiate():
    global driver
    global soup
    service = Service('C:\\Users\\kapti\\.vscode\Workspace\\building\\FE_Tracker\\chromedriver.exe')
    options = Options()
    option_args = ['--no-sandbox','--disable-dev-shm-usage','--disable-gpu',"--start-maximized","--user-data-dir=C:\\Users\\kapti\\PycharmProjects\\lbt\\pd3070"]
    for arg in option_args:
        options.add_argument(arg)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.polaris.com/en-us/account/orders/details/?orderId=375036")
    soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
    
def getStatus():
    bikeStatuses = soup.find_all("li", {"class": "progress-bar-status__list-item"})
   
    for i in bikeStatuses:
        if i.get("data-status-active") == 'True':
            currentBikeStatus = i.find("div").getText()
    return currentBikeStatus

def getShipDate():
    bikeDetails = soup.find("div", {"class": "wholegoods-orders-details__app-order-status-progress"}).find_all("div")
    shipDate = bikeDetails[1].getText()
    return shipDate

def getTime():
    date = datetime.now(timezone('US/Central'))
    central_hour = int(date.strftime("%H"))
    if central_hour > 12:
        time_hour = str(central_hour - 12)
        timestamp = date.strftime(time_hour + ":%M:%Spm" + " %b %d, %G")
    elif central_hour == 12:
        timestamp = date.strftime("%H:%M:%Spm" + " %b %d, %G")
    else:
        timestamp = date.strftime("%H:%M:%Sam" + " %b %d, %G")
    return timestamp

def runTracker():
    initiate()
    status = True
    lastPhase = "Scheduled"
    lastDate = "Ship Date: 08/16/2022 - 08/31/2022"
    while status:
        currentStatus = getStatus()
        currentDate = getShipDate()
        print(f'{currentStatus} at {getTime()}. {currentDate}')

        if currentStatus != lastPhase:
            sendDM(f'Your Scout Rogue build status has changed to {currentStatus}!', 135039188)
        elif currentDate != lastDate:
            sendDM(f'Your Scout Rogue ship date has changed to {currentDate}!', 135039188)
        time.sleep(3600)
        driver.refresh()

runTracker()