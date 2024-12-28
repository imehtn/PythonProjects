#automated login to github (can be modified for other sites)

#using selenium and chrome driver
from selenium import webdriver
import os 
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#starts the bot's login process
def startBot(username, password, url):
    #path to chromedriver executable 
    path = "C:\\Users\\ingri\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    
    service = Service(path)
    chrome_options = Options()
    
    #start in maximized window
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=service,options=chrome_options)

    print("Opening the login page...")
    driver.get(url)
    print("Filling in the username...")
    driver.find_element(By.ID,"login_field").send_keys(username)
    print("Filling in the password...")
    driver.find_element(By.ID,"password").send_keys(password)
    print("Clicking the login button...")
    driver.find_element(By.NAME,"commit").click()
    print("Login process initiated...")
    time.sleep(5)

    #program ends 
    driver.quit()

#Enter login credentials and the URL of the login parameters
username="" #enter username
password="" #enter password
url = "https://github.com/login"

startBot(username,password,url) #call bot using credentials
