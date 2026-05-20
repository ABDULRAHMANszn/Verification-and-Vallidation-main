
# Covers: Signup, Signin, Meals, Cart, Orders, Business Rules Performance, Security, Usability / UX
# Target: http://localhost:3000   |   Backend: http://localhost:8000

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import requests

# Driver setup  (shared across every section below)
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()

BASE_URL = "http://localhost:3000"

# Helper utilities

def open_signup():
    """Click the Sign-Up link from the home page to open the signup form."""
    sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
    driver.execute_script("arguments[0].click();", sign_up_btn)


def clear_local_storage():
    """Wipe localStorage to reset auth / cart state between tests."""
    driver.execute_script("window.localStorage.clear();")


# SECTION 1 — SIGNUP / REGISTRATION

# TC-FUNC-002  |  Register with existing username  
# sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
# driver.execute_script("arguments[0].click();", sign_up_btn)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "email").send_keys("sass@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("1234567890")
# driver.find_element(By.ID, "address").send_keys("123 Main St")
# driver.find_element(By.ID, "register-btn").click()
# assert "/login" in driver.current_url
# print("TC-FUNC-002 PASSED - Duplicate username rejected")
# clear_local_storage()
# driver.quit()

# TC-FUNC-001  |  Registration without optional email  
# driver.get(f"{BASE_URL}/login?mode=signup")
# driver.find_element(By.ID, "username").send_keys("sami4")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "email").send_keys("")
# driver.find_element(By.ID, "phone").send_keys("1234567890")
# driver.find_element(By.ID, "address").send_keys("123 Main St")
# driver.find_element(By.ID, "register-btn").click()
# assert "/signup" not in driver.current_url
# print("TC-FUNC-001 PASSED - Registration without optional email accepted")
# clear_local_storage()
# driver.quit()

# TC-FUNC-000  |  Registration with empty password  
# driver.get(f"{BASE_URL}/login?mode=signup")
# driver.find_element(By.ID, "username").send_keys("sami5")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.ID, "email").send_keys("aaaa@gmail.com")
# driver.find_element(By.ID, "phone").send_keys("1234567890")
# driver.find_element(By.ID, "address").send_keys("123 Main St")
# driver.find_element(By.ID, "register-btn").click()
# assert "signup" in driver.current_url
# print("TC-FUNC-000 PASSED - Registration with empty password rejected")
# driver.quit()


# Login link navigates to Login page  
# driver.get(f"{BASE_URL}/")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(2)
# assert "/login" in driver.current_url
# print("TC-FUNC-000 PASSED - Login link navigates to login page")

# TC-003  |  Registration with empty username  (File 4)
# try:
#     driver.get(f"{BASE_URL}/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)
#     driver.find_element(By.ID, "username").send_keys("")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("123456789")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()
#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-003 PASSED - Username with empty username accepted")
# except AssertionError:
#     print("TC-003 FAILED - Username with less than 3 chars was accepted")
# driver.quit()


# TC-003  |  Registration with empty phone  (File 4)
# try:
#     driver.get(f"{BASE_URL}/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)
#     driver.find_element(By.ID, "username").send_keys("ibrahim")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()
#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-003 PASSED - Registration with empty phone accepted")
# except AssertionError:
#     print("TC-003 FAILED - Registration with empty phone was rejected (unexpected)")
# driver.quit()

# TC-003  |  Registration with empty address  (File 4)
# try:
#     driver.get(f"{BASE_URL}/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)
#     driver.find_element(By.ID, "username").send_keys("mustafa")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("123456789")
#     driver.find_element(By.ID, "address").send_keys("")
#     driver.find_element(By.ID, "register-btn").click()
#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-003 PASSED - Registration with empty address accepted")
# except AssertionError:
#     print("TC-003 FAILED - Registration with empty address was rejected (unexpected)")
# driver.quit()

# TC-003  |  Username with fewer than 3 characters  (File 4)
# try:
#     open_signup()
#     driver.find_element(By.ID, "username").send_keys("aa")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("123456789")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()
#     assert "/login" not in driver.current_url
#     print("TC-003 PASSED - Username with less than 3 chars rejected")
# except AssertionError:
#     print("TC-003 FAILED - Username with less than 3 chars was accepted")
# driver.quit()

# TC-004  |  Empty password at registration  (File 4)
# try:
#     open_signup()
#     driver.find_element(By.ID, "username").send_keys("muhammed")
#     driver.find_element(By.ID, "password").send_keys("")
#     driver.find_element(By.ID, "email").send_keys("sass4@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("123456789")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()
#     assert "/login" not in driver.current_url
#     print("TC-004 PASSED - Empty password rejected")
# except AssertionError:
#     print("TC-004 FAILED - Empty password was accepted")
# driver.quit()

# TC-005  |  Empty phone at registration  (File 4)
# try:
#     open_signup()
#     driver.find_element(By.ID, "username").send_keys("muhammed5")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass5@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()
#     assert "/login" not in driver.current_url
#     print("TC-005 PASSED - Empty phone rejected")
# except AssertionError:
#     print("TC-005 FAILED - Empty phone was accepted")
# driver.quit()

# TC-006  |  Special characters in username  (File 4)
# try:
#     open_signup()
#     driver.find_element(By.ID, "username").send_keys("mohamed$2026!")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass6@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("5012345678")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()
#     assert "/login" not in driver.current_url
#     print("TC-006 PASSED - Special characters handled (check validation rules)")
# except AssertionError:
#     print("TC-006 FAILED - username contains special character")






