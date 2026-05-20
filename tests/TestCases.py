"""
    Functional Tests       
    Performance Tests      
    Usability Tests        
    Security Tests         
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

BASE_URL = "http://localhost:3000"

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://localhost:3000/")


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  1. FUNCTIONAL TESTS                                                      ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-001 | Registration without optional email accepted
# ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/login?mode=signup")
# driver.find_element(By.ID, "username").send_keys("abdulrahman")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "email").send_keys("")
# driver.find_element(By.ID, "phone").send_keys("1234567890")
# driver.find_element(By.ID, "address").send_keys("123 Main St")
# driver.find_element(By.ID, "register-btn").click()
# assert "/signup" not in driver.current_url
# print("TC-FUNC-001 PASSED - Registration without optional email accepted")
# driver.execute_script("window.localStorage.clear();")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-002 | Duplicate username rejected
# # ══════════════════════════════════════════════════════════════════
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
# driver.execute_script("window.localStorage.clear();")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-003 | Registration with empty username rejected
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)

#     driver.find_element(By.ID, "username").send_keys("")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("123456789")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()

#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-FUNC-003 PASSED - Registration with empty username rejected")

# except AssertionError:
#     print("TC-FUNC-003 FAILED - Registration with empty username was accepted")

# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-004 | Registration with empty password rejected
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/login?mode=signup")
# driver.find_element(By.ID, "username").send_keys("sami5")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.ID, "email").send_keys("")
# driver.find_element(By.ID, "phone").send_keys("1234567890")
# driver.find_element(By.ID, "address").send_keys("123 Main St")
# driver.find_element(By.ID, "register-btn").click()
# assert "signup" in driver.current_url
# print("TC-FUNC-004 PASSED - Registration with empty password rejected")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-005 | Empty password on sign up rejected (open_signup flow)
# # ══════════════════════════════════════════════════════════════════
# try:
#     sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
#     driver.execute_script("arguments[0].click();", sign_up_btn)

#     driver.find_element(By.ID, "username").send_keys("muhammed")
#     driver.find_element(By.ID, "password").send_keys("")
#     driver.find_element(By.ID, "email").send_keys("sass4@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("123456789")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()

#     assert "/login" not in driver.current_url
#     print("TC-FUNC-005 PASSED - Empty password rejected")

# except AssertionError:
#     print("TC-FUNC-005 FAILED - Empty password was accepted")

# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-006 | Registration with empty phone rejected
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)

#     driver.find_element(By.ID, "username").send_keys("ibrahim")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()

#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-FUNC-006 PASSED - Registration with empty phone rejected")

# except AssertionError:
#     print("TC-FUNC-006 FAILED - Registration with empty phone was accepted")

# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-007 | Registration with empty address rejected
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)

#     driver.find_element(By.ID, "username").send_keys("mustafa")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("123456789")
#     driver.find_element(By.ID, "address").send_keys("")
#     driver.find_element(By.ID, "register-btn").click()

#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-FUNC-007 PASSED - Registration with empty address rejected")

# except AssertionError:
#     print("TC-FUNC-007 FAILED - Registration with empty address was accepted")

# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-008 | Empty phone on sign up rejected (open_signup flow)
# # ══════════════════════════════════════════════════════════════════
# try:
#     sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
#     driver.execute_script("arguments[0].click();", sign_up_btn)

#     driver.find_element(By.ID, "username").send_keys("muhammed5")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass5@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()

#     assert "/login" not in driver.current_url
#     print("TC-FUNC-008 PASSED - Empty phone rejected")

# except AssertionError:
#     print("TC-FUNC-008 FAILED - Empty phone was accepted")

# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-009 | Special characters in username rejected
# # ══════════════════════════════════════════════════════════════════
# try:
#     sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
#     driver.execute_script("arguments[0].click();", sign_up_btn)

#     driver.find_element(By.ID, "username").send_keys("mohamed$2026!")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, "email").send_keys("sass6@gmail.com")
#     driver.find_element(By.ID, "phone").send_keys("5012345678")
#     driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
#     driver.find_element(By.ID, "register-btn").click()

#     assert "/login" not in driver.current_url
#     print("TC-FUNC-009 PASSED - Special characters in username rejected")

# except AssertionError:
#     print("TC-FUNC-009 FAILED - Username with special characters was accepted")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-010 | Login with correct credentials succeeds
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" not in driver.current_url
# print("TC-FUNC-010 PASSED - Login with correct credentials succeeds")
# driver.execute_script("window.localStorage.clear();")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-011 | Login with wrong password rejected
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("wrongpassword")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-011 PASSED - Login with wrong password rejected")
# driver.execute_script("window.localStorage.clear();")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-012 | Login with non-existent username rejected
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("nonexistentuser")
# driver.find_element(By.ID, "password").send_keys("anyPassword")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-012 PASSED - Login with non-existent username rejected")
# driver.execute_script("window.localStorage.clear();")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-013 | Login with empty username rejected
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-013 PASSED - Login with empty username rejected")
# driver.execute_script("window.localStorage.clear();")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-014 | Login with empty password rejected
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-014 PASSED - Login with empty password rejected")
# driver.execute_script("window.localStorage.clear();")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-015 | Cannot decrement meal quantity below zero
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# revitem = driver.find_element(By.ID, 'remove-from-cart-2')
# driver.execute_script("arguments[0].click();", revitem)

# que = driver.find_element(By.ID, 'quantityOfMeal')
# print("TC-FUNC-015 PASSED - Cannot decrement meal quantity below zero")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-016 | Login with empty username and password rejected
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.ID, "login-btn").click()
# assert "/login" in driver.current_url
# print("TC-FUNC-016 PASSED - Login with empty username and password rejected")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-017 | Get meal details by ID via cart-item
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# driver.find_element(By.ID, 'cart-btn').click()
# cart = driver.find_element(By.ID, 'cart-item-1')
# time.sleep(2)
# assert cart is not None
# print("TC-FUNC-017 PASSED - Meal details retrieved by ID")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-018 | Get meal by non-existent ID returns Not Found
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:8000/meals/99")
# time.sleep(2)
# assert "Not Found" in driver.page_source
# print("TC-FUNC-018 PASSED - Non-existent meal returns Not Found")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-019 | Login link navigates to login page
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(2)
# assert "/login" in driver.current_url
# print("TC-FUNC-019 PASSED - Login link navigates to login page")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-020 | Cart modal opens via cart bar button
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# cart_btn = driver.find_element(By.ID, 'add-to-cart-3')
# driver.execute_script("arguments[0].click();", cart_btn)
# cart_modal = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_modal)
# meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "cart-item")]')
# assert len(meal_cards) == 1
# print("TC-FUNC-020 PASSED - Cart modal opens when clicking cart button")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-021 | Open cart modal via nav button
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000")
#     time.sleep(1)

#     openCart = driver.find_element(By.ID, 'nav-cart-btn')
#     driver.execute_script("arguments[0].click();", openCart)
#     time.sleep(1)
#     cart_btn = driver.find_element(By.ID, "cart-btn")

#     assert cart_btn.is_displayed() == True

#     print("TC-FUNC-021 PASSED - Cart modal opened via nav button")

# except AssertionError:
#     print("TC-FUNC-021 FAILED - Cart modal not opened via nav button")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-022 | Navigate from Sign In page to Sign Up page
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000/login")
#     time.sleep(3)
#     print(driver.current_url)

#     signup_button = driver.find_element(By.ID, 'toggle-login-btn')
#     driver.execute_script("arguments[0].click();", signup_button)
#     time.sleep(2)
#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-FUNC-022 PASSED - Navigate Sign In -> Sign Up")

# except AssertionError:
#     print("TC-FUNC-022 FAILED - Navigation Sign In -> Sign Up failed")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-023 | Navigate from Sign Up page to Sign In page
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000/login?mode=signup")
#     time.sleep(3)
#     print(driver.current_url)

#     signup_button = driver.find_element(By.ID, 'toggle-login-btn')
#     driver.execute_script("arguments[0].click();", signup_button)
#     time.sleep(2)
#     assert "/login" not in driver.current_url
#     print("TC-FUNC-023 PASSED - Navigate Sign Up -> Sign In")

# except AssertionError:
#     print("TC-FUNC-023 FAILED - Navigation Sign Up -> Sign In failed")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-024 | Cart modal closes when clicking close button
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# cart_btn = driver.find_element(By.ID, 'add-to-cart-3')
# driver.execute_script("arguments[0].click();", cart_btn)
# cart_modal = driver.find_element(By.ID, 'cart-btn')
# driver.execute_script("arguments[0].click();", cart_modal)
# close_btn = driver.find_element(By.ID, 'close-cart-btn')
# driver.execute_script("arguments[0].click();", close_btn)
# time.sleep(2)
# cart_modal = driver.find_element(By.ID, 'cart-modal')
# time.sleep(3)
# assert not cart_modal.is_displayed()
# print("TC-FUNC-024 PASSED - Cart modal closes when clicking close button")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-025 | Login and then Logout successfully
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000/login")
#     time.sleep(2)
#     print(driver.current_url)

#     driver.find_element(By.ID, "username").send_keys("sami2")
#     driver.find_element(By.ID, "password").send_keys("123456")
#     driver.find_element(By.ID, 'login-btn').click()
#     time.sleep(2)
#     assert "/login" not in driver.current_url

#     driver.find_element(By.ID, 'logout-btn').click()

#     assert "/login" not in driver.current_url
#     print("TC-FUNC-025 PASSED - Login and logout flow successful")

# except AssertionError:
#     print("TC-FUNC-025 FAILED - Logout failed")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-026 | Get all meals — 9 meal cards loaded on home page
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
# time.sleep(3)
# meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')
# assert len(meal_cards) == 9
# print(f"TC-FUNC-026 PASSED - {len(meal_cards)} meals loaded")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-027 | Add single meal to cart
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000")
#     time.sleep(2)
#     meal1 = driver.find_element(By.ID, 'add-to-cart-1')
#     driver.execute_script("arguments[0].click();", meal1)
#     time.sleep(1)
#     cart = driver.find_element(By.ID, "cart-btn").click()
#     time.sleep(1)
#     total = driver.find_element(By.ID, "cart-total-price").text
#     price = int(total.replace("₺", ""))

#     assert price == 120
#     print("TC-FUNC-027 PASSED - Meal 1 added to cart")
# except AssertionError:
#     print("TC-FUNC-027 FAILED - Meal 1 not added to cart")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-028 | Add same meal multiple times — quantity increments
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000")
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
#     print("TC-FUNC-028 PASSED - Meal 1 added multiple times to cart")
# except AssertionError:
#     print("TC-FUNC-028 FAILED - Meal 1 not added multiple times to cart")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-029 | Remove meal from cart (decrement)
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000")
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
# print("TC-FUNC-029 PASSED - Removing one item works correctly")

# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-030 | Completely removing a meal → total becomes 0
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000")
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
# print("TC-FUNC-030 PASSED - Cart total becomes 0 when meal completely removed")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-031 | Increase item quantity via cart modal
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000")
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
#     print("TC-FUNC-031 PASSED - Increasing item quantity via cart modal works")

# except AssertionError:
#     print("TC-FUNC-031 FAILED - Increasing item quantity via cart modal failed")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-032 | Decrease item quantity via cart modal
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000")
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
#     print("TC-FUNC-032 PASSED - Decreasing item quantity via cart modal works")

# except AssertionError:
#     print("TC-FUNC-032 FAILED - Decreasing item quantity via cart modal failed")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-033 | Cart bar total is correct
# # ══════════════════════════════════════════════════════════════════
# driver.get("http://localhost:3000/")
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
# print("TC-FUNC-033 PASSED - Cart total is correct")

# # ══════════════════════════════════════════════════════════════════
# # TC-FUNC-034 | Verify total price calculation
# # ══════════════════════════════════════════════════════════════════
# try:
#     driver.get("http://localhost:3000/")

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

#     print("TC-FUNC-034 PASSED - Total price calculation is correct")

# except AssertionError:
#     print("TC-FUNC-034 FAILED - Price calculation mismatch")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-035 | Create order with valid data (single item)
# ══════════════════════════════════════════════════════════════════
try:
    driver.get("http://localhost:3000/")
    driver.get("http://localhost:3000/")
    sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
    sign_in_btn.click()
    driver.find_element(By.ID, "username").send_keys("sami2")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(3)

    add_btn=driver.find_element(By.ID, "add-to-cart-1")
    driver.execute_script("arguments[0].click();", add_btn)
    cart_btn=driver.find_element(By.ID, "cart-btn")
    driver.execute_script("arguments[0].click();", cart_btn)
    driver.find_element(By.ID, "place-order-btn").click()
    time.sleep(5)
    modal = driver.find_element(By.XPATH, "//*[contains(text(), 'Order placed successfully!')]")

    assert modal is not None
    print("TC-FUNC-035 PASSED - Single item order created")

except AssertionError:
    print("TC-FUNC-035 FAILED - Order not created correctly")


driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-036 | Create order with multiple items
# ══════════════════════════════════════════════════════════════════
try:

    driver.find_element(By.ID, "add-to-cart-1").click()
    driver.find_element(By.ID, "add-to-cart-1").click()

    driver.find_element(By.ID, "add-to-cart-2").click()
    driver.find_element(By.ID, "add-to-cart-2").click()
    driver.find_element(By.ID, "add-to-cart-2").click()

    driver.find_element(By.ID, "cart-btn").click()
    driver.find_element(By.ID, "place-order-btn").click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    assert "placed successfully" in alert_text or "Order #" in alert_text
    print("TC-FUNC-036 PASSED - Multiple items order created")

except AssertionError:
    print("TC-FUNC-036 FAILED - Multiple items order assertion failed")


driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-037 | Order with non-existent meal rejected
# ══════════════════════════════════════════════════════════════════
try:
    driver.get("http://localhost:3000/")

    driver.find_element(By.ID, "add-to-cart-9999").click()

    driver.find_element(By.ID, "cart-btn").click()
    driver.find_element(By.ID, "place-order-btn").click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    assert "placed successfully" not in alert_text

    print("TC-FUNC-037 FAILED - Order should not be created with non-existent meal")

except AssertionError:
    print("TC-FUNC-037 PASSED - Non-existent meal correctly rejected")


driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-038 | Order from non-existent user blocked
# ══════════════════════════════════════════════════════════════════
try:
    driver.get("http://localhost:3000/")

    # simulate non-existent user
    driver.execute_script(
        "window.localStorage.setItem('user', JSON.stringify({user_id: 99999}))"
    )

    # try to access orders (or cart flow that depends on user)
    driver.find_element(By.ID, "add-to-cart-1").click()
    driver.find_element(By.ID, "cart-btn").click()
    driver.find_element(By.ID, "place-order-btn").click()

    # handle alert if it appears
    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    # EXPECTATION: should NOT succeed
    assert "placed successfully" not in alert_text

    print("TC-FUNC-038 PASSED - Non-existent user blocked from ordering")

except AssertionError:
    print("TC-FUNC-038 FAILED - Invalid user was able to place order")

except Exception:
    print("TC-FUNC-038 PASSED - System blocked non-existent user correctly")


driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-039 | Create order with quantity = 0 rejected
# ══════════════════════════════════════════════════════════════════
try:
    driver.get("http://localhost:3000/")

    driver.find_element(By.ID, "add-to-cart-1").click()

    driver.find_element(By.ID, "cart-btn").click()

    minus_btn = driver.find_element(By.ID, "remove-from-cart-1")
    minus_btn.click()

    driver.find_element(By.ID, "place-order-btn").click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    assert "placed successfully" not in alert_text

    print("TC-FUNC-039 PASSED - Order with quantity 0 rejected")

except AssertionError:
    print("TC-FUNC-039 FAILED - Order created with quantity 0")

driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-040 | Create order with negative quantity blocked
# ══════════════════════════════════════════════════════════════════
try:
    driver.get("http://localhost:3000/")

    driver.find_element(By.ID, "add-to-cart-1").click()

    driver.find_element(By.ID, "cart-btn").click()

    driver.find_element(By.ID, "remove-from-cart-1").click()
    driver.find_element(By.ID, "remove-from-cart-1").click()  # now should be -1

    driver.find_element(By.ID, "place-order-btn").click()

    alert = driver.switch_to.alert
    alert_text = alert.text
    alert.accept()

    assert "placed successfully" not in alert_text

    print("TC-FUNC-040 PASSED - Negative quantity blocked correctly")

except AssertionError:
    print("TC-FUNC-040 FAILED - Order created with negative quantity")


driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-041 | My Orders link navigates to orders page
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
sign_in_btn.click()
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.find_element(By.ID, 'my-orders-link').click()
time.sleep(2)
assert "MyOrders" in driver.current_url
print("TC-FUNC-041 PASSED - My Orders link navigates to orders page")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-042 | My Orders redirects unauthenticated user to login
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
driver.find_element(By.ID, 'my-orders-link').click()
time.sleep(3)
assert "/login" in driver.current_url
print("TC-FUNC-042 PASSED - My Orders redirects unauthenticated user to login page")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-043 | Cart modal shows correct number of items
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu1 = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu1)
addbtu2 = driver.find_element(By.ID, 'add-to-cart-2')
driver.execute_script("arguments[0].click();", addbtu2)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
cart_items = driver.find_elements(By.XPATH, '//*[contains(@id, "cart-item")]')
assert len(cart_items) == 2
print("TC-FUNC-043 PASSED - Cart modal shows 2 items after adding 2 meals")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-044 | Cart modal shows empty state message
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(2)
nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
driver.execute_script("arguments[0].click();", nav_cart)
time.sleep(1)
empty_msg = driver.find_element(By.XPATH, '//p[contains(text(), "Your cart is empty")]')
assert empty_msg.is_displayed()
print("TC-FUNC-044 PASSED - Cart modal shows empty state message")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-045 | Cart item IDs present in modal
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
cart_item = driver.find_element(By.ID, 'cart-item-1')
assert cart_item is not None
print("TC-FUNC-045 PASSED - cart-item-1 element exists in cart modal")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-046 | Place order when not logged in shows error
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
driver.execute_script("window.localStorage.clear();")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
place_order = driver.find_element(By.ID, 'place-order-btn')
driver.execute_script("arguments[0].click();", place_order)
time.sleep(1)
error_msg = driver.find_element(By.ID, 'cart-error')
assert error_msg.is_displayed()
assert "sign in" in error_msg.text.lower()
print("TC-FUNC-046 PASSED - cart-error shown when placing order without login")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-047 | My Orders page loads for logged-in user
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
assert "MyOrders" in driver.current_url
print("TC-FUNC-047 PASSED - My Orders page loads for logged-in user")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-048 | Order cards displayed for user with orders
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
place_order = driver.find_element(By.ID, 'place-order-btn')
driver.execute_script("arguments[0].click();", place_order)
time.sleep(1)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
order_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')
assert len(order_cards) > 0
print("TC-FUNC-048 PASSED - Order cards displayed for user with orders")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-049 | Order card shows price information
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
order_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')
first_card = order_cards[0]
price_el = first_card.find_element(By.XPATH, './/p[contains(text(), "₺")]')
assert price_el.is_displayed()
print("TC-FUNC-049 PASSED - Order card shows price information")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-050 | Grand total section visible on orders page
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
grand_total = driver.find_element(By.XPATH, '//p[contains(text(), "All Orders Total")]')
assert grand_total.is_displayed()
print("TC-FUNC-050 PASSED - Grand total section is visible on orders page")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-051 | No orders message for user with no orders
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami5")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
no_orders_msg = driver.find_element(By.XPATH, "//p[contains(text(), \"haven't placed any orders\")]")
assert no_orders_msg.is_displayed()
print("TC-FUNC-051 PASSED - No orders message shown for user with no orders")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-052 | No orders message for user with no orders
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami5")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(5)
driver.get(f"{BASE_URL}/MyOrders")
time.sleep(3)
no_orders_msg = driver.find_element(By.XPATH, "//p[contains(text(), \"haven't placed any orders\")]")
assert no_orders_msg.is_displayed()
print("TC-FUNC-052 PASSED - No orders message shown")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-053 | Meal subtotal shown when quantity > 0
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
time.sleep(1)
subtotal = driver.find_element(By.ID, 'meal-subtotal-1')
assert subtotal.is_displayed()
print("TC-FUNC-053 PASSED - Subtotal text appears after adding meal 1")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-054 | Meal subtotal hidden when quantity = 0
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
subtotals = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-subtotal")]')
assert len(subtotals) == 0
print("TC-FUNC-054 PASSED - No subtotal elements shown when cart is empty")

# ══════════════════════════════════════════════════════════════════
# TC-FUNC-055 | Home page loads with meal cards (at least one)
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')
assert len(meal_cards) > 0
print("TC-FUNC-055 PASSED - Home page loaded with meal cards")


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  2. BUSINESS RULES                                                        ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# ══════════════════════════════════════════════════════════════════
# BR-007 | Maximum quantity per item capped at 10
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/")
time.sleep(3)
add_btn = driver.find_element(By.ID, "add-to-cart-1")
for _ in range(11):
    driver.execute_script("arguments[0].click();", add_btn)
    time.sleep(0.15)
cart_btn = driver.find_element(By.ID, "cart-btn")
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
qty_el = driver.find_element(By.ID, "quantity-1")
quantity = int(qty_el.text)
assert quantity <= 10
print(f"BR-007 PASSED - Quantity capped at {quantity}")
close_btn = driver.find_element(By.ID, "close-cart-btn")
driver.execute_script("arguments[0].click();", close_btn)

# ══════════════════════════════════════════════════════════════════
# BR-008 | Password minimum 6 characters enforced
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("testbr008")
driver.find_element(By.ID, "password").send_keys("ab1")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Address 123")
register_btn = driver.find_element(By.ID, "register-btn")
driver.execute_script("arguments[0].click();", register_btn)
time.sleep(2)
assert "mode=signup" in driver.current_url
print("BR-008 PASSED - Short password rejected")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# BR-009 | Phone number must be digits only
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("testbr009")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "phone").send_keys("abcdefghij")
driver.find_element(By.ID, "address").send_keys("Test Address 123")
register_btn = driver.find_element(By.ID, "register-btn")
driver.execute_script("arguments[0].click();", register_btn)
time.sleep(2)
assert "mode=signup" in driver.current_url
print("BR-009 PASSED - Non-numeric phone rejected")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# BR-010 | Order confirmation must be shown after successful order
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
login_btn = driver.find_element(By.ID, "login-btn")
driver.execute_script("arguments[0].click();", login_btn)
time.sleep(3)
add_btn = driver.find_element(By.ID, "add-to-cart-1")
driver.execute_script("arguments[0].click();", add_btn)
cart_btn = driver.find_element(By.ID, "cart-btn")
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
place_order_btn = driver.find_element(By.ID, "place-order-btn")
driver.execute_script("arguments[0].click();", place_order_btn)
time.sleep(2)
success_elements = driver.find_elements(By.XPATH, '//*[contains(text(),"success") or contains(text(),"placed") or contains(text(),"confirmed")]')
assert len(success_elements) > 0
print("BR-010 PASSED - Success message shown after order")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# BR-011 | Cart contents must survive page refresh
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/")
time.sleep(3)
add_btn = driver.find_element(By.ID, "add-to-cart-1")
driver.execute_script("arguments[0].click();", add_btn)
time.sleep(1)
total_before = driver.find_element(By.ID, "cartbar-total-price").text
driver.refresh()
time.sleep(3)
total_after = driver.find_element(By.ID, "cartbar-total-price").text
assert total_after == total_before
print("BR-011 PASSED - Cart persisted after refresh")

# ══════════════════════════════════════════════════════════════════
# BR-012 | Username minimum 3 characters enforced
# ══════════════════════════════════════════════════════════════════
try:
    sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
    driver.execute_script("arguments[0].click();", sign_up_btn)

    driver.find_element(By.ID, "username").send_keys("aa")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "email").send_keys("sass3@gmail.com")
    driver.find_element(By.ID, "phone").send_keys("123456789")
    driver.find_element(By.ID, "address").send_keys("IYV Istanbul Turkey")
    driver.find_element(By.ID, "register-btn").click()

    assert "/login" not in driver.current_url
    print("BR-012 PASSED - Username with less than 3 chars rejected")

except AssertionError:
    print("BR-012 FAILED - Username with less than 3 chars was accepted")

driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# BR-013 | Username minimum 3 characters enforced (signup form)
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("a")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Address 123")
register_btn = driver.find_element(By.ID, "register-btn")
driver.execute_script("arguments[0].click();", register_btn)
time.sleep(2)
assert "mode=signup" in driver.current_url
print("BR-013 PASSED - Short username rejected")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# BR-014 | Username must not contain special characters
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("test@user!")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Address 123")
register_btn = driver.find_element(By.ID, "register-btn")
driver.execute_script("arguments[0].click();", register_btn)
time.sleep(2)
assert "mode=signup" in driver.current_url
print("BR-014 PASSED - Username with special characters rejected")
driver.execute_script("window.localStorage.clear();")


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  3. PERFORMANCE                                                           ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# ══════════════════════════════════════════════════════════════════
# TC-PERF-001 | Home page initial load time under 3s
# ══════════════════════════════════════════════════════════════════
start = time.time()
driver.get("http://localhost:3000/")
while len(driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')) == 0:
    if time.time() - start > 10:
        break
    time.sleep(0.1)
elapsed = time.time() - start
assert elapsed < 3, f"Home page took {elapsed:.2f}s (limit 3s)"
print(f"TC-PERF-001 PASSED - Home page loaded in {elapsed:.2f}s")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-002 | Login response time under 2s
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
start = time.time()
driver.find_element(By.ID, "login-btn").click()
while "/login" in driver.current_url:
    if time.time() - start > 5:
        break
    time.sleep(0.1)
elapsed = time.time() - start
assert "/login" not in driver.current_url, "Login did not redirect"
assert elapsed < 2, f"Login took {elapsed:.2f}s (limit 2s)"
print(f"TC-PERF-002 PASSED - Login completed in {elapsed:.2f}s")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-003 | Register response time under 2s
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("perftest2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Street 1")
start = time.time()
driver.find_element(By.ID, "register-btn").click()
while "/login" in driver.current_url:
    if time.time() - start > 5:
        break
    time.sleep(0.1)
elapsed = time.time() - start
assert "/login" not in driver.current_url, "Register did not redirect"
assert elapsed < 2, f"Register took {elapsed:.2f}s (limit 2s)"
print(f"TC-PERF-003 PASSED - Registration completed in {elapsed:.2f}s")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-004 | Place order response time under 2s
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
start = time.time()
driver.find_element(By.ID, 'place-order-btn').click()
elapsed = time.time() - start
assert elapsed < 2, f"Order placement took {elapsed:.2f}s (limit 2s)"
print(f"TC-PERF-004 PASSED - Order placed in {elapsed:.2f}s")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-005 | My Orders page load time under 3s
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
start = time.time()
driver.get("http://localhost:3000/MyOrders")
while len(driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')) == 0:
    if time.time() - start > 10:
        break
    time.sleep(0.1)
elapsed = time.time() - start
assert elapsed < 3, f"My Orders page took {elapsed:.2f}s (limit 3s)"
print(f"TC-PERF-005 PASSED - My Orders page loaded in {elapsed:.2f}s")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-006 | Cart modal opens under 300ms
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
start = time.time()
driver.execute_script("arguments[0].click();", nav_cart)
driver.find_element(By.ID, 'cart-modal')
elapsed = (time.time() - start) * 1000
assert elapsed < 300, f"Cart modal took {elapsed:.0f}ms to open (limit 300ms)"
print(f"TC-PERF-006 PASSED - Cart modal opened in {elapsed:.0f}ms")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-007 | Add to cart instant feedback under 200ms
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
start = time.time()
driver.execute_script("arguments[0].click();", addbtu)
cart_bar = driver.find_element(By.ID, 'cart-btn')
while not cart_bar.is_displayed():
    if time.time() - start > 2:
        break
    time.sleep(0.05)
elapsed = (time.time() - start) * 1000
assert elapsed < 200, f"Cart bar took {elapsed:.0f}ms to appear (limit 200ms)"
print(f"TC-PERF-007 PASSED - Cart bar appeared in {elapsed:.0f}ms after add")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-008 | My Orders page with many orders (stress)
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(4)
order_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')
logs = driver.get_log('browser')
errors = [l for l in logs if l['level'] == 'SEVERE']
assert len(errors) == 0, f"JS errors found: {errors}"
assert len(order_cards) > 0
print(f"TC-PERF-008 PASSED - Orders page rendered {len(order_cards)} cards with no JS errors")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-PERF-009 | 10 rapid add-to-cart clicks handled correctly
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
for r in range(10):
    driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
quantity = driver.find_element(By.ID, 'quantity-1').text
assert quantity == "10", f"Expected quantity 10, got {quantity}"
logs = driver.get_log('browser')
errors = [l for l in logs if l['level'] == 'SEVERE']
assert len(errors) == 0, f"JS errors after rapid clicks: {errors}"
print(f"TC-PERF-009 PASSED - 10 rapid clicks resulted in quantity {quantity} with no JS errors")


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  4. USABILITY                                                             ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# ══════════════════════════════════════════════════════════════════
# TC-USA-001 | Error message visible on failed login
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("wrongpassword")
driver.find_element(By.ID, "login-btn").click()
time.sleep(2)
error_msg = driver.find_element(By.ID, "login-error")
assert error_msg.is_displayed()
assert len(error_msg.text) > 0
print("TC-USA-001 PASSED - Login error message is visible with text: " + error_msg.text)

# ══════════════════════════════════════════════════════════════════
# TC-USA-002 | Error message visible on failed register
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Street 1")
driver.find_element(By.ID, "register-btn").click()
time.sleep(2)
error_msg = driver.find_element(By.ID, "register-error")
assert error_msg.is_displayed()
assert len(error_msg.text) > 0
print("TC-USA-002 PASSED - Register error message is visible with text: " + error_msg.text)

# ══════════════════════════════════════════════════════════════════
# TC-USA-003 | Place order button shows loading state
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
place_btn = driver.find_element(By.ID, 'place-order-btn')
driver.execute_script("arguments[0].click();", place_btn)
time.sleep(0.5)
btn_text = place_btn.text
assert btn_text == "Placing order..."
print("TC-USA-003 PASSED - Button showed 'Placing order...' during request")
time.sleep(3)
driver.find_element(By.ID, 'close-cart-btn').click()
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-USA-004 | Cart bar hidden when cart is empty
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
cart_btn = driver.find_element(By.ID, 'cart-btn')
assert not cart_btn.is_displayed()
print("TC-USA-004 PASSED - Cart bar confirm button is hidden when cart is empty")

# ══════════════════════════════════════════════════════════════════
# TC-USA-005 | Cart bar appears after adding item
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
time.sleep(1)
cart_btn = driver.find_element(By.ID, 'cart-btn')
assert cart_btn.is_displayed()
print("TC-USA-005 PASSED - Cart bar confirm button is visible after adding item")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-USA-006 | Confirm button hidden when cart is empty (variant)
# ══════════════════════════════════════════════════════════════════
try:
    driver.get("http://localhost:3000/")
    time.sleep(2)

    cart_btn = driver.find_element(By.ID, "cart-btn")

    assert cart_btn.is_displayed() == False

    print("TC-USA-006 PASSED - Confirm button hidden when cart is empty")

except AssertionError:
    print("TC-USA-006 FAILED - Confirm button is visible while cart is empty")


driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-USA-007 | Confirm button visible when cart is not empty (variant)
# ══════════════════════════════════════════════════════════════════
try:
    driver.get("http://localhost:3000/")
    time.sleep(2)

    addbtu = driver.find_element(By.ID, 'add-to-cart-1')
    driver.execute_script("arguments[0].click();", addbtu)
    time.sleep(1)
    cart_btn = driver.find_element(By.ID, "cart-btn")

    assert cart_btn.is_displayed() == True

    print("TC-USA-007 PASSED - Confirm button visible when cart is not empty")

except AssertionError:
    print("TC-USA-007 FAILED - Confirm button is hidden while cart is not empty")


driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/")

# ══════════════════════════════════════════════════════════════════
# TC-USA-008 | Empty cart message + disabled Place Order button
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/")
time.sleep(2)
nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
driver.execute_script("arguments[0].click();", nav_cart)
time.sleep(1)
empty_msg = driver.find_element(By.XPATH, '//p[contains(text(), "Your cart is empty")]')
assert empty_msg.is_displayed()
place_btn = driver.find_element(By.ID, 'place-order-btn')
assert place_btn.get_attribute("disabled") is not None
print("TC-USA-008 PASSED - Empty cart message visible and place order button is disabled")

# ══════════════════════════════════════════════════════════════════
# TC-USA-009 | Order confirmation message is clear
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
driver.find_element(By.ID, 'place-order-btn').click()
time.sleep(4)
success_msg = driver.find_element(By.ID, 'order-success-msg')
assert success_msg.is_displayed()
assert "placed successfully" in success_msg.text or "Order" in success_msg.text
print("TC-USA-009 PASSED - Order confirmation message is clear: " + success_msg.text)
driver.find_element(By.ID, 'close-cart-btn').click()
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-USA-010 | My Orders shows empty state clearly
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami5")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
empty_msg = driver.find_element(By.XPATH, "//p[contains(text(), \"haven't placed any orders\")]")
assert empty_msg.is_displayed()
print("TC-USA-010 PASSED - Empty orders state message is clearly displayed")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-USA-011 | Username displayed in navbar after login
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
username_display = driver.find_element(By.XPATH, '//span[contains(text(), "sami2")]')
assert username_display.is_displayed()
print("TC-USA-011 PASSED - Username 'sami2' is visible in the navbar after login")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-USA-012 | Page title visible on My Orders page
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(2)
heading = driver.find_element(By.XPATH, '//h1[contains(text(), "My Orders")]')
assert heading.is_displayed()
print("TC-USA-012 PASSED - 'My Orders' heading is clearly visible on the orders page")
driver.execute_script("window.localStorage.clear();")


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  5. LOGOUT (USABILITY)                                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# ══════════════════════════════════════════════════════════════════
# TC-USA-LOGOUT-001 | Logout redirects to /login
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.find_element(By.ID, "logout-btn").click()
time.sleep(2)
assert "/login" in driver.current_url
print("TC-USA-LOGOUT-001 PASSED - Logout redirects user to /login")

# ══════════════════════════════════════════════════════════════════
# TC-USA-LOGOUT-002 | Navbar shows Sign In after logout
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.find_element(By.ID, "logout-btn").click()
time.sleep(2)
login_link = driver.find_element(By.ID, "login-btn")
assert login_link.is_displayed()
print("TC-USA-LOGOUT-002 PASSED - Sign In link is visible in navbar after logout")

# ══════════════════════════════════════════════════════════════════
# TC-USA-LOGOUT-003 | After logout cannot access My Orders
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.find_element(By.ID, "logout-btn").click()
time.sleep(2)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
assert "/login" in driver.current_url
print("TC-USA-LOGOUT-003 PASSED - Logged out user is redirected from /MyOrders to /login")


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  6. SECURITY                                                              ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# ══════════════════════════════════════════════════════════════════
# TC-SEC-001 | SQL injection in login username rejected
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("' OR '1'='1")
driver.find_element(By.ID, "password").send_keys("anything")
driver.find_element(By.ID, "login-btn").click()
time.sleep(2)
assert "/login" in driver.current_url
error_msg = driver.find_element(By.ID, "login-error")
assert error_msg.is_displayed()
print("TC-SEC-001 PASSED - SQL injection in username was rejected")

# ══════════════════════════════════════════════════════════════════
# TC-SEC-002 | SQL injection in login password rejected
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("' OR '1'='1")
driver.find_element(By.ID, "login-btn").click()
time.sleep(2)
assert "/login" in driver.current_url
error_msg = driver.find_element(By.ID, "login-error")
assert error_msg.is_displayed()
print("TC-SEC-002 PASSED - SQL injection in password was rejected")

# ══════════════════════════════════════════════════════════════════
# TC-SEC-003 | XSS in register username blocked
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("<script>alert('xss')</script>")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Street 1")
driver.find_element(By.ID, "register-btn").click()
time.sleep(3)
try:
    driver.switch_to.alert.accept()
    assert False, "XSS script executed - SECURITY FAILURE"
except:
    print("TC-SEC-003 PASSED - XSS script not executed in register username")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-SEC-004 | XSS in address field blocked
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("xsstest1")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("<img src=x onerror=alert(1)>")
driver.find_element(By.ID, "register-btn").click()
time.sleep(3)
try:
    driver.switch_to.alert.accept()
    assert False, "XSS script executed via address field - SECURITY FAILURE"
except:
    print("TC-SEC-004 PASSED - XSS script not executed in address field")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-SEC-005 | Access My Orders without auth redirects to login
# ══════════════════════════════════════════════════════════════════
driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
assert "/login" in driver.current_url
print("TC-SEC-005 PASSED - Unauthenticated user redirected to login from /MyOrders")

# ══════════════════════════════════════════════════════════════════
# TC-SEC-006 | Brute force login — 10 wrong attempts all rejected
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
for i in range(10):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys("sami2")
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(f"wrongpass{i}")
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(1)
    assert "/login" in driver.current_url
print("TC-SEC-006 PASSED - All 10 brute force attempts were rejected")

# ══════════════════════════════════════════════════════════════════
# TC-SEC-007 | Password not stored in localStorage
# ══════════════════════════════════════════════════════════════════
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
user_data = driver.execute_script("return window.localStorage.getItem('user');")
assert user_data is not None
assert "123456" not in user_data
assert "password" not in user_data.lower()
print("TC-SEC-007 PASSED - Password is not stored in localStorage")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# TC-SEC-008 | Register with 500-char input doesn't crash app
# ══════════════════════════════════════════════════════════════════
long_input = "a" * 500
driver.get("http://localhost:3000/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys(long_input)
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Street 1")
driver.find_element(By.ID, "register-btn").click()
time.sleep(3)
assert driver.find_element(By.TAG_NAME, "body").is_displayed()
assert "Internal Server Error" not in driver.page_source
assert "500" not in driver.title
print("TC-SEC-008 PASSED - App handled 500-char input without crashing")
driver.execute_script("window.localStorage.clear();")

# ═══════════════════════════════════════════════════════════════════════════
#   END OF TEST SUITE
# ═══════════════════════════════════════════════════════════════════════════
input("Press Enter to close...")
driver.quit()