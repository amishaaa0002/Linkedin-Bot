from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException    #common exceptions
from selenium.common.exceptions import ElementNotInteractableException   #for not interactable objects



PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

driver.get("https://www.linkedin.com/login/")
username_in=driver.find_element(by=By.ID,value='username')
password_in=driver.find_element(by=By.ID,value='password')
username_in.send_keys(username) 
password_in.send_keys(password) #please enter your own password here
down_sign_in=driver.find_element(by=By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
down_sign_in.click()



driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH")
time.sleep(3)

all_buttons=driver.find_elements(By.TAG_NAME,value="button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();",btn)
    time.sleep(2)
    send = driver.find_element(By.XPATH,value="//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();",send)
    close_button = driver.find_element(By.XPATH,value="//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();",close_button)
    time.sleep(2)





   