# BR-008  |  Password minimum length (min 6 characters)  
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("testbr008")
# driver.find_element(By.ID, "password").send_keys("ab1")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("Test Address 123")
# register_btn = driver.find_element(By.ID, "register-btn")
# driver.execute_script("arguments[0].click();", register_btn)
# time.sleep(2)
# assert "mode=signup" in driver.current_url
# print("BR-008 PASSED - Short password rejected")
# clear_local_storage()
# driver.quit()

# BR-009  |  Phone number must be digits only  
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("testbr009")
# driver.find_element(By.ID, "password").send_keys("password123")
# driver.find_element(By.ID, "phone").send_keys("abcdefghij")
# driver.find_element(By.ID, "address").send_keys("Test Address 123")
# register_btn = driver.find_element(By.ID, "register-btn")
# driver.execute_script("arguments[0].click();", register_btn)
# time.sleep(2)
# assert "mode=signup" in driver.current_url
# print("BR-009 PASSED - Non-numeric phone rejected")
# clear_local_storage()
# driver.quit()

# BR-012  |  Username minimum length (min 3 characters)  
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("a")
# driver.find_element(By.ID, "password").send_keys("password123")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("Test Address 123")
# register_btn = driver.find_element(By.ID, "register-btn")
# driver.execute_script("arguments[0].click();", register_btn)
# time.sleep(2)
# assert "mode=signup" in driver.current_url
# print("BR-012 PASSED - Short username rejected")
# clear_local_storage()
# driver.quit()

# BR-013  |  Username must not contain special characters  
# Bug: No regex validation — "@user!" is accepted.
# Expect: Error shown and user stays on signup page.
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("test@user!")    # special chars
# driver.find_element(By.ID, "password").send_keys("password123")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("Test Address 123")
# register_btn = driver.find_element(By.ID, "register-btn")
# driver.execute_script("arguments[0].click();", register_btn)
# time.sleep(2)
# assert "mode=signup" in driver.current_url
# print("BR-013 PASSED - Username with special characters rejected")
# clear_local_storage()
# driver.quit()

# TC-USA-002  |  Error message visible on failed register  
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("Test Street 1")
# driver.find_element(By.ID, "register-btn").click()
# time.sleep(2)
# error_msg = driver.find_element(By.ID, "register-error")
# assert error_msg.is_displayed()
# assert len(error_msg.text) > 0
# print("TC-USA-002 PASSED - Register error message is visible with text: " + error_msg.text)
# driver.quit()


# TC-SEC-004  |  XSS in register username  
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("<script>alert('xss')</script>")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("Test Street 1")
# driver.find_element(By.ID, "register-btn").click()
# time.sleep(3)
# try:
#     driver.switch_to.alert.accept()
#     assert False, "XSS script executed - SECURITY FAILURE"
# except:
#     print("TC-SEC-004 PASSED - XSS script not executed in register username")
# clear_local_storage()
# driver.quit()

# TC-SEC-005  |  XSS in address field  
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("xsstest1")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("<img src=x onerror=alert(1)>")
# driver.find_element(By.ID, "register-btn").click()
# time.sleep(3)
# try:
#     driver.switch_to.alert.accept()
#     assert False, "XSS script executed via address field - SECURITY FAILURE"
# except:
#     print("TC-SEC-005 PASSED - XSS script not executed in address field")
# clear_local_storage()
# driver.quit()

# TC-SEC-016  |  Register with extremely long input (500 chars)  *** ACTIVE ***
# long_input = "a" * 500
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys(long_input)
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("Test Street 1")
# driver.find_element(By.ID, "register-btn").click()
# time.sleep(3)
# assert driver.find_element(By.TAG_NAME, "body").is_displayed()
# assert "Internal Server Error" not in driver.page_source
# assert "500" not in driver.title
# print("TC-SEC-016 PASSED - App handled 500-char input without crashing")
# clear_local_storage()
# driver.quit()


# SECTION 2 — SIGNIN / LOGIN

# TC-FUNC-006  |  Login with correct credentials  
# driver.get(f"{BASE_URL}/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" not in driver.current_url
# print("TC-FUNC-006 PASSED - Login with correct credentials")
# clear_local_storage()
# driver.quit()

# TC-FUNC-007  |  Login with wrong password  
# driver.get(f"{BASE_URL}/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("wrongpassword")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-007 PASSED - Login with wrong password rejected")
# clear_local_storage()
# driver.quit()

# TC-FUNC-008  |  Login with non-existent username  
# driver.get(f"{BASE_URL}/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("nonexistentuser")
# driver.find_element(By.ID, "password").send_keys("anyPassword")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-008 PASSED - Login with non-existent username rejected")
# clear_local_storage()
# driver.quit()

# TC-FUNC-009  |  Login with empty username  
# driver.get(f"{BASE_URL}/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-009 PASSED - Login with empty username rejected")
# clear_local_storage()
# driver.quit()

# TC-FUNC-010  |  Login with empty password  
# driver.get(f"{BASE_URL}/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-010 PASSED - Login with empty password rejected")
# clear_local_storage()
# driver.quit()

# TC-FUNC-000  |  Login with both fields empty  
# driver.get(f"{BASE_URL}/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.ID, "login-btn").click()
# assert "/login" in driver.current_url
# print("TC-FUNC-000 PASSED - Login with empty username and password rejected")
# driver.quit()


# Navigate from Sign-In to Sign-Up page 
# try:
#     driver.get(f"{BASE_URL}/login")
#     time.sleep(3)
#     print(driver.current_url)
#     signup_button = driver.find_element(By.ID, 'toggle-login-btn')
#     driver.execute_script("arguments[0].click();", signup_button)
#     time.sleep(2)
#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-003 PASSED - navigation to signup rejected (expected?)")
# except AssertionError:
#     print("TC-003 FAILED - navigating accepted")
# driver.quit()


