"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

driver.back()
driver.forward()
driver.refresh()

#Finding Elements
#element = driver.find_element(By.ID, "content")
element = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a')

#wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'content')))
element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ul/li[1]/a')))


#Interactions
element.click()
element.send_keys("Mohamed Riyaz")
element.clear()

#screenshots
driver.save_screenshot("screenshot.png")"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
import time
import os

# ----- SETUP -----
# Make sure chromedriver is in your PATH
service = Service()
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()

    # 1. Checkboxes
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    print("Checking all checkboxes...")
    for box in checkboxes:
        if not box.is_selected():
            box.click()
    time.sleep(1)

    print("Unchecking all checkboxes...")
    for box in checkboxes:
        if box.is_selected():
            box.click()
    time.sleep(1)

    # 2. Dropdown
    driver.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = Select(driver.find_element(By.ID, "dropdown"))
    dropdown.select_by_visible_text("Option 2")
    time.sleep(1)
    selected_option = dropdown.first_selected_option.text
    print(f"Dropdown selection: {selected_option}")

    # 3. JavaScript Alerts
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = Alert(driver)
    print(f"Alert text: {alert.text}")
    alert.accept()
    time.sleep(1)

    # 4. Dynamic Content
    driver.get("https://the-internet.herokuapp.com/dynamic_content")
    initial_text = driver.find_element(By.CSS_SELECTOR, "#content .row:nth-child(1) .large-10").text
    print(f"Initial dynamic text: {initial_text}")
    driver.refresh()
    time.sleep(2)
    new_text = driver.find_element(By.CSS_SELECTOR, "#content .row:nth-child(1) .large-10").text
    print(f"New dynamic text: {new_text}")

    if initial_text != new_text:
        print("Dynamic content has changed after refresh!")
    else:
        print("Dynamic content has NOT changed after refresh.")

    # 5. File Upload
    driver.get("https://the-internet.herokuapp.com/upload")
    
    # Create a temporary file to upload
    test_file_path = os.path.join(os.getcwd(), "test_file.txt")
    with open(test_file_path, "w") as f:
        f.write("This is a test file for Selenium upload.")

    upload_input = driver.find_element(By.ID, "file-upload")
    upload_input.send_keys(test_file_path)
    driver.find_element(By.ID, "file-submit").click()

    uploaded_text = driver.find_element(By.ID, "uploaded-files").text
    print(f"Uploaded file: {uploaded_text}")

finally:
    time.sleep(3)
    driver.quit()

