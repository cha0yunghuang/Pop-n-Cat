import config
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Explicit-Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(config.chromeDriver)
# direct to...
driver.get('https://popcat.click/')

# select item
cat = driver.find_element_by_xpath('//*[@id="app"]/div')

# explicit-wait for the cat appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div'))
)

actions = ActionChains(driver)

for i in range(10000):
    actions.click(cat).perform()  # single-click
    actions.double_click(cat).perform()  # double-click

driver.close()
    