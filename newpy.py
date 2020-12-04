import os
import requests
import re


def getimg(soup,i):
    print('http:'+ soup[0])
    root = "D://tu//tu"  # 保存的根目录
    j=1
    for k in soup:
        print(k)
        path = root + str(j) + ".jpg"  # 保存的地址
        if not os.path.exists(path):  # 如果文件不存在就爬取并保存
            mun='http:'+ k
            r=requests.get(mun)
            j=j+1
            with open(path, 'wb') as f:  # 'wb'以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                f.write(r.content)  # content返回二进制数据，所以使用'wb'
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
def main():
    url = 'https://s.taobao.com/search?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20201126&ie=utf8'
    file = open('C:/Users/YHAA-1ED2A3/Desktop/taobao_product.txt','w',encoding='utf-8')
    cookie_str = r't=e62fc3896f26735342c795d27a369781; cna=QsJDGKPtOQUCAXlFXn56tO/s; _samesite_flag_=true; cookie2=18f3ca8f664255e5fa4a54f44085d0ef; _tb_token_=ebe1e9783ebeb; xlly_s=1; sgcookie=E100HaqgtKZnFXCoZy4Z47Nyn46ViVkbq193VU%2FlawYv%2FLkTMR%2B%2BBsL00%2FKHXVvfn0WFYKv2csagnjK0at3C8Jbaig%3D%3D; unb=2953956279; uc3=vt3=F8dCuf2CTYSUmaUY9JE%3D&nk2=gIdv7wxVVw%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=UUGnyZCRrAKp3A%3D%3D; csg=61e5ac05; lgc=%5Cu6C90%5Cu7B19521; cookie17=UUGnyZCRrAKp3A%3D%3D; dnk=%5Cu6C90%5Cu7B19521; skt=e973007ce0d9b953; existShop=MTYwNjk4MTg4NQ%3D%3D; uc4=nk4=0%40gsxrS26%2FUeHsmjQUXtedYPBO&id4=0%40U2OQ3kyj%2FeqU2SE5dzFgniagOBuB; tracknick=%5Cu6C90%5Cu7B19521; _cc_=WqG3DMC9EA%3D%3D; _l_g_=Ug%3D%3D; sg=195; _nk_=%5Cu6C90%5Cu7B19521; cookie1=BqPlf%2FrNnGNEgQVGe0Pv98TmjKcRPqlXGB7i%2BI6xQe4%3D; enc=tsioNzktZpPH2mJEs2e71efjJFEj9oQ75AsAG68SxuQRqTSj2bhelZDoQOH8yrmK87rNPgbMfsa0d7%2Fmo%2BIxDw%3D%3D; JSESSIONID=0AA6F45EE6E2A23E40F30BED38CCA262; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; mt=ci=98_1; tfstk=c0hNBobKPCdZ66FXe5NVhc4e481OZdr0V6zzIxMpS0Y5-fwGiBSYRXj88rrJtRf..; l=eBLsUV1IOC9O8VWsBOfZourza77TbIRfguPzaNbMiOCPON195BiNWZRThsLpCnGVHsZwR3u14VQeBrT1xyCq0-Y3L3k_J_Dm3dC..; isg=BLW1ZUMcBrw6m2J3oVJ5rO56xDFvMmlEd3laBTfaaix7DtQA_4B3FIrMXNI4ToH8; uc1=cookie15=VFC%2FuZ9ayeYq2g%3D%3D&pas=0&cookie14=Uoe0az9p%2FE1OWw%3D%3D&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=VFC%2FuZ9ainBZ&existShop=false'
    cookies = {}
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    r = requests.get(url, headers = headers, cookies = cookies)
    r.encoding = r.apparent_encoding
    demo = r.text
    soup = re.findall(r'"pic_url":"([^"]+)"',r.text,re.I) 
    getimg(soup,1)

main()
