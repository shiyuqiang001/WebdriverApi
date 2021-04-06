参加gitbooks：https://wangxiwei.gitbooks.io/webdriver-python/content/12/send_keys.py.html
##driver的api
###driver.close() - 关闭当前浏览器窗口 
###driver.quit() - 关闭窗口，还会彻底的退出webdriver 
###driver.maximize_window() - 设置浏览器最大化 
###driver.set_window_size() - 设置浏览器大小,参数（长，宽） 
###driver.get() - 跳转一个界面 ，参数（url地址） 
###driver.title  - 浏览器标题 
###driver.back()  --后退 
###driver.forward() --前进 
###driver.find_element - 定位元素，定位单个 
###driver.find_elements -定位一组对象 
- 批量操作对象，比如将页面上所有的checkbox都勾上
- 先获取一组对象，再在这组对象中过滤出需要具体定位的一些对象。比如定位出页面上所有的checkbox，然后选择最后一个

##元素定位方式
###简单定位方式（8种）
- id
- name
- class name
- link text
- partial link text
- tag name
- xpath
- css selector
###层级定位方式
`页面上有很多个属性基本相同的元素，现在需要具体定位到其中的一个。由于属性基本相当，所以在定位的时候会有些麻烦，这时候就需要用到层级定位。先定位父元素，然后再通过父元素定位子孙元素。`

##模拟场景【ActionChains】

- key_down。模拟按键按下
- key_up。模拟按键弹起
- click
- send_keys
- double_click。鼠标左键双击
- click_and_hold。鼠标左键点击住不放
- release。鼠标左键弹起，可以与click_and_hold配合使用
- move_to_element。把鼠标移动到元素的中心点
- content_click。鼠标右键点击
- drag_and_drop。拖拽
````
from selenium.webdriver.common.action_chains import ActionChains
element = webdriver.find_element_by_link_text('xxxxx')
hov = ActionChains(wd).move_to_element(element)
hov.perform()
````

##element的api
###element.click() 点击对象
###element.send_keys() 在对象上模拟按键输入 
###KEY.常量  --- 模拟键盘操作

##常见的处理
###button group【按钮组】
将一组按钮排列在一起。处理这种对象的思路一般是先找到button group的包裹(wrapper)div，然后通过层级定位，用index或属性去定位更具体的按钮。 
````
buttons = dr.find_element_by_class_name('btn-group').find_elements_by_class_name('btn')
for btn in buttons:
    if btn.text == 'second': print 'find second button'
````
###button group【把按钮和下拉菜单弄到了一起】
````
driver.find_element_by_link_text('Info').click()

####找到dropdown-menu父元素
WebDriverWait(dr,10).until(lambda the_driver: the_driver.find_element_by_class_name('dropdown-menu').is_displayed())

#####找到better than
menu = dr.find_element_by_class_name('dropdown-menu').find_element_by_link_text('better than')

menu.click()
````
###navs导航栏
navs可以看作是简单的类似于tab的导航栏。一般来说导航栏都是ul+li。先定位ul再去层级定位li中的link基本就能解决问题。
````
# 方法1：层级定位，先定位ul再定位li
dr.find_element_by_class_name('nav').find_element_by_link_text('About').click()

# 方法2: 直接定位link
dr.find_element_by_link_text('Home').click()
````
###面包屑导航【breadcrumb.html】
在实际的测试脚本中，有可能需要处理面包屑。处理面包屑主要是获取其层级关系，以及获得当前的层级。一般来说当前层级都不会是链接，而父层级则基本是以链接，所以处理面包屑的思路就很明显了。找到面包屑所在的div或ul，然后再通过该div或ul找到下面的所有链接，这些链接就是父层级。最后不是链接的部分就应该是当前层级了。
````
#获得其父层级
anstors = dr.find_element_by_class_name('breadcrumb').find_elements_by_tag_name('a')
for ans in anstors:
    print(ans.text)

sleep(1)

