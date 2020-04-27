import cv2
import numpy as np

# #打開影片
# v = cv2.VideoCapture("./NEZUKO.mp4")
# print("影寬:", v.get(3)) # 640
# print("影片高:", v.get(4)) # 480
# print("每秒影格數:", v.get(5))
# print("影片總影格數:", v.get(7))
# w = cv2.VideoWriter("./N2.mp4", cv2.VideoWriter_fourcc(*'MP4V'), 10, (1280, 720))
# while v.isOpened():
#     r, m2 = v.read()
#     if r == True:
#         print("當前影格:", v.get(1))
#         cv2.imshow("m1", m2)
#         w.write(m2)
#         cv2.waitKey(33)
#     else:
#         break
# w.release()
# cv2.destroyAllWindows()
# #影像二值化處理,
# m1 = cv2.imread("./3d-green-letter-o.png", 1)
# #127門檻值, 255像素最大值, binary是超過門檻值的像素為最大值, 小於門檻值設為0
# th, m2 = cv2.threshold(m1, 127,255, cv2.THRESH_BINARY)
# print("門檻值:", th)
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# #門檻值自動計算, THRESH_OTSU只能接受單一通道色彩
# m1 = cv2.imread("./3d-green-letter-o.png", 0)
# #127門檻值, 255像素最大值, binary是超過門檻值的像素為最大值, 小於門檻值設為0
# th, m2 = cv2.threshold(m1, 127,255, cv2.THRESH_BINARY, cv2.THRESH_OTSU)
# print("門檻值:", th)
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# #將彩色圖片先處理成單色，在處理二值化
# m1 = cv2.imread("./3d-green-letter-o.png", 1)
# m2 = m1.copy() #讓m1根m2圖片大小相同,
# th, m2[:,:,0] = cv2.threshold(m1[:,:,0], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:,:,1] = cv2.threshold(m1[:,:,1], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# th, m2[:,:,2] = cv2.threshold(m1[:,:,2], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# #cv2.imshow("m3", m3)
# cv2.waitKey()
# cv2.destroyAllWindows()

# #當圖片亮暗情況差異很大, 需要將每一個地方當做一個區塊來計算二值, 能夠完全處理所有地方避免某些區塊因為計算後不見
# m1 = cv2.imread("./3d-green-letter-o.png", 0)
# #m1的圖設定像素對大直為255, 計算區塊大小為5, 計算區塊大小之內的平均值再減去微調值(0),
# m2 = cv2.adaptiveThreshold(m1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #用上面坊法處理後, 小字的地方會比較清晰呈現, 整張圖的樣子比較清晰

