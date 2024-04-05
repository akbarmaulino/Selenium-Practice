from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    options=options, service=Service(ChromeDriverManager().install())
)
driver.maximize_window()
driver.get("https://www.tokopedia.com/")

# Locator Find Element
# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")

#find Button masuk
# driver.find_element(By.CLASS_NAME, "css-16r70d4").click()
# driver.implicitly_wait(5)

#find Send keys for username and password
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div/div/input").send_keys("Goodluch")


driver.find_element.send_keys(Keys.ENTER)


# driver.find_element(By.CLASS_NAME, "//input[@placeholder='Cari di Tokopedia']").click()