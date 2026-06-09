from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

url = "https://formy-project.herokuapp.com/form"
driver.get(url)
time.sleep(2)

firstName = driver.find_element(By.ID, "first-name")
lastName = driver.find_element(By.ID, "last-name")
jobTitle = driver.find_element(By.ID, "job-title")
levelOfEducation = driver.find_element(By.ID, "radio-button-2")
sex = driver.find_element(By.ID, "checkbox-1")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(1)

yearOfExperience = driver.find_element(By.XPATH, '//*[@id="select-menu"]/option[2]') 
date = driver.find_element(By.ID, "datepicker")
submitButton = driver.find_element(By.XPATH, "/html/body/div/form/div/div[8]/a")

firstName.send_keys("Phil")
time.sleep(1)

lastName.send_keys("Coulson")
time.sleep(1)

jobTitle.send_keys("Shield Agent")
time.sleep(1)

levelOfEducation.click()
time.sleep(1)

sex.click()
time.sleep(1)

yearOfExperience.click()
time.sleep(1)

date.send_keys("06/21/2026")
time.sleep(1)

submitButton.click()
time.sleep(1)

assert "thanks" in driver.current_url, "The form was not submitted!"

time.sleep(2)

driver.quit()