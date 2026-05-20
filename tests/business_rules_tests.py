from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import requests

BASE_URL = "http://localhost:3000"

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()



# ══════════════════════════════════════════════════════════════════
# BR-007 | Maximum Quantity Per Item (max 10)
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
# BR-008 | Password Minimum Length (min 6 characters)
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
print(" BR-008 PASSED - Short password rejected")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# BR-009 | Phone Number Must Be Digits Only
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
print(" BR-009 PASSED - Non-numeric phone rejected")
driver.execute_script("window.localStorage.clear();")

# ══════════════════════════════════════════════════════════════════
# BR-010 | Order Confirmation Must Be Shown After Successful Order
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
# BR-011 | Cart Contents Must Survive Page Refresh
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
# BR-012 | Username Minimum Length (min 3 characters)
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
print("BR-012 PASSED - Short username rejected")
driver.execute_script("window.localStorage.clear();")


# ══════════════════════════════════════════════════════════════════
# BR-013 | Username Must Not Contain Special Characters
# Bug:    No regex validation on username — "@user!" is accepted.
# Expect: Error shown and user stays on signup page
# ══════════════════════════════════════════════════════════════════
driver.get(f"{BASE_URL}/login?mode=signup")
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("test@user!")   # special chars
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.ID, "phone").send_keys("0501234567")
driver.find_element(By.ID, "address").send_keys("Test Address 123")
register_btn = driver.find_element(By.ID, "register-btn")
driver.execute_script("arguments[0].click();", register_btn)
time.sleep(2)
assert "mode=signup" in driver.current_url
print("BR-013 PASSED - Username with special characters rejected")
driver.execute_script("window.localStorage.clear();")


# ══════════════════════════════════════════════════════════════════
  # No Orders Message
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
print("TC-FUNC-053 PASSED - No orders message shown")
driver.execute_script("window.localStorage.clear();")

input("Press Enter to close...")
driver.quit()