# Navigate from Registration to Login 
# try:
#     driver.get(f"{BASE_URL}/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)
#     signup_button = driver.find_element(By.ID, 'toggle-login-btn')
#     driver.execute_script("arguments[0].click();", signup_button)
#     time.sleep(2)
#     assert "/login" not in driver.current_url
#     print("TC-003 PASSED - navigation from registration to login rejected")
# except AssertionError:
#     print("TC-003 FAILED - navigating accepted")
# driver.quit()


# Login and then Logout  (File 4)
# try:
#     driver.get(f"{BASE_URL}/login")
#     time.sleep(2)
#     print(driver.current_url)
#     driver.find_element(By.ID, "username").send_keys("sami2")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, 'login-btn').click()
#     time.sleep(2)
#     assert "/login" not in driver.current_url
#     driver.find_element(By.ID, 'logout-btn').click()
#     assert "/login" not in driver.current_url
#     print("0000 - logout successfully")
# except AssertionError:
#     print("0000 - logout failed")
# driver.quit()


# TC-USA-001  |  Error message visible on failed login  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("wrongpassword")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(2)
# error_msg = driver.find_element(By.ID, "login-error")
# assert error_msg.is_displayed()
# assert len(error_msg.text) > 0
# print("TC-USA-001 PASSED - Login error message is visible with text: " + error_msg.text)
# driver.quit()


# TC-SEC-001  |  SQL injection in login username  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("' OR '1'='1")
# driver.find_element(By.ID, "password").send_keys("anything")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(2)
# assert "/login" in driver.current_url
# error_msg = driver.find_element(By.ID, "login-error")
# assert error_msg.is_displayed()
# print("TC-SEC-001 PASSED - SQL injection in username was rejected")
# driver.quit()


# TC-SEC-002  |  SQL injection in login password  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("' OR '1'='1")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(2)
# assert "/login" in driver.current_url
# error_msg = driver.find_element(By.ID, "login-error")
# assert error_msg.is_displayed()
# print("TC-SEC-002 PASSED - SQL injection in password was rejected")
# driver.quit()


# TC-SEC-010  |  Brute force login — 10 wrong attempts all rejected  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# for i in range(10):
#     driver.find_element(By.ID, "username").clear()
#     driver.find_element(By.ID, "username").send_keys("sami2")
#     driver.find_element(By.ID, "password").clear()
#     driver.find_element(By.ID, "password").send_keys(f"wrongpass{i}")
#     driver.find_element(By.ID, "login-btn").click()
#     time.sleep(1)
#     assert "/login" in driver.current_url
# print("TC-SEC-010 PASSED - All 10 brute force attempts were rejected")
# driver.quit()


# TC-SEC-013  |  Password not stored in localStorage  *** ACTIVE ***  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# user_data = driver.execute_script("return window.localStorage.getItem('user');")
# assert user_data is not None
# assert "123456" not in user_data
# assert "password" not in user_data.lower()
# print("TC-SEC-013 PASSED - Password is not stored in localStorage")
# clear_local_storage()
# driver.quit()






# TC-PERF-003  |  Login response time  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# start = time.time()
# driver.find_element(By.ID, "login-btn").click()
# while "/login" in driver.current_url:
#     if time.time() - start > 5:
#         break
#     time.sleep(0.1)
# elapsed = time.time() - start
# assert "/login" not in driver.current_url, "Login did not redirect"
# assert elapsed < 2, f"Login took {elapsed:.2f}s (limit 2s)"
# print(f"TC-PERF-003 PASSED - Login completed in {elapsed:.2f}s")
# clear_local_storage()
# driver.quit()

# TC-PERF-004  |  Register response time  
# driver.get(f"{BASE_URL}/login?mode=signup")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("perftest2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "phone").send_keys("0501234567")
# driver.find_element(By.ID, "address").send_keys("Test Street 1")
# start = time.time()
# driver.find_element(By.ID, "register-btn").click()
# while "/login" in driver.current_url:
#     if time.time() - start > 5:
#         break
#     time.sleep(0.1)
# elapsed = time.time() - start
# assert "/login" not in driver.current_url, "Register did not redirect"
# assert elapsed < 2, f"Register took {elapsed:.2f}s (limit 2s)"
# print(f"TC-PERF-004 PASSED - Registration completed in {elapsed:.2f}s")
# clear_local_storage()
# driver.quit()


# SECTION 3 — MEALS

# TC-FUNC-010  |  Get all meals — expects 9 cards  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')
# assert len(meal_cards) == 9
# print(f"TC-FUNC-010 PASSED - {len(meal_cards)} meals loaded")
# driver.quit()

# TC-FUNC-012  |  Get meal by ID via cart  
# driver.get(f"{BASE_URL}")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# driver.find_element(By.ID, 'cart-btn').click()
# cart = driver.find_element(By.ID, 'cart-item-1')
# time.sleep(2)
# assert cart is not None
# print("TC-FUNC-012 PASSED - Meal details retrieved by ID")
# driver.quit()

# TC-FUNC-012  |  Get meal by non-existent ID  
# driver.get("http://localhost:8000/meals/99")
# time.sleep(2)
# assert "Not Found" in driver.page_source
# print("TC-FUNC-012 PASSED - Meal not found")
# driver.quit()

