from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://localhost:3000/")


def open_signup():
    sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
    driver.execute_script("arguments[0].click();", sign_up_btn)

#################################
# Registeration
#################################


# Registration with empty username
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
#     print("TC-003 PASSED - Username with empty username accepted")

# except AssertionError:
#     print("TC-003 FAILED - Username with less than 3 chars was accepted")

# driver.get("http://localhost:3000/")


# # Registration with empty phone
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
#     print("TC-003 PASSED - Username with empty username accepted")

# except AssertionError:
#     print("TC-003 FAILED - Username with less than 3 chars was accepted")

# driver.get("http://localhost:3000/")

# # Registration with empty address
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
#     print("TC-003 PASSED - Username with empty username accepted")

# except AssertionError:
#     print("TC-003 FAILED - Username with less than 3 chars was accepted")

# driver.get("http://localhost:3000/")

# TC-003 Username with less than 3 chars
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

# driver.get("http://localhost:3000/")


# # TC-004 Empty password
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

# driver.get("http://localhost:3000/")


# # TC-005 Empty phone
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

# driver.get("http://localhost:3000/")


# # TC-006 Special characters username
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


# driver.quit()


# # TC-006 Special characters username
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


# driver.quit()


# #########################################
# # Login
# #########################################

# navigate from sign in to sign up page
# try:
#     driver.get("http://localhost:3000/login") 
#     time.sleep(3)
#     print(driver.current_url)

#     signup_button = driver.find_element(By.ID,'toggle-login-btn')
#     driver.execute_script("arguments[0].click();", signup_button)
#     time.sleep(2)
#     assert "/login?mode=signup" not in driver.current_url
#     print("TC-003 PASSED - navigating rejected")

# except AssertionError:
#     print("TC-003 FAILED - navigating accepted")



# navigation from registration to login
# try:
#     driver.get("http://localhost:3000/login?mode=signup") 
#     time.sleep(3)
#     print(driver.current_url)

#     signup_button = driver.find_element(By.ID,'toggle-login-btn')
#     driver.execute_script("arguments[0].click();", signup_button)
#     time.sleep(2)
#     assert "/login" not in driver.current_url
#     print("TC-003 PASSED - navigating rejected")

# except AssertionError:
#     print("TC-003 FAILED - navigating accepted")
    
    
# Login and then Logout
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
#     print("0000 - logout successfully")

# except AssertionError:
#     print("0000 - logout failed")



# #########################################
# # Meals
# #########################################

# Add meal to cart
# try:
#     driver.get("http://localhost:3000")
#     time.sleep(2)
#     meal1 = driver.find_element(By.ID, 'add-to-cart-1')
#     driver.execute_script("arguments[0].click();", meal1)
#     time.sleep(1)
#     cart = driver.find_element(By.ID, "cart-btn").click()
#     time.sleep(1)
#     total = driver.find_element(By.ID, "cart-total-price").text
#     price = int(total.replace("₺",""))

#     assert price == 120
#     print("00000 - Meal 1 added to cart")
# except AssertionError:
#     print("00000 - Meal 1 not added to cart")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")
# driver.quit()


# Add same meal multiple times to cart
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
#     price = int(total.replace("₺",""))

#     assert price == 360
#     print("00000 - Meal 1 added multiple times to cart")
# except AssertionError:
#     print("00000 - Meal 1 not added multiple times to cart")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")
# driver.quit()



# Removeing meal from a cart
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
# price = int(total.replace("₺",""))

# assert price == 480
# print("00000 - Removing one item correctly")

# driver.quit()


# Confirm button hidden when cart is empty
# try:
#     driver.get("http://localhost:3000/")
#     time.sleep(2)

#     cart_btn = driver.find_element(By.ID, "cart-btn")

#     assert cart_btn.is_displayed() == False

#     print("000000000 PASSED - Confirm button hidden when cart is empty")

# except AssertionError:
#     print("00000000000 FAILED - Confirm button is visible while cart is empty")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")


# Confirm button visible when cart is not empty
# try:
#     driver.get("http://localhost:3000/")
#     time.sleep(2)

#     addbtu = driver.find_element(By.ID, 'add-to-cart-1')
#     driver.execute_script("arguments[0].click();", addbtu)
#     time.sleep(1)
#     cart_btn = driver.find_element(By.ID, "cart-btn")

#     assert cart_btn.is_displayed() == True

