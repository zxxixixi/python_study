 
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
 
 
# path = 'D:/驱动/chromedriver_win32/chromedriver.exe'
 
# #打开浏览器
# chrome_options = Options()
# chrome_options.add_argument('headless')
# # chrome_options.add_argument('--disable-gpu')
# # 驱动路径
# path = 'D:/驱动/chromedriver_win32/chromedriver.exe'
# # 创建浏览器对象
# driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

from selenium import webdriver
import time
# option = webdriver.ChromeOptions()
# print(option)
# option.add_argument('--disable-popup')
# driver =webdriver.Chrome(chrome_options=option)
driver=webdriver.Chrome()
driver.get('https://blog.csdn.net/qq_44929535')

for i in range(0,29):
	driver.find_element_by_xpath('//*[@id="articleMeList-blog"]/div[2]/div['+str(i+1)+']/h4/a').click()
	time.sleep(i%4)

driver.quit()