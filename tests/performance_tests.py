from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://localhost:3000/")

############################################################################ page load ##########################################################################

# # TC-PERF-001 - Home Page Initial Load Time
# start = time.time()
# driver.get("http://localhost:3000/")
# while len(driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')) == 0:
#     if time.time() - start > 10:
#         break
#     time.sleep(0.1)
# elapsed = time.time() - start
# assert elapsed < 3, f"Home page took {elapsed:.2f}s (limit 3s)"
# print(f"TC-PERF-001 PASSED - Home page loaded in {elapsed:.2f}s")



# # TC-PERF-006 - My Orders Page Load Time
# driver.get("http://localhost:3000/login")
# time.sleep(2)
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# start = time.time()
# driver.get("http://localhost:3000/MyOrders")
# while len(driver.find_elements(By.XPATH, '//*[contains(@id, "order-card")]')) == 0:
#     if time.time() - start > 10:
#         break
#     time.sleep(0.1)
# elapsed = time.time() - start
# assert elapsed < 3, f"My Orders page took {elapsed:.2f}s (limit 3s)"
# print(f"TC-PERF-006 PASSED - My Orders page loaded in {elapsed:.2f}s")
# driver.execute_script("window.localStorage.clear();")

# ########################################################################### auth ##########################################################################

# # TC-PERF-003 - Login Response Time
# driver.get("http://localhost:3000/login")
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
# driver.execute_script("window.localStorage.clear();")

# # TC-PERF-004 - Register Response Time
# driver.get("http://localhost:3000/login?mode=signup")
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
# driver.execute_script("window.localStorage.clear();")

# ########################################################################### cart ##########################################################################

# # TC-PERF-007 - Cart Modal Opens Instantly
# driver.get("http://localhost:3000/")
# time.sleep(3)
# nav_cart = driver.find_element(By.ID, 'nav-cart-btn')
# start = time.time()
# driver.execute_script("arguments[0].click();", nav_cart)
# driver.find_element(By.ID, 'cart-modal')
# elapsed = (time.time() - start) * 1000
# assert elapsed < 300, f"Cart modal took {elapsed:.0f}ms to open (limit 300ms)"
# print(f"TC-PERF-007 PASSED - Cart modal opened in {elapsed:.0f}ms")

# # TC-PERF-008 - Add to Cart Instant Feedback
# driver.get("http://localhost:3000/")
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

########################################################################### order ##########################################################################

# TC-PERF-005 - Place Order Response Time
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
print(f"TC-PERF-005 PASSED - Order placed in {elapsed:.2f}s")
driver.execute_script("window.localStorage.clear();")

########################################################################### stress ##########################################################################

# TC-PERF-010 - My Orders Page with Many Orders
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
print(f"TC-PERF-010 PASSED - Orders page rendered {len(order_cards)} cards with no JS errors")
driver.execute_script("window.localStorage.clear();")

# TC-PERF-011 - Simultaneous Cart Operations (10 rapid clicks)
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
print(f"TC-PERF-011 PASSED - 10 rapid clicks resulted in quantity {quantity} with no JS errors")


