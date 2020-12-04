from selenium import webdriver
import time
import random
driver=webdriver.Chrome()
urllist=[
	'https://blog.csdn.net/qq_44929535/article/details/109995242',
    'https://blog.csdn.net/qq_44929535/article/details/109967975',
    'https://blog.csdn.net/qq_44929535/article/details/109809877',
    'https://blog.csdn.net/qq_44929535/article/details/109745538',
    'https://blog.csdn.net/qq_44929535/article/details/109116634',
    'https://blog.csdn.net/qq_44929535/article/details/107841031',
    'https://blog.csdn.net/qq_44929535/article/details/109384851',
    'https://blog.csdn.net/qq_44929535/article/details/109112917',
    'https://blog.csdn.net/qq_44929535/article/details/109809877',
    'https://blog.csdn.net/qq_44929535/article/details/109745538',
    'https://blog.csdn.net/qq_44929535/article/details/109116634',
    'https://blog.csdn.net/qq_44929535/article/details/107841031',

]

for i in range(0,10):
	url=random.choice(urllist)
	driver.get(url)
	time.sleep(3)
else:
	time.sleep(3)
	# os.system('taskkill /IM chrome.exe')