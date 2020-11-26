from requests_html import HTMLSession
import pandas as pd
session = HTMLSession()
url = 'https://nvzhuang.tmall.com/?spm=875.7931836/B.category2016010.1.723d4265dgp4g8&acm=lb-zebra-148799-667863.1003.4.708026&scm=1003.4.lb-zebra-148799-667863.OTHER_14561681423980_708026'
r=session.get(url)
# print(r.html.text) #全部文本内容
# print(r.html.links) #相对路劲
# print(r.html.absolute_links) #绝对路径
sel = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'
# results = r.html.find(sel)
# print(results)
# print(results[0].text)
# print(list(results[0].absolute_links)[0])

def isfairy(sel):
	mylist=[]
	try:
		results=r.html.find(sel)
		for result in results:
			mytext =result.text;
			mylink =list(result.absolute_links)[0]
			mylist.append((mytext,mylink))
		return mylist
	except:
		return None
print(isfairy(sel))
df = pd.DataFrame(isfairy(sel))
df.columns = ['text', 'link']
print(df)
df.to_csv('C:/Users/YHAA-1ED2A3/Desktop/output.csv', encoding='gbk', index=False)