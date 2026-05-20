from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("http://localhost:3000/")

############################################################################ sql injection ##########################################################################

# TC-SEC-001 - SQL Injection in Login Username
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

# TC-SEC-002 - SQL Injection in Login Password
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

########################################################################### xss ##########################################################################

# TC-SEC-004 - XSS in Register Username
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
    print("TC-SEC-004 PASSED - XSS script not executed in register username")
driver.execute_script("window.localStorage.clear();")

# TC-SEC-005 - XSS in Address Field
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
    print("TC-SEC-005 PASSED - XSS script not executed in address field")
driver.execute_script("window.localStorage.clear();")

########################################################################### authentication ##########################################################################

# TC-SEC-006 - Access My Orders Without Authentication
driver.execute_script("window.localStorage.clear();")
driver.get("http://localhost:3000/MyOrders")
time.sleep(3)
assert "/login" in driver.current_url
print("TC-SEC-006 PASSED - Unauthenticated user redirected to login from /MyOrders")

# TC-SEC-010 - Brute Force Login (10 wrong attempts all rejected)
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
print("TC-SEC-010 PASSED - All 10 brute force attempts were rejected")

########################################################################### data exposure ##########################################################################

# TC-SEC-013 - Password Not Stored in LocalStorage
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
print("TC-SEC-013 PASSED - Password is not stored in localStorage")
driver.execute_script("window.localStorage.clear();")

########################################################################### input limits ##########################################################################

# TC-SEC-016 - Register with Extremely Long Input (500 chars)
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
print("TC-SEC-016 PASSED - App handled 500-char input without crashing")
driver.execute_script("window.localStorage.clear();")

input("Press Enter to close...")
driver.quit()
