from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



TEST_USERNAME = "adel_test_01"
TEST_PASSWORD = "12345678"
TEST_PHONE = "0501234567"
TEST_ADDRESS = "Istanbul Turkey"
TEST_EMAIL = "adel@test.com"


driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install())
)

driver.maximize_window()

wait = WebDriverWait(driver, 15)

try:



    driver.get("http://localhost:3000/")

    print("Home page opened")

    signup_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(text(),"Sign Up")]')
        )
    )

    signup_button.click()

    print("Sign Up button clicked")

    wait.until(
        EC.url_contains("mode=signup")
    )

    print("Signup page loaded")


    username_input = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, '//input[@placeholder="Username"]')
        )
    )

    password_input = driver.find_element(
        By.XPATH,
        '//input[@placeholder="Password"]'
    )

    email_input = driver.find_element(
        By.XPATH,
        '//input[contains(@placeholder,"Email")]'
    )

    phone_input = driver.find_element(
        By.XPATH,
        '//input[contains(@placeholder,"Phone Number")]'
    )

    address_input = driver.find_element(
        By.XPATH,
        '//textarea[@placeholder="Address"]'
    )

    print("All form inputs found")



    username_input.send_keys(TEST_USERNAME)

    password_input.send_keys(TEST_PASSWORD)

    email_input.send_keys(TEST_EMAIL)

    phone_input.send_keys(TEST_PHONE)

    address_input.send_keys(TEST_ADDRESS)

    print("Form filled successfully")

    submit_button = driver.find_element(
        By.XPATH,
        '//button[@type="submit"]'
    )

    submit_button.click()

    print("Submit button clicked")

    

    time.sleep(5)


    current_url = driver.current_url
    page_source = driver.page_source.lower()

    print("Current URL:", current_url)

    # Successful registration checks
    if (
        current_url == "http://localhost:3000/"
        or "welcome back" in page_source
        or TEST_USERNAME.lower() in page_source
    ):
        print("TC-FUNC-001 PASSED")

    else:
        print("TC-FUNC-001 FAILED")

except Exception as e:

    print("TEST FAILED")
    print(type(e).__name__)
    print(e)

finally:

    time.sleep(3)
    driver.quit()