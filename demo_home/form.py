from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('../html_home/form.html')
dr.get(file_path)

# 选中checkbox
dr.find_element_by_css_selector('input[type=checkbox]').click()
sleep(1)

# 选中radio
dr.find_element_by_css_selector('input[type=radio]').click()
sleep(1)

# 选择下拉菜单中的最后一项
dr.find_element_by_tag_name('select').find_elements_by_tag_name('option')[-1].click()
sleep(1)

# 点击提交按钮
dr.find_element_by_css_selector('input[type=submit]').click()
sleep(5)

####switch_to_alert()被废除，现在编写如下：switch_to.alert
alert = dr.switch_to.alert
print (alert.text)
alert.accept()

dr.quit()

