from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('../html_home/css.html')

dr.get(file_path)

link = dr.find_element_by_id('tooltip')
#获取css的颜色
color= link.value_of_css_property('color')
print (color)
#获取css的字体
font=dr.find_element_by_tag_name('h3').value_of_css_property('font-size')
print (font)

dr.quit()