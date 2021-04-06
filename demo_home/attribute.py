from selenium import webdriver
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('../html_home/attribute.html')

dr.get(file_path)

link = dr.find_element_by_id('tooltip')

link.click()

sleep(1)
# 获得tooltip的内容使用get_attribute(),title使用data-original-title标注
res=link.get_attribute('data-original-title')
print (res)

sleep(1)
# 获取该链接的text
print (link.text)

dr.quit()