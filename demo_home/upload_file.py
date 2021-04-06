from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
if 'HTTP_PROXY'in os.environ: del os.environ['HTTP_PROXY']

dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('../html_home/upload_file.html')

dr.get(file_path)
print(os.getcwd())
##send_key填写需要上传文件的路径
###方式一：比较简单
dr.find_element_by_name('file').send_keys(os.getcwd()+'\css.py')

###方式二：比较复杂，可以满足只读类型的上传文件AutoIT
##参考：https://blog.csdn.net/qq_35451939/article/details/83029946

sleep(2)
dr.quit()