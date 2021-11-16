"""
@author:86152
@file:京东.py
@time:2021/11/15
"""

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r'https://www.jd.com')

driver.maximize_window()

# 搜索框输入内容
driver.find_element('xpath',"//*[@id='key']").send_keys("机械键盘")
# 点击搜索
driver.find_element('xpath',"//*[@clstag='h|keycount|head|search_a']").click()
time.sleep(2)

# 选择一个商品
driver.find_element('xpath',"/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img").click()
time.sleep(2)
# 换窗口
driver.switch_to.window(driver.window_handles[1])
# 点击加入购物车
driver.find_element('xpath',"//*[@id='InitCartUrl']").click()

driver.find_element('xpath',"/html/body/div[2]/div[2]/div[1]/div/div[3]/a").click()

driver.find_element('xpath',"//*[@id='loginname']").send_keys("15286950262")

driver.find_element('xpath',"//*[@id='nloginpwd']").send_keys("")

driver.find_element('xpath',"//*[@id='loginsubmit']").click()

time.sleep(3)
driver.quit()

"""
@author:86152
@file:苏宁.py
@time:2021/11/15
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get(r'https://www.suning.com')

driver.maximize_window()

driver.find_element('xpath',"//*[@id='searchKeywords']").send_keys("平板")

driver.find_element('xpath',"//*[@id='searchSubmit']").click()

time.sleep(2)
driver.find_element('xpath',"/html/body/div[10]/div/ul/li[7]/div/div/div[1]/div/a/img").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.find_element('xpath',"//*[@id='addCart']").click()


"""
@author:86152
@file:b站.py
@time:2021/11/15
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r'https://www.bilibili.com')

driver.maximize_window()

driver.find_element('xpath',"//*[@autocomplete='off']").send_keys("自来也")

time.sleep(2)
driver.find_element('xpath',"//*[@class='nav-search-btn nav-search-btn-exper nav-search-btn-exper3 nav-search-btn-exper4 nav-search-btn-exper4-hover']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element('xpath',"/html/body/div[3]/div/div[2]/div/div[1]/div[2]/ul/li[2]/a").click()

time.sleep(2)
driver.find_element('xpath',"//*[@class='like on']").click()


driver.quit()

