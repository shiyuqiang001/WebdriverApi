from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('../html_home/js.html')
dr.get(file_path)

# 在页面上直接执行js
js= 'alert("要开始隐藏元素了")'
dr.execute_script(js)
sleep(2)
dr.switch_to.alert.accept()
sleep(2)

dr.execute_script('$("#tooltip").fadeOut();')
sleep(2)

# 在已经定位的元素上执行js
button = dr.find_element_by_class_name('btn')
sleep(2)
dr.execute_script('$(arguments[0]).fadeOut()', button)

dr.quit()