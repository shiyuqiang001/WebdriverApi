from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import selenium.webdriver.support.ui as ui
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('../html_home/wait.html')

dr.get(file_path)

sleep(3)
# 点击按钮
dr.find_element_by_id('btn').click()

wait = ui.WebDriverWait(dr, 10)
wait.until(lambda dr: dr.find_element_by_class_name('label').is_displayed())

sleep(3)
dr.quit()