
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