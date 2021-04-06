'''
导航相关api
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Naviga(object):

    '''
    ##查找元素、输入、键盘按键、清除输入、后退、前进
        查找元素：find_element_by_*()   *表示8种查找元素方式的任何一种
        输入：send_keys()
        键盘按键：Keys
        driver.back() 后退
        driver.forward()  ##前进
    '''
    def findElement(self):
        element=driver.find_element_by_id('kw')
        element.send_keys('selenium')
        element.send_keys(" and some", Keys.ENTER)
        element.clear()
    '''
    ###下拉选择框
    '''
    def setSelected(self):
        from selenium.webdriver.support.ui import Select
        select = Select(driver.find_element_by_name('jumpMenu'))
        #选中下拉框的值方式一
        #select.select_by_index(1)
        #选中下拉框的值式二
        #select.select_by_visible_text("DIVCSS5")

        ##取消选中的下拉框
        #select.deselect_all()

        options  =[]
        options= select.options
        print(options)
        ##
        ##老黄历
        # element = driver.find_element_by_id("jumpMenu" )
        # all_options = element.find_elements_by_xpath("//*[@id='jumpMenu']/option[1]")
        # for option in all_options:
        #     print(option.get_attribute("value"))
    '''
    拖拽、弹出框处理
    '''
    def Drag(self,source,target):
        from selenium.webdriver import ActionChains
        import time
        ##拖拽
        actions = ActionChains(driver)
        actions.drag_and_drop(source, target)
        actions.perform()

        ##弹出对话框
        alert = driver.switch_to.alert
        print(alert)
        time.sleep(3)
        alert.dismiss()
        time.sleep(5)

    '''
    cookies设置
    '''
    def Cookies(self):
        # Go to the correct domain
        driver.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 设置界面cookies
        cookie = {'name': 'foo', 'value': 'bar'}
        driver.add_cookie(cookie)
        #读取界面的Cookies
        driver.get_cookies()
        print(driver.get_cookies())
        print("title of current page is %s" % (driver.title))
        print("url of current page is %s" % (driver.current_url))

    '''
      超时验证
    '''
    def  Time_Out(self):
        driver.implicitly_wait(10)  # seconds
        driver.get("http://www.divcss5.com/fanli/form-select.htm")
        myDynamicElement = driver.find_element_by_id("myDynamicElement")


if __name__ == '__main__':
    driver = webdriver.Firefox()
    '''
    findElement(self)
    '''
    # driver.get('http://www.baidu.com')   ##跳转URL地址
    # Naviga().findElement() ##查找元素、输入、键盘按键、清除输入
    # sleep(3)
    # driver.back()  ##后退
    # sleep(3)
    # driver.forward()  ##前进

    '''
    setSelected(self)
    '''
    # driver.get('http://www.divcss5.com/fanli/form-select.html')
    # Naviga().setSelected()

    '''
    Drag(self)
    '''
    # driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    # driver.maximize_window()
    # driver.switch_to.frame('iframeResult')
    # source = driver.find_element_by_id('draggable')
    # target = driver.find_element_by_id('droppable')
    # Naviga().Drag(source,target)

    '''
    Cookies(self)
    '''
    #Naviga().Cookies()

    '''
    Time_Out(self) 
    '''
    Naviga().Time_Out()
