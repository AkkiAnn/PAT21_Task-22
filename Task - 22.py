from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set path to ChromeDriver executable
serv_obj=Service(r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")

# New instance of Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize browser window
driver.maximize_window()

driver.implicitly_wait(6)
driver.get("https://www.instagram.com/guviofficial/")

followers = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[2]/span").text
print("followers: ", followers)

following = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[3]/span").text
print("following: ",following)

driver.quit()