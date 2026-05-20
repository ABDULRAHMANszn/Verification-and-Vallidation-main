from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()


########################################################################### home page ##########################################################################

# Home Page Loads with Meals
driver.get("http://localhost:3000/")
time.sleep(3)
meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')
assert len(meal_cards) > 0
print("TC-FUNC-061 PASSED - Home page loaded with meal cards")

########################################################################### meal cards ##########################################################################

# Meal Subtotal Shown When Qty > 0
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
time.sleep(1)
subtotal = driver.find_element(By.ID, 'meal-subtotal-1')
assert subtotal.is_displayed()
print("TC-FUNC-059 PASSED - Subtotal text appears after adding meal 1")

# Meal Subtotal Hidden When Qty = 0
driver.get("http://localhost:3000/")
time.sleep(3)
subtotals = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-subtotal")]')
assert len(subtotals) == 0
print("TC-FUNC-060 PASSED - No subtotal elements shown when cart is empty")

########################################################################### cart modal ##########################################################################

# Cart Modal Shows Empty State Message
driver.get("http://localhost:3000/")
time.sleep(2)
nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
driver.execute_script("arguments[0].click();", nav_cart)
time.sleep(1)
empty_msg = driver.find_element(By.XPATH, '//p[contains(text(), "Your cart is empty")]')
assert empty_msg.is_displayed()
print("TC-FUNC-038 PASSED - Cart modal shows empty state message")

# Cart Modal Shows Correct Number of Items
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
print("TC-FUNC-037 PASSED - Cart modal shows 2 items after adding 2 meals")

# Cart Item IDs Present in Modal
driver.get("http://localhost:3000/")
time.sleep(3)
addbtu = driver.find_element(By.ID, 'add-to-cart-1')
driver.execute_script("arguments[0].click();", addbtu)
cart_btn = driver.find_element(By.ID, 'cart-btn')
driver.execute_script("arguments[0].click();", cart_btn)
time.sleep(1)
cart_item = driver.find_element(By.ID, 'cart-item-1')
assert cart_item is not None
print("TC-FUNC-043 PASSED - cart-item-1 element exists in cart modal")

# Place Order When Not Logged In Shows Error
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

########################################################################### my orders ##########################################################################

# View My Orders Page
driver.get("http://localhost:3000/login")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "login-btn").click()
time.sleep(3)
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
assert "MyOrders" in driver.current_url
print("TC-FUNC-049 PASSED - My Orders page loads for logged-in user")
driver.execute_script("window.localStorage.clear();")

# Order Cards Present in DOM
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
print("TC-FUNC-050 PASSED - Order cards displayed for user with orders")
driver.execute_script("window.localStorage.clear();")

# Order Card Shows Title and Price
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
print("TC-FUNC-051 PASSED - Order card shows price information")
driver.execute_script("window.localStorage.clear();")

# Grand Total Section Visible on Orders Page
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
print("TC-FUNC-052 PASSED - Grand total section is visible on orders page")
driver.execute_script("window.localStorage.clear();")

# No Orders Message for User With No Orders
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
print("TC-FUNC-053 PASSED - No orders message shown for user with no orders")
driver.execute_script("window.localStorage.clear();")


input("Press Enter to close...")
driver.quit()
