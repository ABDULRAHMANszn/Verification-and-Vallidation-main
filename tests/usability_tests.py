from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://localhost:3000/")

########################################################################### login / register ##########################################################################

# # TC-USA-001 - Error Message Visible on Failed Login
# driver.get("http://localhost:3000/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("wrongpassword")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(2)
# error_msg = driver.find_element(By.ID, "login-error")
# assert error_msg.is_displayed()
# assert len(error_msg.text) > 0
# print("TC-USA-001 PASSED - Login error message is visible with text: " + error_msg.text)

# # TC-USA-002 - Error Message Visible on Failed Register
# driver.get("http://localhost:3000/login?mode=signup")
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

# ########################################################################### order ##########################################################################

# # TC-USA-005 - Place Order Button Shows Loading State
# driver.get("http://localhost:3000/login")
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
# driver.execute_script("window.localStorage.clear();")

# # TC-USA-011 - Order Confirmation Message is Clear
# driver.get("http://localhost:3000/login")
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
# driver.execute_script("window.localStorage.clear();")

# ########################################################################### cart bar ##########################################################################

# # TC-USA-006 - Cart Bar Hidden When Cart is Empty
# driver.get("http://localhost:3000/")
# time.sleep(3)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# assert not cart_btn.is_displayed()
# print("TC-USA-006 PASSED - Cart bar confirm button is hidden when cart is empty")

# # TC-USA-007 - Cart Bar Appears After Adding Item
# driver.get("http://localhost:3000/")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# time.sleep(1)
# cart_btn = driver.find_element(By.ID, 'cart-btn')
# assert cart_btn.is_displayed()
# print("TC-USA-007 PASSED - Cart bar confirm button is visible after adding item")
# driver.execute_script("window.localStorage.clear();")


# ########################################################################### cart modal ##########################################################################

# # TC-USA-010 - Empty Cart Message and Disabled Button in Modal
# driver.get("http://localhost:3000/")
# time.sleep(2)
# nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
# driver.execute_script("arguments[0].click();", nav_cart)
# time.sleep(1)
# empty_msg = driver.find_element(By.XPATH, '//p[contains(text(), "Your cart is empty")]')
# assert empty_msg.is_displayed()
# place_btn = driver.find_element(By.ID, 'place-order-btn')
# assert place_btn.get_attribute("disabled") is not None
# print("TC-USA-010 PASSED - Empty cart message visible and place order button is disabled")

# ########################################################################### my orders ##########################################################################

# # TC-USA-014 - My Orders Shows Empty State Clearly
# # NOTE: use a username that has no orders
# driver.get("http://localhost:3000/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami5")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get("http://localhost:3000/MyOrders")
# time.sleep(3)
# empty_msg = driver.find_element(By.XPATH, "//p[contains(text(), \"haven't placed any orders\")]")
# assert empty_msg.is_displayed()
# print("TC-USA-014 PASSED - Empty orders state message is clearly displayed")
# driver.execute_script("window.localStorage.clear();")

########################################################################### navbar ##########################################################################

# # TC-USA-019 - Username Displayed in Navbar After Login
# driver.get("http://localhost:3000/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# username_display = driver.find_element(By.XPATH, '//span[contains(text(), "sami2")]')
# assert username_display.is_displayed()
# print("TC-USA-019 PASSED - Username 'sami2' is visible in the navbar after login")
# driver.execute_script("window.localStorage.clear();")

# # TC-USA-020 - Page Title Visible on My Orders Page
# driver.get("http://localhost:3000/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# driver.get("http://localhost:3000/MyOrders")
# time.sleep(2)
# heading = driver.find_element(By.XPATH, '//h1[contains(text(), "My Orders")]')
# assert heading.is_displayed()
# print("TC-USA-020 PASSED - 'My Orders' heading is clearly visible on the orders page")
# driver.execute_script("window.localStorage.clear();")

############################################################################ logout ##########################################################################

# TC-USA-LOGOUT-001 - Logout Redirects to Login Page
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

# TC-USA-LOGOUT-002 - Navbar Shows Sign In After Logout
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

# TC-USA-LOGOUT-003 - After Logout Cannot Access My Orders
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

input("Press Enter to close...")
driver.quit()
