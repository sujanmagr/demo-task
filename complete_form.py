import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
url="https://formy-project.herokuapp.com/form"
driver.maximize_window()
driver.get(url)
time.sleep(3)
# driver.implicitly_wait(10)
first_name=driver.find_element(By.ID,"first-name")
last_name=driver.find_element(By.ID,"last-name")
job_title=driver.find_element(By.ID,"job-title")
education_level=driver.find_element(By.ID ,"radio-button-2")

gender=driver.find_element(By.ID,"checkbox-1")

experience=driver.find_element(By.ID,"select-menu")

date=driver.find_element(By.ID,"datepicker")

first_name.send_keys("John")
time.sleep(1)
last_name.send_keys("Smith")
time.sleep(1)
job_title.send_keys("QA Engineer")
time.sleep(1)
education_level.click()
time.sleep(1)
gender.click()
time.sleep(1)
experience = Select(driver.find_element(By.ID, "select-menu"))
experience.select_by_index(2)
time.sleep(1)
date.send_keys("05/16/2026")
time.sleep(2)
submit=driver.find_element(By.CSS_SELECTOR,"body > div > form > div > div:nth-child(15) > a")
submit.click()
time.sleep(2)
driver.quit()