#     print("000000000 PASSED - Confirm button visible when cart is not empty")

# except AssertionError:
#     print("00000000000 FAILED - Confirm button is visible while cart is not empty")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# Open cart via nav button
# try:
#     driver.get("http://localhost:3000")
#     time.sleep(1)

#     openCart = driver.find_element(By.ID, 'nav-cart-btn')
#     driver.execute_script("arguments[0].click();", openCart)
#     time.sleep(1)
#     cart_btn = driver.find_element(By.ID, "cart-btn")

#     assert cart_btn.is_displayed() == True

#     print("000000000 PASSED - Cart model is opened via button in nav")

# except AssertionError:
#     print("00000000000 FAILED - Cart model is not opened via button in nav")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")



# Open cart via nav button
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
#     price = int(total.replace("₺",""))

#     assert price == 300
#     print("000000000 PASSED - Increasing item quantity via cart modal is successful")

# except AssertionError:
#     print("00000000000 FAILED - Cart model is not opened via button in nav")


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
#     price = int(total.replace("₺",""))

#     assert price == 100
#     print("000000000 PASSED - Decreasing item quantity via cart modal is successful")

# except AssertionError:
#     print("00000000000 FAILED - Decreasing item quantity via cart modal is not successful")



# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")


# ##########################################################
# # Orders Testing
# ##########################################################

# # TC-FUNC-015 — Create order with valid data
# try:
#     driver.get("http://localhost:3000/")

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


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")


# # TC-FUNC-016 — Create order with non-existent meal
# try:
#     driver.get("http://localhost:3000/")

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


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")


# # TC-FUNC-017 - Create order with multiple items
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


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")


# # TC-FUNC-019 — Get orders for non-existent user
# try:
#     driver.get("http://localhost:3000/")

#     # simulate non-existent user
#     driver.execute_script(
#         "window.localStorage.setItem('user', JSON.stringify({user_id: 99999}))"
#     )

#     # try to access orders (or cart flow that depends on user)
#     driver.find_element(By.ID, "add-to-cart-1").click()
#     driver.find_element(By.ID, "cart-btn").click()
#     driver.find_element(By.ID, "place-order-btn").click()

#     # handle alert if it appears
#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()

#     # EXPECTATION: should NOT succeed
#     assert "placed successfully" not in alert_text

#     print("TC-FUNC-019 PASSED - Non-existent user blocked from ordering")

# except AssertionError:
#     print("TC-FUNC-019 FAILED - Invalid user was able to place order")

# except Exception:
#     print("TC-FUNC-019 PASSED - System blocked non-existent user correctly")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# # TC-FUNC-020 — Create order with quantity = 0
# try:
#     driver.get("http://localhost:3000/")

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

# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")



# # TC-FUNC-021 — Create order with negative quantity
# try:
#     driver.get("http://localhost:3000/")

#     driver.find_element(By.ID, "add-to-cart-1").click()

#     driver.find_element(By.ID, "cart-btn").click()

#     driver.find_element(By.ID, "remove-from-cart-1").click()
#     driver.find_element(By.ID, "remove-from-cart-1").click() # now should be -1

#     driver.find_element(By.ID, "place-order-btn").click()

#     alert = driver.switch_to.alert
#     alert_text = alert.text
#     alert.accept()

#     assert "placed successfully" not in alert_text

#     print("TC-FUNC-021 PASSED - Negative quantity blocked correctly")

# except AssertionError:
#     print("TC-FUNC-021 FAILED - Order created with negative quantity")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")

# # TC-FUNC-024 — Verify total price calculation
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

#     print("TC-FUNC-024 PASSED - Total price calculation is correct")

# except AssertionError:
#     print("TC-FUNC-024 FAILED - Price calculation mismatch")


# driver.execute_script("window.localStorage.clear();")
# driver.get("http://localhost:3000/")


# Completely removing a meal
# driver.get("http://localhost:3000")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# driver.execute_script("arguments[0].click();", addbtu)
# driver.find_element(By.ID, 'cart-btn').click()
# emovebut =driver.find_element(By.ID, 'decrease-1')
# driver.execute_script("arguments[0].click();", emovebut)
# driver.execute_script("arguments[0].click();", emovebut)

# time.sleep(2)

# total = driver.find_element(By.ID, "cart-total-price").text
# price = int(total.replace("₺",""))

# assert price == 0
# print("00000 - completely removed correctly")

# driver.quit()

