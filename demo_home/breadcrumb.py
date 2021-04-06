from selenium import  webdriver
from time import sleep
import  os


dr = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('../html_home/breadcrumb.html')
dr.get(file_path)

#获得其父层级
anstors = dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a')
for ans in anstors:
    print(ans.text)

print('父级执行完成')
sleep(1)

# 获取当前层级
# 由于页面上可能有很多class为active的元素
# 所以使用层级定位最为保险

print(dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text)

dr.quit()