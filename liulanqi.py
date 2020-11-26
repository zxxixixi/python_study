# import webbrowser
# webbrowser.open("https://blog.csdn.net/qq_44929535/article/details/109967975")


# -*- coding: utf-8 -*
import webbrowser as web    
import time    
import os    
 
urllist=[
    'https://blog.csdn.net/qq_44929535/article/details/109995242',
    'https://blog.csdn.net/qq_44929535/article/details/109967975',
    'https://blog.csdn.net/qq_44929535/article/details/109809877',
]
 
 
for url in urllist:
    web.open(url,new=2)  #访问网址地址，语法 .open(url,new=0,Autorasise=True),设置 new 的值不同有不同的效果0、1、2   
    time.sleep(3)  #设置每次打开新页面的等待时间
else:  
    time.sleep(1) #设置每次等待关闭浏览器的时间  
    # os.system('taskkill /IM chrome.exe')  #你设置的默认使用浏览器，其他的更换下就行