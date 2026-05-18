from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()


driver.get("http://localhost:3000/")

############################################################################ signup ##########################################################################
# # Register with existing username
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

############################################################################ signin ##########################################################################

# # Login with correct credentials
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" not in driver.current_url
# print("TC-FUNC-006 PASSED - Login with correct credentials")
# driver.execute_script("window.localStorage.clear();")


# # Login with wrong password
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("wrongpassword")
# driver.find_element(By.ID, "login-btn").click() 
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-007 PASSED - Login with wrong password rejected")
# driver.execute_script("window.localStorage.clear();")

# # Login with non-existent username
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("nonexistentuser")
# driver.find_element(By.ID, "password").send_keys("anyPassword")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-008 PASSED - Login with non-existent username rejected")
# driver.execute_script("window.localStorage.clear();") 

# # Login with empty username
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("")
# driver.find_element(By.ID, "password").send_keys("123456")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-009 PASSED - Login with empty username rejected")
# driver.execute_script("window.localStorage.clear();")

# # Login with empty password
# driver.get("http://localhost:3000/")
# sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
# sign_in_btn.click()
# driver.find_element(By.ID, "username").send_keys("sami2")
# driver.find_element(By.ID, "password").send_keys("")
# driver.find_element(By.ID, "login-btn").click()
# time.sleep(3)
# assert "/login" in driver.current_url
# print("TC-FUNC-010 PASSED - Login with empty password rejected")
# driver.execute_script("window.localStorage.clear();")

# Login with empty two fields
driver.get("http://localhost:3000/")
sign_in_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign In")]')
sign_in_btn.click()
driver.find_element(By.ID, "username").send_keys("")
driver.find_element(By.ID, "password").send_keys("")
driver.find_element(By.ID, "login-btn").click()
assert "/login" in driver.current_url
print("TC-FUNC-000 PASSED - Login with empty username and password rejected")
############################################################################ meals ##########################################################################

# # Get all meals
# driver.get("http://localhost:3000/")
# time.sleep(3)
# meal_cards = driver.find_elements(By.XPATH, '//*[contains(@id, "meal-card")]')  
# assert len(meal_cards) == 9
# print(f"TC-FUNC-010 PASSED - {len(meal_cards)} meals loaded")

# # Get meal by ID
# driver.get("http://localhost:3000")
# time.sleep(3)
# addbtu = driver.find_element(By.ID, 'add-to-cart-1')
# driver.execute_script("arguments[0].click();", addbtu)
# driver.find_element(By.ID, 'cart-btn').click()
# cart = driver.find_element(By.ID, 'cart-item-1')
# time.sleep(2)
# assert cart is not None
# print("TC-FUNC-012 PASSED - Meal details retrieved by ID")

# # Get meal by non-existent ID
# driver.get("http://localhost:8000/meals/99")
# time.sleep(2)
# assert "Not Found" in driver.page_source
# print("TC-FUNC-012 PASSED - Meal not found")

############################################################################ orders ##########################################################################


input("Press Enter to close...")  
driver.quit()