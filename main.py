import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.safari.service import Service
from selenium.webdriver.support.wait import WebDriverWait

# User data
linkedin_username = input("Enter your linkedin username: ")
linkedin_password = input("Enter your linkedin password: ")
job_name = input("Enter job title/skill/name: ")
job_location = input("Enter job location: ")
phone_number = input("Enter your phone number: ")

# Initialising web driver
WEBDRIVER_PATH = "/usr/bin/safaridriver"
web_driver_service = Service(executable_path=WEBDRIVER_PATH)
driver = webdriver.Safari(service=web_driver_service)
driver.maximize_window()
JOB_SEARCH_URL = 'https://www.linkedin.com/jobs/search/'
driver.get(JOB_SEARCH_URL)

timeout = 5

# Sign in button
try:
    element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/header/nav/div/a[2]'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    sign_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
    sign_in_button.click()

# Username and password fields
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    username_box = driver.find_element(By.XPATH, '//*[@id="username"]')
    password_box = driver.find_element(By.XPATH, '//*[@id="password"]')
    username_box.click()
    username_box.send_keys(linkedin_username)
    password_box.click()
    password_box.send_keys(linkedin_password)
    password_box.send_keys(Keys.RETURN)


# Job name field
try:
    element_present = EC.presence_of_element_located((By.ID, 'jobs-search-box-keyword-id-ember24'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    name_search = driver.find_element(By.ID, 'jobs-search-box-keyword-id-ember24')
    time.sleep(3)
    name_search.send_keys(job_name)
    time.sleep(3)
    name_search.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    name_search.send_keys(Keys.RETURN)
    time.sleep(2)

# Job location field
try:
    element_present = EC.presence_of_element_located((By.ID, 'jobs-search-box-location-id-ember24'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    location_search = driver.find_element(By.ID, 'jobs-search-box-location-id-ember24')
    location_search.send_keys(Keys.COMMAND + "a")
    time.sleep(1)
    location_search.send_keys(Keys.BACK_SPACE)
    time.sleep(2)
    location_search.send_keys(job_location)
    time.sleep(3)
    location_search.send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    location_search.send_keys(Keys.RETURN)

# Apply Easy Apply filter
try:
    element_present = EC.presence_of_element_located((By.XPATH, "//button[text()= 'Easy Apply']"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    easy_to_apply_filter = driver.find_element(By.XPATH, "//button[text()= 'Easy Apply']")
    easy_to_apply_filter.click()
    time.sleep(3)

# Press Easy Apply
try:
    element_present = EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".jobs-apply-button--top-card .jobs-apply-button"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card .jobs-apply-button")
    easy_apply.click()
    time.sleep(2)

# Type phone number
try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, "fb-single-line-text__input"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    phone_field = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
    if phone_field.text == "":
        phone_field.send_keys(phone_number)
    time.sleep(1)

# Submit application
try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, "footer button"))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    submit = driver.find_element(By.CSS_SELECTOR, "footer button")
    submit.click()
