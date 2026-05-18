from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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
try:
    driver.get("http://localhost:3000/login")

    signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//h1[contains(text(),"Sign Up")]'))).click()
    
    create_account_text = driver.find_element(By.XPATH, '//p[contains(text(), "Create Account")]')

    assert "/login" not in driver.current_url
    print("TC-003 PASSED - navigating rejected")

except AssertionError:
    print("TC-003 FAILED - navigating accepted")





# #########################################
# # Meals
# #########################################


# ##########################################################
# # Orders Testing
# ##########################################################

# # TC-FUNC-015 — Create order with valid data
# try:
#     open_signup()

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
#     open_signup()

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
#     open_signup()

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
#     open_signup()

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
#     open_signup()

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
#     open_signup()

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