from itertools import product
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "C:/Users/Gnanam/Downloads/w&ip/selenium/chromedriver.exe"
service = Service(executable_path= chrome_driver_path)
driver = webdriver.Chrome(service= service)
driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie_id = 'bigCookie'
cookie_text_id = 'cookies'
product_price_prefix = 'productPrice'
product_prefix = 'productName'

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="langSelect-EN"]'))
)

language = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
language.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookie_count = driver.find_element(By.ID, cookie_text_id).text.split(' ')[0]
    cookie_count = int(cookie_count.replace(',', ''))
    
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(',', '')
        if not product_price.isdigit():
            continue
        product_price = int(product_price)
        
        if cookie_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            # product.click()
            try:
                product.click()
            except:
                    # If click is intercepted, use JavaScript to click as a fallback
                driver.execute_script("arguments[0].click();", product)
            break
    