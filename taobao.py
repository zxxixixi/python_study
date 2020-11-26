
import re
import requests

url = 'https://s.taobao.com/search?q=%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20201126&ie=utf8'
payload = {'q': 'g_page_config','s': '1','ie':'utf8'}  #字典传递url参数
file = open('C:/Users/YHAA-1ED2A3/Desktop/taobao_product.txt','w',encoding='utf-8')
cookie_str = r'cna=QsJDGKPtOQUCAXlFXn56tO/s; xlly_s=1; _m_h5_tk=16d32b1f815407a2df3e8d8d9acec207_1606308689929; _m_h5_tk_enc=19aebad8f119bac3c9d04f64c2df10ca; XSRF-TOKEN=14bac8bb-6732-4c51-ad5b-f6e4e830b523; dnk=%5Cu6C90%5Cu7B19521; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie21=UtASsssme%2BBq&existShop=false&pas=0&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie14=Uoe0azUBIx0Bcw%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D; uc3=nk2=gIdv7wxVVw%3D%3D&vt3=F8dCufwmdbAMDjPbnsc%3D&id2=UUGnyZCRrAKp3A%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu6C90%5Cu7B19521; lid=%E6%B2%90%E7%AC%99521; uc4=id4=0%40U2OQ3kyj%2FeqU2SE5dzFglO%2F8%2FVeu&nk4=0%40gsxrS26%2FUeHsmjQUVCXY%2BwWD; _l_g_=Ug%3D%3D; unb=2953956279; lgc=%5Cu6C90%5Cu7B19521; cookie1=BqPlf%2FrNnGNEgQVGe0Pv98TmjKcRPqlXGB7i%2BI6xQe4%3D; login=true; cookie17=UUGnyZCRrAKp3A%3D%3D; cookie2=1c25628993d8ee44af032f6061df71d6; _nk_=%5Cu6C90%5Cu7B19521; sgcookie=E100UbXjE%2B2cuvAa9o2ccCkYmfpkstvnXnWICLc7WPVIg8dPpFczYzfkXZJK%2B2q4wcVtglnUhTevRh37TvInH%2FaEbA%3D%3D; t=a523f2e528d9791567eb93c2e38303a5; sg=195; csg=c71d1aa4; enc=GUBWq6UQwWcSTjNfI82RSrv0hhu0Z2MpFXpeAzNrUjA6kQJ7Kam%2BQRwn0UQy0QGUo%2FPNK2c16dD0BHazY1K%2FEA%3D%3D; _tb_token_=e1e55eeae5373; tfstk=cbMcB_DV_jPXBwVoOKwjxReXqnORwbA4lAkrUYNjPsDVxM5cD_5togKukqDO1; l=eBQUzrqIOlT7oVE9BOfZnurza77TIIRAguPzaNbMiOCPOO1p5qNdWZ7huN89CnGVhsNWR3u14VQUBeYBqImRv7aW0XW42kkmn; isg=BBERTZ5xKp-SlUaItxSlsXX9IB2rfoXwa20-mfOmGFj3mjHsO899wEH4PG58kh0o'
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
for k in range(0,1):        #1次，就是1个页的商品数据
 
    payload ['s'] = 44*k+1   #此处改变的url参数为s，s为1时第一页，s为45是第二页，89时第三页以此类推
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    resp = requests.get(url, headers = headers, cookies = cookies)
    # print(resp.text)          #打印访问的网址
    # print(resp.text)
    # print(resp.url)          #打印访问的网址
    resp.encoding = 'utf-8'  #设置编码
    # file.write(resp.text)

    title = re.findall(r'"raw_title":"([^"]+)"',resp.text,re.I)  #正则保存所有raw_title的内容，这个是书名，下面是价格，地址
    price = re.findall(r'"view_price":"([^"]+)"',resp.text,re.I)
    loc = re.findall(r'"item_loc":"([^"]+)"',resp.text,re.I)
    x = len(title)           #每一页商品的数量
    
    for i in range(0,x) :    #把列表的数据保存到文件中
        file.write(str(k*44+i+1)+'书名：'+title[i]+'\n'+'价格：'+price[i]+'\n'+'地址：'+loc[i]+'\n\n')
        print(title[i])
file.close() 
 
