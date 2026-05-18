from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# =====================================
# TEST DATA
# =====================================

TEST_USERNAME = "adel_test_01"
TEST_PASSWORD = "12345678"
TEST_PHONE = "0501234567"
TEST_ADDRESS = "Istanbul Turkey"
TEST_EMAIL = "adel@test.com"

# =====================================
# START CHROME
# =====================================

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.maximize_window()

wait = WebDriverWait(driver, 15)

try:

    # =====================================
    # OPEN HOME PAGE
    # =====================================

    driver.get("http://localhost:3000/")

    print("Home page opened")

    # =====================================
    # CLICK SIGN UP BUTTON
    # =====================================

    signup_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(text(),"Sign Up")]')
        )
    )

    signup_button.click()

    print("Sign Up button clicked")

    # =====================================
    # VERIFY SIGNUP PAGE
    # =====================================

    wait.until(
        EC.url_contains("mode=signup")
    )

    print("Signup page loaded")

    # =====================================
    # FIND FORM INPUTS
    # =====================================

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

    # =====================================
    # FILL FORM
    # =====================================

    username_input.send_keys(TEST_USERNAME)

    password_input.send_keys(TEST_PASSWORD)

    email_input.send_keys(TEST_EMAIL)

    phone_input.send_keys(TEST_PHONE)

    address_input.send_keys(TEST_ADDRESS)

    print("Form filled successfully")

    # =====================================
    # CLICK SUBMIT
    # =====================================

    submit_button = driver.find_element(
        By.XPATH,
        '//button[@type="submit"]'
    )

    submit_button.click()

    print("Submit button clicked")

    # =====================================
    # WAIT AFTER SUBMIT
    # =====================================

    time.sleep(5)

    # =====================================
    # VALIDATION
    # =====================================

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