from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()


driver.get("http://localhost:3000/")


# Register with existing username
sign_up_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Sign Up")]')
driver.execute_script("arguments[0].click();", sign_up_btn)
driver.find_element(By.ID, "username").send_keys("sami2")
driver.find_element(By.ID, "password").send_keys("123456")
driver.find_element(By.ID, "email").send_keys("sass@gmail.com")
driver.find_element(By.ID, "phone").send_keys("1234567890")
driver.find_element(By.ID, "address").send_keys("123 Main St")
driver.find_element(By.ID, "register-btn").click()
assert "/login" in driver.current_url
print("TC-FUNC-002 PASSED - Duplicate username rejected")

input("Press Enter to close...")  # ← browser stays open until you press Enter
driver.quit()