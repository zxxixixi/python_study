import urllib.request
import requests
import time
import ssl
import random

def openUrl(ip, agent):
 headers = {'User-Agent': agent}
 proxies = {'http' : ip}
 requests.get("https://blog.csdn.net/qq_44929535/article/details/109809877", headers=headers, proxies=proxies, verify=True)
 ssl._create_default_https_context = ssl._create_unverified_context
 print("Access to success.")

#IP池
#IP来源：
# http://www.xicidaili.com/
# https://www.kuaidaili.com/free/
def randomIP():
 ip = random.choice(['120.78.78.141', '122.72.18.35', '120.92.119.229','192.168.43.206'])
 return ip

#User-Agent
#User-Agent来源：http://www.useragentstring.com/pages/useragentstring.php
def randomUserAgent():
 UserAgent = random.choice(['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'])
 return UserAgent

if __name__ == '__main__':
 for i in range(10):
  ip = randomIP()
  print(ip)
  agent = randomUserAgent()
  openUrl(ip, agent)
  time.sleep(3)
