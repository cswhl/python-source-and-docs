from selenium import webdriver
import time

driver = webdriver.Chrome("G:/tool/chromedriver_win32/chromedriver")

# 设置浏览器要打开的url
driver.get("http://www.baidu.com")

# 打印网页的title
print(driver.title)

# 在百度搜索框中输入关键字"selenium",
# 网页元素:"<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">"
driver.find_element_by_id("kw").send_keys("selenium")

# 单击搜索框按钮
# 网页元素：<input type="submit" id="su" value="百度一下" class="bg s_btn">
driver.find_element_by_id("su").click()
time.sleep(1)

# 找到selenium官网的链接，并点击进入
element_target = driver.find_element_by_xpath('//*[contains(text(), "automates browsers")]')
element_target.click()
time.sleep(10)

# 页面大小控制:先最大尺寸后更改位800*720
driver.maximize_window()
time.sleep(3)
driver.set_window_size(800, 720)
time.sleep(3)

# 关闭当前网页tab
driver.close()
# 关闭浏览器
driver.quit()