# #將圖片先設定為單一顏色通道後在處理
# m1 = cv2.imread("./3d-green-letter-o.png", 1)
# m2 = m1.copy() #將m2設定為跟m1一樣大小的畫布
# #0是藍色通道, 取出m1的藍色通道, 影像二值化之後, 再放到m2的藍色通道內, 以下依此類推
# th, m2[:,:,0] = cv2.threshold(m1[:,:,0], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU) #0=藍色
# th, m2[:,:,1] = cv2.threshold(m1[:,:,1], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU) #1=綠色
# th, m2[:,:,2] = cv2.threshold(m1[:,:,2], 127,255, cv2.THRESH_BINARY|cv2.THRESH_OTSU) #2=紅色
# #影像二值化, adaptiveThreshold只接受單一通道色彩空間
# m2[:,:,0] = cv2.adaptiveThreshold(m1[:,:,0], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
# m2[:,:,1] = cv2.adaptiveThreshold(m1[:,:,1], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
# m2[:,:,2] = cv2.adaptiveThreshold(m1[:,:,2], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 0)
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #邊緣偵測, 用大的門檻值1,檢測邊緣繪製一次, 再把小的邊緣數值將
# m1 = cv2.imread("./3d-green-letter-o.png", 1)
# m2 = cv2.Canny(m1, 100, 200)
#
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #平均值模糊法
# m1 = cv2.imread("./3d-green-letter-o.png", 1)
# #m2 = cv2.blur(m1, (15,15)) #寬 高內的平均值
# #局部模糊
# m2 = m1.copy() #先複製一個跟m1一樣大小的圖, 再做下面處理
# m2[0:100, 0:100] = cv2.blur(m1[0:100, 0:100], (15,15))
#
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #中值模糊法, 所有值排序之後取最中間值, 前後會被忽略掉, 糊到最後會把東西模糊掉
# m1 = cv2.imread("./3d-green-letter-o.png", 1)
# m2 =cv2.medianBlur(m1, 25)
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #銳利化法, 假設像素有兩種127跟128, 做完之後127=0 128=255, 會把兩種顏色差距拉大, 會更清晰
# m1 = cv2.imread("./unnamed.jpg", 1)
# m2=m1.copy()
# #m2 = cv2.equalizeHist(m1)
# m2[:,:,0] = cv2.equalizeHist(m1[:,:,0]) #把RGB通道拆開成單一顏色通道, 之後在做銳利化
# m2[:,:,1] = cv2.equalizeHist(m1[:,:,1])
# m2[:,:,2] = cv2.equalizeHist(m1[:,:,2])
#
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#型態學, 侵蝕:色彩值低的(顏色越深的)變大, 色彩值高(顏色越淺)的變小
m1 = cv2.imread("./3d-green-letter-o.png", 1)
#m2 = cv2.erode(m1, np.ones((25,25)))
#型態學, 膨脹:色彩值高(顏色淺的)的變大, 色彩值低的(顏色深的)變小
#m2 = cv2.dilate(m1, np.ones((5,5)))
# #組合應用效果, 先讓色彩值低的變大, 再讓色彩質高的變大
# m2 = cv2.dilate(m1, np.ones((7,7)))
# m2 = cv2.erode(m1, np.ones((7,7)))

# #先膨脹在侵蝕函式
# m2 = cv2.morphologyEx(m1, cv2.MORPH_CLOSE, np.ones((7, 7)))
#
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#留下色像值 0~100之間的物件
#字體範圍內0~100的是大字體, 直接變成白色, 其他變成黑色
#m2 = cv2.inRange(m1, (0,0,0), (100,100,100))
#小字變成白色,消失, m1是三維像素彩色圖, m2是變成二維像素單色圖
#m2 = cv2.inRange(m1, (160,160,160), (255,255,255))

# #讓大字體消失., !!原則是把要保留的變成黑色在做運算將其他東西去除!!
# m2 = cv2.inRange(m1, (0,0,0), (100,100,100)) #先保留0~100的深色變成白色
# m2 = cv2.cvtColor(m2, cv2.COLOR_GRAY2BGR) #將灰階轉換成BGR
# m2 = cv2.dilate(m2, np.ones((3,3))) #將m2色彩淺的範圍變大
# m2 = cv2.add(m1, m2)
# #留下大字,
# m2 = cv2.inRange(m1, (0,0,0), (100,100,100)) #先保留160~255的淺色變成白色
# m2 = cv2.cvtColor(m2, cv2.COLOR_GRAY2BGR) #將灰階轉換成BGR, 顏色不會變只是通道改變成三通道
# m2 = cv2.dilate(m2, np.ones((3,3))) #將m2色彩淺的範圍變大
# m2 = cv2.bitwise_not(m2) #色相相反
# m2 = cv2.add(m1, m2)

# #留下logo,未完
# m2=cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)
# th, m2=cv2.threshold(m2, 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
#
# m2=cv2.cvtColor(m2,cv2.COLOR_GRAY2BGR)
# m2=cv2.bitwise_not(m2)
# m2=cv2.erode(m2,
# 	np.ones((2,2))
# )
# m2=cv2.dilate(m2,
# 	np.ones((5,5))
# )
# # m2=cv2.add(m1,m2)
#
# #================
# m4=cv2.subtract(m2,m3)
# m4=cv2.bitwise_not(m4)
#
# m5=cv2.add(m1,m4)
#
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.imshow("m3", m3)
# cv2.imshow("m4", m4)
# cv2.imshow("m5", m5)
# cv2.waitKey(0)
# cv2.destroyAllWindows() #未完