# TC-FUNC-011  |  Cannot decrement below zero  
# driver.get(f"{BASE_URL}/")
# revitem = driver.find_element(By.ID, 'remove-from-cart-2')
# driver.execute_script("arguments[0].click();", revitem)
# que = driver.find_element(By.ID, 'quantityOfMeal')
# print("TC-FUNC-011 PASSED - Cannot decrement meal quantity below zero")
# driver.quit()



# TC-FUNC-061  |  Home page loads with meal cards  *** ACTIVE ***  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')
# assert len(meal_cards) > 0
# print("TC-FUNC-061 PASSED - Home page loaded with meal cards")
# driver.quit()


# TC-FUNC-059  |  Meal subtotal shown when qty > 0  *** ACTIVE ***  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# time.sleep(1)
# subtotal = driver.find_element(By.ID, 'meal-subtotal-1')
# assert subtotal.is_displayed()
# print("TC-FUNC-059 PASSED - Subtotal text appears after adding meal 1")
# driver.quit()


# TC-FUNC-060  |  Meal subtotal hidden when qty = 0  *** ACTIVE ***  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# subtotals = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-subtotal")]')
# assert len(subtotals) == 0
# print("TC-FUNC-060 PASSED - No subtotal elements shown when cart is empty")
# driver.quit()







# Add meal to cart — verifies total price  
# try:
#     driver.get(f"{BASE_URL}")
#     time.sleep(2)
#     meal1 = driver.find_element(By.ID, 'add-to-cart-1')
#     driver.execute_script("arguments[0].click();", meal1)
#     time.sleep(1)
#     cart = driver.find_element(By.ID, "cart-btn").click()
#     time.sleep(1)
#     total = driver.find_element(By.ID, "cart-total-price").text
#     price = int(total.replace("₺", ""))
#     assert price == 120
#     print("00000 - Meal 1 added to cart")
# except AssertionError:
#     print("00000 - Meal 1 not added to cart")
# clear_local_storage()
# driver.quit()

# Add same meal multiple times to cart 
# try:
#     driver.get(f"{BASE_URL}")
#     time.sleep(2)
#     meal1 = driver.find_element(By.ID, 'add-to-cart-1')
#     driver.execute_script("arguments[0].click();", meal1)
#     driver.execute_script("arguments[0].click();", meal1)
#     driver.execute_script("arguments[0].click();", meal1)
#     time.sleep(1)
#     cart = driver.find_element(By.ID, "cart-btn").click()
#     time.sleep(1)
#     total = driver.find_element(By.ID, "cart-total-price").text
#     price = int(total.replace("₺", ""))
#     assert price == 360
#     print("00000 - Meal 1 added multiple times to cart")
# except AssertionError:
#     print("00000 - Meal 1 not added multiple times to cart")
# clear_local_storage()
# driver.quit()

# Removing meal from cart (quantity decrease) 
# driver.get(f"{BASE_URL}")
# time.sleep(2)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# driver.execute_script("arguments[0].click();", addbtu)
# driver.execute_script("arguments[0].click();", addbtu)
# driver.execute_script("arguments[0].click();", addbtu)
# driver.execute_script("arguments[0].click();", addbtu)
# driver.find_element(By.ID, 'cart-btn').click()
# removebut = driver.find_element(By.ID, 'decrease-1')
# driver.execute_script("arguments[0].click();", removebut)
# time.sleep(2)
# total = driver.find_element(By.ID, "cart-total-price").text
# price = int(total.replace("₺", ""))
# assert price == 480
# print("00000 - Removing one item correctly")
# driver.quit()


# TC-PERF-001  |  Home page initial load time  
# start = time.time()
# driver.get(f"{BASE_URL}/")
# while len(driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')) == 0:
#     if time.time() - start > 10:
#         break
#     time.sleep(0.1)
# elapsed = time.time() - start
# assert elapsed < 3, f"Home page took {elapsed:.2f}s (limit 3s)"
# print(f"TC-PERF-001 PASSED - Home page loaded in {elapsed:.2f}s")
# driver.quit()


# SECTION 4 — CART BAR

# TC-FUNC-012  |  CartBar total is correct  
# driver.get(f"{BASE_URL}/")
# addbtu1 = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu1)
# price1 = driver.find_element(By.ID, "meal-price-1").text
# addbtu2 = driver.find_element(By.ID, 'add-to-cart-2')
# driver.execute_script("arguments[0].click();", addbtu2)
# price2 = driver.find_element(By.ID, "meal-price-2").text
# total_price = driver.find_element(By.ID, 'cartbar-total-price').text
# price1_value = float(price1.replace('₺', ''))
# price2_value = float(price2.replace('₺', ''))
# total_price_value = float(total_price.replace('Total: ₺', ''))
# assert total_price_value == price1_value + price2_value
# print("TC-FUNC-012 PASSED - Cart total is correct")
# driver.quit()


# Confirm button hidden when cart is empty  (File 4)
# try:
#     driver.get(f"{BASE_URL}/")
#     time.sleep(2)
#     cart_btn = driver.find_element(By.ID, "cart-btn")
#     assert cart_btn.is_displayed() == False
#     print("000000000 PASSED - Confirm button hidden when cart is empty")
# except AssertionError:
#     print("00000000000 FAILED - Confirm button is visible while cart is empty")
# clear_local_storage()
# driver.quit()

# Confirm button visible when cart is not empty  (File 4)
# try:
#     driver.get(f"{BASE_URL}/")
#     time.sleep(2)
#     addbtu = driver.find_element(By.ID, 'add-to-cart-1')
#     driver.execute_script("arguments[0].click();", addbtu)
#     time.sleep(1)
#     cart_btn = driver.find_element(By.ID, "cart-btn")
#     assert cart_btn.is_displayed() == True
#     print("000000000 PASSED - Confirm button visible when cart is not empty")
# except AssertionError:
#     print("00000000000 FAILED - Confirm button is not visible while cart is not empty")
# clear_local_storage()
# driver.quit()

