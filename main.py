import time
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException, ElementNotInteractableException
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


# Applying for the jobs
def makeApplication(listing):
    listing.click()
    time.sleep(1)

    # Press Easy Apply button
    try:
        driver.find_element(By.CSS_SELECTOR, '.jobs-unified-top-card__content--two-pane button.jobs-apply-button').click()
        time.sleep(1)

        # Type phone number
        try:
            global element_present
            element_present = EC.presence_of_element_located((By.CLASS_NAME, "fb-single-line-text__input"))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")
        finally:
            phone_field = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
            if phone_field.text == "":
                phone_field.send_keys(Keys.COMMAND + "a")
                time.sleep(1)
                phone_field.send_keys(Keys.BACK_SPACE)
                time.sleep(1)
                phone_field.send_keys(phone_number)
            time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'form .artdeco-button--primary').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'form .artdeco-button--primary').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '.jobs-easy-apply-content .artdeco-button--primary').click()
        time.sleep(1)

        try:
            driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss').click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__actionbar .artdeco-button--primary').click()
        except NoSuchElementException:
            print('Applied!')
            try:
                driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss').click()
            except NoSuchElementException:
                print('There was no questions')
        else:
            print('Filling out a form is required!')

    except NoSuchElementException:
        print('Already applied')
    except ElementNotInteractableException:
        print('LinkedIn application loading error')
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()
        time.sleep(2)


# Get list of available jobs
all_job_listings = driver.find_elements(By.CLASS_NAME, 'job-card-container--clickable')
print(len(all_job_listings))

for company in all_job_listings:
    makeApplication(company)
    time.sleep(1)