# 获取当前层级
# 由于页面上可能有很多class为active的元素
# 所以使用层级定位最为保险

print(dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text)
````
###提示工具【attribute.html】
当您想要描述一个链接的时候，提示工具（Tooltip）就显得非常有用。\
title使用data-original-title标注
````
link = dr.find_element_by_id('tooltip')

# 获得tooltip的内容
print link.get_attribute('data-original-title')

# 获取该链接的text
print link.text

````
###css的提取验证【css.html】
当你的测试用例纠结细枝末节的时候，你就需要通过判断元素的css属性来验证你的操作是否达到了预期的效果。比如你可以通过判断页面上的标题字号以字体来验证页面的显示是否符合预期。
````
 element.value_of_css_property('color')
````
###测试对象的状态【status.html】
- 是否显示。使用element.is_displayed()方法
- 是否存在。使用find_element_by_xxx方法，捕获其抛出的异常, 如果存在异常的话则可以确定该元素不存在
- 是否被选中。一般是判断表单元素，比如radio或checkbox是否被选中。使用element.is_selected()方法
- 是否enable，也就是是否是灰化状态。使用element.is_enabled()方法；
###表单处理【from.html】

- 使用send_keys方法往多行文本框和单行文本框赋值；
- 使用click方法选择checkbox
- 使用click方法选择radio
- 使用click方法点击button
- 使用click方法选择option，从而达到选中select下拉框中某个具体菜单项的效果
```
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
```
###对js的操作【js.html】
- 在页面直接执行一段js
- 在某个已经定位的元素的上执行js
````
# 在页面上直接执行js
js= 'alert("要开始隐藏元素了")'
dr.execute_script(js)
sleep(2)
dr.switch_to.alert.accept()
sleep(2)
#隐藏
dr.execute_script('$("#tooltip").fadeOut();')
sleep(2)

# 在已经定位的元素上执行js
button = dr.find_element_by_class_name('btn')
sleep(2)
dr.execute_script('$(arguments[0]).fadeOut()', button)

````
###处理alert/confirm/prompt 
webdriver中处理原生的js alert confirm 以及prompt是很简单的。具体思路是使用switch_to.alert()方法定位到alert/confirm/prompt。然后使用text/accept/dismiss/send_keys按需进行操做
- text()返回alert/confirm/prompt中的文字信息
- accept()点击确认按钮
- dismiss()点击取消按钮，如果有的话
- send_keys()向prompt中输入文字

###定位frame中的元素【frame.html】
处理frame需要用到2个方法，分别是switch_to_frame(name_or_id_or_frame_element)和switch_to_default_content()\
- switch_to_frame方法把当前定位的主体切换了frame里。
- witch_to_default_content方法的话则是从frame中嵌入的页面里跳出，跳回到最外面的原始页面中。
````
# 先到f1再到f2
dr.switch_to_frame('f1')
dr.switch_to_frame('f2')

# 往f2中的百度关键字文本框中输入内容
dr.find_element_by_id('kw').send_keys('watir-webdriver')

# 直接跳出所有frame
dr.switch_to_default_content()

# 再到f1
dr.switch_to_frame('f1')
dr.find_element_by_link_text('click').click()
````
###上传文件【upload_file】
上传文件的方法是找到上传文件的对象，通常是的对象。然后直接往这个对象send_keys，传入需要上传文件的正确路径。绝对路径和相对路径都可以，但是上传的文件必须存在，否则会报错。
`````
##send_key填写需要上传文件的路径
###方式一：比较简单
dr.find_element_by_name('file').send_keys(os.getcwd()+'\css.py')

###方式二：比较复杂，可以满足只读类型的上传文件AutoIT
##参考：https://blog.csdn.net/qq_35451939/article/details/83029946
`````
###下载
````
import os

from selenium import webdriver

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

browser = webdriver.Firefox(firefox_profile=fp)
browser.get("http://pypi.python.org/pypi/selenium")
browser.find_element_by_partial_link_text("selenium-2").click()
````