# TC-USA-006  |  Cart bar hidden when cart is empty  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# assert not cart_btn.is_displayed()
# print("TC-USA-006 PASSED - Cart bar confirm button is hidden when cart is empty")
# driver.quit()


# TC-USA-007  |  Cart bar appears after adding item  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# time.sleep(1)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# assert cart_btn.is_displayed()
# print("TC-USA-007 PASSED - Cart bar confirm button is visible after adding item")
# clear_local_storage()
# driver.quit()

# BR-011  |  Cart contents must survive page refresh  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# add_btn = driver.find_element(By.ID, "add-to-cart-1")
# driver.execute_script("arguments[0].click();", add_btn)
# time.sleep(1)
# total_before = driver.find_element(By.ID, "cartbar-total-price").text
# driver.refresh()
# time.sleep(3)
# total_after = driver.find_element(By.ID, "cartbar-total-price").text
# assert total_after == total_before
# print("BR-011 PASSED - Cart persisted after refresh")
# driver.quit()


# TC-PERF-008  |  Add to cart instant feedback  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# start = time.time()
# driver.execute_script("arguments[0].click();", addbtu)
# cart_bar = driver.find_element(By.ID, 'cart-btn')
# while not cart_bar.is_displayed():
#     if time.time() - start > 2:
#         break
#     time.sleep(0.05)
# elapsed = (time.time() - start) * 1000
# assert elapsed < 200, f"Cart bar took {elapsed:.0f}ms to appear (limit 200ms)"
# print(f"TC-PERF-008 PASSED - Cart bar appeared in {elapsed:.0f}ms after add")
# driver.quit()



# SECTION 5 — CART MODAL


# TC-FUNC-013  |  Open cart modal via CartBar  
# driver.get(f"{BASE_URL}/")
# cart_btn = driver.find_element(By.ID, 'add-to-cart-3')
# driver.execute_script("arguments[0].click();", cart_btn)
# cart_modal = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_modal)
# meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "cart-item")]')
# assert len(meal_cards) == 1
# print("TC-FUNC-013 PASSED - Cart modal opens when clicking cart button")
# driver.quit()


# TC-FUNC-014  |  Close cart modal   
# driver.get(f"{BASE_URL}/")
# cart_btn = driver.find_element(By.ID, 'add-to-cart-3')
# driver.execute_script("arguments[0].click();", cart_btn)
# cart_modal_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_modal_btn)
# close_btn = driver.find_element(By.ID, 'close-cart-btn')
# driver.execute_script("arguments[0].click();", close_btn)
# time.sleep(2)
# cart_modal = driver.find_element(By.ID, 'cart-modal')
# time.sleep(3)
# assert not cart_modal.is_displayed()
# print("TC-FUNC-014 PASSED - Cart modal closes when clicking close button")
# driver.quit()


# TC-FUNC-038  |  Cart modal shows empty state message   
# driver.get(f"{BASE_URL}/")
# time.sleep(2)
# nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
# driver.execute_script("arguments[0].click();", nav_cart)
# time.sleep(1)
# empty_msg = driver.find_element(By.XPATH, '//p[contains(text(), "Your cart is empty")]')
# assert empty_msg.is_displayed()
# print("TC-FUNC-038 PASSED - Cart modal shows empty state message")
# driver.quit()


# TC-FUNC-037  |  Cart modal shows correct number of items    
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# addbtu1 = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu1)
# addbtu2 = driver.find_element(By.ID, 'add-to-cart-2')
# driver.execute_script("arguments[0].click();", addbtu2)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# cart_items = driver.find_elements(By.XPATH, '//*[contains(@id, "cart-item")]')
# assert len(cart_items) == 2
# print("TC-FUNC-037 PASSED - Cart modal shows 2 items after adding 2 meals")
# driver.quit()



# TC-FUNC-043  |  Cart item IDs present in modal  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# cart_item = driver.find_element(By.ID, 'cart-item-1')
# assert cart_item is not None
# print("TC-FUNC-043 PASSED - cart-item-1 element exists in cart modal")
# driver.quit()


# TC-FUNC-046  |  Place order when not logged in shows error    
# driver.get(f"{BASE_URL}/")
# clear_local_storage()
# driver.quit()
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# place_order = driver.find_element(By.ID, 'place-order-btn')
# driver.execute_script("arguments[0].click();", place_order)
# time.sleep(1)
# error_msg = driver.find_element(By.ID, 'cart-error')
# assert error_msg.is_displayed()
# assert "sign in" in error_msg.text.lower()
# print("TC-FUNC-046 PASSED - cart-error shown when placing order without login")
# driver.quit()


# Open cart via nav button  
# try:
#     driver.get(f"{BASE_URL}")
#     time.sleep(1)
#     openCart = driver.find_element(By.ID, 'nav-cart-btn')
#     driver.execute_script("arguments[0].click();", openCart)
#     time.sleep(1)
#     cart_btn = driver.find_element(By.ID, "cart-btn")
#     assert cart_btn.is_displayed() == True
#     print("000000000 PASSED - Cart model is opened via button in nav")
# except AssertionError:
#     print("00000000000 FAILED - Cart model is not opened via button in nav")
# clear_local_storage()
# driver.quit()


