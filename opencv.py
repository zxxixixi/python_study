# # 导入模块 
# import cv2 as cv
# # 读取图片
# img=cv.imread('tiaotiao.jpg') #路径中不能有中文，否则加载图片失败
# #显示图片
# cv.imshow('read_img',img)
# #等待键盘输入 单位毫秒 传入0是无限等待
# cv.waitKey(0)
# #释放内存 由于OpenCV底层是由C++编写的
# cv.destroyAllWindows()



#图片灰度转变
# import cv2 as cv
# img=cv.imread('tiaotiao.jpg')
# cv.imshow('BGR_img',img)
# gray_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)#将图片转换成灰色
# cv.imshow('gry_img',gray_gray)
# cv.imwrite('gry_img_new.jpg',gray_gray)#将图片以gry_img_new.jpg为名,保存在当前目录下
# cv.waitKey(0)
# cv.destroyAllWindows()


# 修改图片的大小
# import cv2 as cv
# img=cv.imread('tiaotiao.jpg')
# print('img',img.shape)#打印图片的尺寸
# resize_img=cv.resize(img,dsize=(200,240))#设置图片的尺寸
# resize_img1=cv.resize(img,dsize=(600,450))
# print('resize_img1',resize_img1.shape)
# cv.imshow('resize_img',resize_img)
# cv.imshow('resize_img1',resize_img1)
# while True:
# 	if ord('q')==cv.waitKey(0): #按q时推出
# 		break
# cv.destroyAllWindows()

#绘制矩形或者圆
# import cv2 as cv
# img=cv.imread('tiaotiao.jpg')
# # x,y,w,h=50,50,40,60 #左上角坐标(x,y) 矩形的宽高w,h
# # cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,0),thickness=2) #设置颜色和粗细
# x,y,r=100,100,50
# cv.circle(img,center=(x,y),radius=r,color=(0,0,255),thickness=2)
# cv.imshow('rectangle_img',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import cv2 as cv
# def fac_detect_demo():
# 	#将图片转换成灰度图片
# 	gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 	#加载特征数据

# 	face_detector=cv.CascadeClassifier('D:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
# 	faces=face_detector.detectMultiScale(gray)
# 	for x,y,w,h in faces:
# 		cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
# 	cv.imshow('result',img)
# #加载图片
# img=cv.imread('zx.jpg')
# fac_detect_demo()# cv.imshow('img',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv 
def face_detect_demo(img):
	gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
	face_detector=cv.CascadeClassifier('D:/opencv/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
	faces=face_detector.detectMultiScale(gray)
	for x,y,w,h in faces:
		cv.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)
	cv.imshow('result',img)

#读取视频
cap =cv.VideoCapture('shipin.mp4')
while True:
	flag,frame=cap.read()
	if not flag:
		break
	face_detect_demo(frame)
	if ord('q') ==cv.waitKey(10):
		break
cv.destroyAllWindows()
cap.release()


# https://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html
