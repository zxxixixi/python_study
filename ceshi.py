#!/usr/bin/python3
 
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b


# list=[1,2,3,4]
# it =iter(list)
# print(next(it))

# import sys
# list=[1,2,3,4]
# it =iter(list)
# while True:
# 	try:
# 		print(next(it))
# 	except StopIteration:
# 		sys.exit()


#用类方法来定义迭代
# class deidai:
# 	def __iter__(self):
# 		self.a=1
# 		return self
# 	def __next__(self):
# 		if self.a <20:
# 			x=self.a
# 			self.a+=1
# 			return x
# 		else:
# 			raise StopIteration

# deidai= deidai()
# it=iter(deidai)
# for  i in it:
# 	print(i)


#用yield来保存执行内容，下次执行的时候在这个断点处重新执行,yield也是返回的遍历器
#!/usr/bin/python3
# import sys
# def xunhuan(n):
# 	count, a, b =0, 0, 1
# 	while True:
# 		if count > n:
# 			return
# 		yield a
# 		a,b=b,a+b
# 		count+=1
# it=xunhuan(10)
# # for i in it:
# #    print(i) 
# while True:
# 	try:
# 		print(next(it))
# 	except StopIteration:
# 		sys.exit()