# Increasing item quantity via cart modal 
# try:
#     driver.get(f"{BASE_URL}")
#     time.sleep(1)
#     addbtu = driver.find_element(By.ID, 'add-to-cart-3')
#     driver.execute_script("arguments[0].click();", addbtu)
#     openCart = driver.find_element(By.ID, 'nav-cart-btn')
#     driver.execute_script("arguments[0].click();", openCart)
#     time.sleep(1)
#     cart_btn = driver.find_element(By.ID, "cart-btn")
#     driver.execute_script("arguments[0].click();", cart_btn)
#     driver.find_element(By.ID, 'increase-3').click()
#     driver.find_element(By.ID, 'increase-3').click()
#     total = driver.find_element(By.ID, "cart-total-price").text
#     price = int(total.replace("₺", ""))
#     assert price == 300
#     print("000000000 PASSED - Increasing item quantity via cart modal is successful")
# except AssertionError:
#     print("00000000000 FAILED - Cart model is not opened via button in nav")
# driver.quit()


# Decreasing item quantity via cart modal  
# try:
#     driver.get(f"{BASE_URL}")
#     time.sleep(1)
#     addbtu = driver.find_element(By.ID, 'add-to-cart-3')
#     driver.execute_script("arguments[0].click();", addbtu)
#     driver.execute_script("arguments[0].click();", addbtu)
#     driver.execute_script("arguments[0].click();", addbtu)
#     openCart = driver.find_element(By.ID, 'nav-cart-btn')
#     driver.execute_script("arguments[0].click();", openCart)
#     time.sleep(1)
#     cart_btn = driver.find_element(By.ID, "cart-btn")
#     driver.execute_script("arguments[0].click();", cart_btn)
#     driver.find_element(By.ID, 'decrease-3').click()
#     driver.find_element(By.ID, 'decrease-3').click()
#     total = driver.find_element(By.ID, "cart-total-price").text
#     price = int(total.replace("₺", ""))
#     assert price == 100
#     print("000000000 PASSED - Decreasing item quantity via cart modal is successful")
# except AssertionError:
#     print("00000000000 FAILED - Decreasing item quantity via cart modal is not successful")
# clear_local_storage()
# driver.quit()

# Completely removing a meal 
# driver.get(f"{BASE_URL}")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# driver.execute_script("arguments[0].click();", addbtu)
# driver.find_element(By.ID, 'cart-btn').click()
# emovebut = driver.find_element(By.ID, 'decrease-1')
# driver.execute_script("arguments[0].click();", emovebut)
# driver.execute_script("arguments[0].click();", emovebut)
# time.sleep(2)
# total = driver.find_element(By.ID, "cart-total-price").text
# price = int(total.replace("₺", ""))
# assert price == 0
# print("00000 - completely removed correctly")
# driver.quit()


# TC-USA-010  |  Empty cart message and disabled button in modal  
# driver.get(f"{BASE_URL}/")
# time.sleep(2)
# nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
# driver.execute_script("arguments[0].click();", nav_cart)
# time.sleep(1)
# empty_msg = driver.find_element(By.XPATH, '//p[contains(text(), "Your cart is empty")]')
# assert empty_msg.is_displayed()
# place_btn = driver.find_element(By.ID, 'place-order-btn')
# assert place_btn.get_attribute("disabled") is not None
# print("TC-USA-010 PASSED - Empty cart message visible and place order button is disabled")
# driver.quit()



# TC-PERF-007  |  Cart modal opens instantly  
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
# start = time.time()
# driver.execute_script("arguments[0].click();", nav_cart)
# driver.find_element(By.ID, 'cart-modal')
# elapsed = (time.time() - start) * 1000
# assert elapsed < 300, f"Cart modal took {elapsed:.0f}ms to open (limit 300ms)"
# print(f"TC-PERF-007 PASSED - Cart modal opened in {elapsed:.0f}ms")
# driver.quit()



# BR-007  |  Maximum quantity per item (max 10)  ACTIVE   
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# add_btn = driver.find_element(By.ID, "add-to-cart-1")
# for _ in range(11):
#     driver.execute_script("arguments[0].click();", add_btn)
#     time.sleep(0.15)
# cart_btn = driver.find_element(By.ID, "cart-btn")
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# qty_el = driver.find_element(By.ID, "quantity-1")
# quantity = int(qty_el.text)
# assert quantity <= 10
# print(f"BR-007 PASSED - Quantity capped at {quantity}")
# close_btn = driver.find_element(By.ID, "close-cart-btn")
# driver.execute_script("arguments[0].click();", close_btn)
# driver.quit()


# SECTION 6 — ORDERS

# TC-FUNC-013  |  My Orders link navigates to orders  
# driver.get(f"{BASE_URL}/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.find_element(By.ID, 'my-orders-link').click()
# time.sleep(2)
# assert "MyOrders" in driver.current_url
# print("TC-FUNC-013 PASSED - My Orders link navigates to orders page")
# clear_local_storage()
# driver.quit()

# TC-FUNC-014  |  My Orders redirects unauthenticated user  
# driver.get(f"{BASE_URL}/")
# driver.find_element(By.ID, 'my-orders-link').click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-014 PASSED - My Orders redirects unauthenticated user to login page")
# driver.quit()


# TC-FUNC-015  |  Create order with valid data  
# try:
#     driver.get(f"{BASE_URL}/")
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     driver.find_element(By.ID, "place-order-btn").click()
#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()
#     assert "placed successfully" in alert_text or "Order #" in alert_text
#     print("TC-FUNC-015 PASSED - Single item order created")
# except AssertionError:
#     print("TC-FUNC-015 FAILED - Order not created correctly")
# clear_local_storage()
# driver.quit()

