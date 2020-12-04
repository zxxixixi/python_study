import re
import requests
import urllib.request

url = 'https://s.taobao.com/search?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20201126&ie=utf8'
payload = {'q': 'g_page_config','s': '1','ie':'utf8'}  #字典传递url参数
file = open('C:/Users/YHAA-1ED2A3/Desktop/taobao_product.txt','w',encoding='utf-8')
cookie_str = r't=e62fc3896f26735342c795d27a369781; cna=QsJDGKPtOQUCAXlFXn56tO/s; _samesite_flag_=true; cookie2=18f3ca8f664255e5fa4a54f44085d0ef; _tb_token_=ebe1e9783ebeb; xlly_s=1; sgcookie=E100HaqgtKZnFXCoZy4Z47Nyn46ViVkbq193VU%2FlawYv%2FLkTMR%2B%2BBsL00%2FKHXVvfn0WFYKv2csagnjK0at3C8Jbaig%3D%3D; unb=2953956279; uc3=vt3=F8dCuf2CTYSUmaUY9JE%3D&nk2=gIdv7wxVVw%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UUGnyZCRrAKp3A%3D%3D; csg=61e5ac05; lgc=%5Cu6C90%5Cu7B19521; cookie17=UUGnyZCRrAKp3A%3D%3D; dnk=%5Cu6C90%5Cu7B19521; skt=e973007ce0d9b953; existShop=MTYwNjk4MTg4NQ%3D%3D; uc4=nk4=0%40gsxrS26%2FUeHsmjQUXtedYPBO&id4=0%40U2OQ3kyj%2FeqU2SE5dzFgniagOBuB; tracknick=%5Cu6C90%5Cu7B19521; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=195; _nk_=%5Cu6C90%5Cu7B19521; cookie1=BqPlf%2FrNnGNEgQVGe0Pv98TmjKcRPqlXGB7i%2BI6xQe4%3D; enc=tsioNzktZpPH2mJEs2e71efjJFEj9oQ75AsAG68SxuQRqTSj2bhelZDoQOH8yrmK87rNPgbMfsa0d7%2Fmo%2BIxDw%3D%3D; JSESSIONID=0AA6F45EE6E2A23E40F30BED38CCA262; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; mt=ci=98_1; tfstk=c0hNBobKPCdZ66FXe5NVhc4e481OZdr0V6zzIxMpS0Y5-fwGiBSYRXj88rrJtRf..; l=eBLsUV1IOC9O8VWsBOfZourza77TbIRfguPzaNbMiOCPON195BiNWZRThsLpCnGVHsZwR3u14VQeBrT1xyCq0-Y3L3k_J_Dm3dC..; isg=BLW1ZUMcBrw6m2J3oVJ5rO56xDFvMmlEd3laBTfaaix7DtQA_4B3FIrMXNI4ToH8; uc1=cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0&cookie14=Uoe0az9p%2FE1OWw%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=VFC%2FuZ9ainBZ&existShop=false'
cookies = {}
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
for k in range(0,1):        #1次，就是1个页的商品数据
    payload ['s'] = 44*k+1   #数量
    resp = requests.get(url, headers = headers, cookies = cookies)
    # print(resp.text)          #打印文本
    # print(resp.url)          #打印访问的网址
    # resp.encoding = 'utf-8'  #设置编码
    # file.write(resp.text)

    img = re.findall(r'"pic_url":"([^"]+)"',resp.text,re.I)  #正则保存所有raw_title的内容，这个是名称
    # price = re.findall(r'"view_price":"([^"]+)"',resp.text,re.I) #价格
    # loc = re.findall(r'"item_loc":"([^"]+)"',resp.text,re.I) #地址
    x = len(img)           #每一页商品的数量
    
    for i in range(0,x) :    #把列表的数据保存到文件中
        # file.write(str(k*44+i+1)+'名称：'+title[i]+'\n'+'价格：'+price[i]+'\n'+'地址：'+loc[i]+'\n\n')
        print(img[i])
        print(i)
        urllib.request.urlretrieve(img[i].strip,'C:/Users/YHAA-1ED2A3/Desktop/桌面/图片/%s.jpg'%i)

# file.close() 
