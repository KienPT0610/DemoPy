from selenium import webdriver
import time
# time.sleep(3)
driver = webdriver.Chrome()
driver.set_window_size(700, 700)
driver.get('http://youtube.com/')
time.sleep(2)