# TC-FUNC-016  |  Create order with non-existent meal 
# try:
#     driver.get(f"{BASE_URL}/")
#     driver.find_element(By.ID, "add-to-cart-9999").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     driver.find_element(By.ID, "place-order-btn").click()
#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()
#     assert "placed successfully" not in alert_text
#     print("TC-FUNC-016 FAILED - Order should not be created with non-existent meal")
# except AssertionError:
#     print("TC-FUNC-016 PASSED - Non-existent meal correctly rejected")
# clear_local_storage()
# driver.quit()


# TC-FUNC-017  |  Create order with multiple items 
# try:
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "add-to-cart-2").click()
#     driver.find_element(By.ID, "add-to-cart-2").click()
#     driver.find_element(By.ID, "add-to-cart-2").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     driver.find_element(By.ID, "place-order-btn").click()
#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()
#     assert "placed successfully" in alert_text or "Order #" in alert_text
#     print("TC-FUNC-017 PASSED - Multiple items order created")
# except AssertionError:
#     print("TC-FUNC-017 FAILED - Order assertion failed")
# clear_local_storage()
# driver.quit()


# TC-FUNC-019  |  Get orders for non-existent user 
# try:
#     driver.get(f"{BASE_URL}/")
#     driver.execute_script(
#         "window.localStorage.setItem('user', JSON.stringify({user_id: 99999}))"
#     )
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     driver.find_element(By.ID, "place-order-btn").click()
#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()
#     assert "placed successfully" not in alert_text
#     print("TC-FUNC-019 PASSED - Non-existent user blocked from ordering")
# except AssertionError:
#     print("TC-FUNC-019 FAILED - Invalid user was able to place order")
# except Exception:
#     print("TC-FUNC-019 PASSED - System blocked non-existent user correctly")
# clear_local_storage()
# driver.quit()



# TC-FUNC-020  |  Create order with quantity = 0  
# try:
#     driver.get(f"{BASE_URL}/")
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     minus_btn = driver.find_element(By.ID, "remove-from-cart-1")
#     minus_btn.click()
#     driver.find_element(By.ID, "place-order-btn").click()
#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()
#     assert "placed successfully" not in alert_text
#     print("TC-FUNC-020 PASSED - Order with quantity 0 rejected")
# except AssertionError:
#     print("TC-FUNC-020 FAILED - Order created with quantity 0")
# clear_local_storage()
# driver.quit()


# TC-FUNC-021  |  Create order with negative quantity 
# try:
#     driver.get(f"{BASE_URL}/")
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     driver.find_element(By.ID, "remove-from-cart-1").click()
#     driver.find_element(By.ID, "remove-from-cart-1").click()    # now should be -1
#     driver.find_element(By.ID, "place-order-btn").click()
#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()
#     assert "placed successfully" not in alert_text
#     print("TC-FUNC-021 PASSED - Negative quantity blocked correctly")
# except AssertionError:
#     print("TC-FUNC-021 FAILED - Order created with negative quantity")
# clear_local_storage()
# driver.quit()

# TC-FUNC-024  |  Verify total price calculation  
# try:
#     driver.get(f"{BASE_URL}/")
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     quantity_text = driver.find_element(By.ID, "quantityOfMeal").text
#     quantity = int(quantity_text)
#     price_text = driver.find_element(By.XPATH, "//p[contains(text(),'₺')]").text
#     price = float(price_text.replace("₺", "").strip())
#     subtotal_text = driver.find_element(By.XPATH, "//p[contains(text(),'Subtotal')]").text
#     subtotal = float(subtotal_text.replace("Subtotal: ₺", "").strip())
#     expected = round(quantity * price, 2)
#     assert expected == subtotal
#     print("TC-FUNC-024 PASSED - Total price calculation is correct")
# except AssertionError:
#     print("TC-FUNC-024 FAILED - Price calculation mismatch")
# clear_local_storage()
# driver.quit()



# BR-010  |  Order confirmation shown after successful order 
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# login_btn = driver.find_element(By.ID, "login-btn")
# driver.execute_script("arguments[0].click();", login_btn)
# time.sleep(3)
# add_btn = driver.find_element(By.ID, "add-to-cart-1")
# driver.execute_script("arguments[0].click();", add_btn)
# cart_btn = driver.find_element(By.ID, "cart-btn")
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# place_order_btn = driver.find_element(By.ID, "place-order-btn")
# driver.execute_script("arguments[0].click();", place_order_btn)
# time.sleep(2)
# success_elements = driver.find_elements(
#     By.XPATH,
#     '//*[contains(text(),"success") or contains(text(),"placed") or contains(text(),"confirmed")]'
# )
# assert len(success_elements) > 0
# print("BR-010 PASSED - Success message shown after order")
# clear_local_storage()
# driver.quit()

# TC-FUNC-049  |  View My Orders page 
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(3)
# assert "MyOrders" in driver.current_url
# print("TC-FUNC-049 PASSED - My Orders page loads for logged-in user")
# clear_local_storage()
# driver.quit()

# TC-FUNC-050  |  Order cards present in DOM
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# place_order = driver.find_element(By.ID, 'place-order-btn')
# driver.execute_script("arguments[0].click();", place_order)
# time.sleep(1)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(3)
# order_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')
# assert len(order_cards) > 0
# print("TC-FUNC-050 PASSED - Order cards displayed for user with orders")
# clear_local_storage()
# driver.quit()

# TC-FUNC-051  |  Order card shows title and price 
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(3)
# order_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')
# first_card = order_cards[0]
# price_el = first_card.find_element(By.XPATH, './/p[contains(text(), "₺")]')
# assert price_el.is_displayed()
# print("TC-FUNC-051 PASSED - Order card shows price information")
# clear_local_storage()
# driver.quit()

