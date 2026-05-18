from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = 'adilTest1'
password = 'adilTest1'
email = 'adil@fsm.stu.edu.tr'
phone = '5362698610'
address = 'IYV Istanbul Turkey'

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.maximize_window()

wait = WebDriverWait(driver,15)

try:

    driver.get("http://localhost:3000/")

    signUp_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Sign Up")]')))

    signUp_button.click()

    wait.until(EC.url_conatains("mode=signup"))

    username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]')))

    password_input = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')

    email_input = driver.find_element(By.XPATH,'//input[contains(@placeholder,"Email")]')

    phone_input = driver.find_element(By.XPATH,'//input[contains(@placeholder,"Phone Number")]')

    address_input = driver.find_element(By.XPATH,'//textarea[@placeholder="Address"]')

    #lets send the values

    username_input.send_keys(username)

    password_input.send_keys(password)

    email_input.send_keys(email)

    phone_input.send_keys(phone)

    address_input.send_keys(address)


    submit_button = driver.find_element(By.XPATH,'//button[@type="submit"]')

    submit_button.click()

    time.sleep(5)

    current_url = driver.current_url
    page_source = driver.page_source.lower() # the whole html of current page

    if(current_url == "http://localhost:3000/"or "welcome back" in page_source or username.lower() in page_source):
        print("Test PASSED")
    else:
        print("Test FAILED")

except Exception as e:
    print("Test failed")
    print(type(e).__name__)
    print(e)

finally:
    time.sleep(3)
    driver.quit()