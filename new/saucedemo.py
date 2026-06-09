from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


####### Question to Ask ?? ########
# 1. How can we do mouse movement so that we can know which button is being pressed, if yes then can we not integrate in one line,  for example in line 30 with 'action'.

# 2. Can we not do this instead of writing code for each button 
# addToCart = wait.until(EC.element_to_be_clickable((By.NAME, "Add to cart"))).click()


driver = webdriver.Edge()
driver.maximize_window()

url = "https://www.saucedemo.com/"
driver.get(url)
time.sleep(2)

wait = WebDriverWait(driver,10)
action = ActionChains(driver)

username = driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
password = driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
loginButton = wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
time.sleep(3)

# addToCart = wait.until(EC.element_to_be_clickable((By.NAME, "Add to cart"))).click()
# time.sleep(2)

addBackpack = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
time.sleep(1)

addBikelight = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()
time.sleep(1)

addTshirt = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
time.sleep(1)

addJacket = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))).click()
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

addOnesie = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()
time.sleep(1)

addRedTshirt = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
time.sleep(1)


driver.execute_script("window.scrollTo(0,0)")
time.sleep(1)

cartButton = wait.until(EC.element_to_be_clickable((By.ID, "shopping_cart_container"))).click()
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

checkoutButton = wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
time.sleep(2)

driver.execute_script("window.scrollTo(0,0)")
time.sleep(2)

firstName = driver.find_element(By.ID, "first-name").send_keys("Bruce")
time.sleep(1)

lastName = driver.find_element(By.ID, "last-name").send_keys("Banner")
time.sleep(1)

postalCode = driver.find_element(By.ID, "postal-code").send_keys("44600")
time.sleep(2)

continueButton = wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

finishButton = wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
time.sleep(3)

assert "checkout-complete.html" in driver.current_url, "Error Occurred during Checkout!!"

backToHome = wait.until(EC.element_to_be_clickable((By.ID, "back-to-products"))).click()
time.sleep(2)

driver.quit()