# TC-FUNC-052  |  Grand total section visible on orders page 
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(3)
# grand_total = driver.find_element(By.XPATH, '//p[contains(text(), "All Orders Total")]')
# assert grand_total.is_displayed()
# print("TC-FUNC-052 PASSED - Grand total section is visible on orders page")
# clear_local_storage()
# driver.quit()

# TC-FUNC-053  |  No orders message for user with no orders 
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami5")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(5)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(3)
# no_orders_msg = driver.find_element(By.XPATH, "//p[contains(text(), \"haven't placed any orders\")]")
# assert no_orders_msg.is_displayed()
# print("TC-FUNC-053 PASSED - No orders message shown for user with no orders")
# clear_local_storage()
# driver.quit()







# TC-SEC-006  |  Access My Orders without authentication  
# clear_local_storage()
# driver.quit()
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-SEC-006 PASSED - Unauthenticated user redirected to login from /MyOrders")
# driver.quit()


# TC-USA-014  |  My Orders shows empty state clearly  
# NOTE: use a username that has no orders (e.g. sami5)
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami5")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(3)
# empty_msg = driver.find_element(By.XPATH, "//p[contains(text(), \"haven't placed any orders\")]")
# assert empty_msg.is_displayed()
# print("TC-USA-014 PASSED - Empty orders state message is clearly displayed")
# clear_local_storage()
# driver.quit()

# TC-USA-005  |  Place Order button shows loading state  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# place_btn = driver.find_element(By.ID, 'place-order-btn')
# driver.execute_script("arguments[0].click();", place_btn)
# time.sleep(0.5)
# btn_text = place_btn.text
# assert btn_text == "Placing order..."
# print("TC-USA-005 PASSED - Button showed 'Placing order...' during request")
# time.sleep(3)
# driver.find_element(By.ID, 'close-cart-btn').click()
# clear_local_storage()
# driver.quit()

# TC-USA-011  |  Order confirmation message is clear  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# driver.find_element(By.ID, 'place-order-btn').click()
# time.sleep(4)
# success_msg = driver.find_element(By.ID, 'order-success-msg')
# assert success_msg.is_displayed()
# assert "placed successfully" in success_msg.text or "Order" in success_msg.text
# print("TC-USA-011 PASSED - Order confirmation message is clear: " + success_msg.text)
# driver.find_element(By.ID, 'close-cart-btn').click()
# clear_local_storage()
# driver.quit()


# SECTION 7 — PERFORMANCE TESTS

# TC-PERF-005  |  Place order response time  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# start = time.time()
# driver.find_element(By.ID, 'place-order-btn').click()
# elapsed = time.time() - start
# assert elapsed < 2, f"Order placement took {elapsed:.2f}s (limit 2s)"
# print(f"TC-PERF-005 PASSED - Order placed in {elapsed:.2f}s")
# clear_local_storage()
# driver.quit()


# TC-PERF-006  |  My Orders page load time  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# start = time.time()
# driver.get(f"{BASE_URL}/MyOrders")
# while len(driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')) == 0:
#     if time.time() - start > 10:
#         break
#     time.sleep(0.1)
# elapsed = time.time() - start
# assert elapsed < 3, f"My Orders page took {elapsed:.2f}s (limit 3s)"
# print(f"TC-PERF-006 PASSED - My Orders page loaded in {elapsed:.2f}s")
# clear_local_storage()
# driver.quit()

# TC-PERF-010  |  My Orders page with many orders   
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(4)
# order_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')
# logs = driver.get_log('browser')
# errors = [l for l in logs if l['level'] == 'SEVERE']
# assert len(errors) == 0, f"JS errors found: {errors}"
# assert len(order_cards) > 0
# print(f"TC-PERF-010 PASSED - Orders page rendered {len(order_cards)} cards with no JS errors")
# clear_local_storage()
# driver.quit()

# TC-PERF-011  |  Simultaneous cart operations (10 rapid clicks)   
# driver.get(f"{BASE_URL}/")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# for r in range(10):
#     driver.execute_script("arguments[0].click();", addbtu)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_btn)
# time.sleep(1)
# quantity = driver.find_element(By.ID, 'quantity-1').text
# assert quantity == "10", f"Expected quantity 10, got {quantity}"
# logs = driver.get_log('browser')
# errors = [l for l in logs if l['level'] == 'SEVERE']
# assert len(errors) == 0, f"JS errors after rapid clicks: {errors}"
# print(f"TC-PERF-011 PASSED - 10 rapid clicks resulted in quantity {quantity} with no JS errors")
# driver.quit()



# SECTION 8 — USABILITY / NAVBAR

# TC-USA-019  |  Username displayed in navbar after login  
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# username_display = driver.find_element(By.XPATH, '//span[contains(text(), "sami2")]')
# assert username_display.is_displayed()
# print("TC-USA-019 PASSED - Username 'sami2' is visible in the navbar after login")
# clear_local_storage()
# driver.quit()

# TC-USA-020  |  Page title visible on My Orders page 
# driver.get(f"{BASE_URL}/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get(f"{BASE_URL}/MyOrders")
# time.sleep(2)
# heading = driver.find_element(By.XPATH, '//h1[contains(text(), "My Orders")]')
# assert heading.is_displayed()
# print("TC-USA-020 PASSED - 'My Orders' heading is clearly visible on the orders page")
# clear_local_storage()
# driver.quit()

# End of test cases

input("Press Enter to close...")
driver.quit()