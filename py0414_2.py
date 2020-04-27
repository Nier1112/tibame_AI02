import numpy as np
from PIL import ImageDraw, ImageFont, Image
import cv2

# #圖片相加
# # 255為白色，任何值減掉白色(X-255 <0)都是黑色(用substract), 任何值加上白色(X+255=255)都是白色,最大值就是255.(用cv2.add)
# m1 =cv2.imread("./3d-green-letter-o.png", 1)   #原始圖檔
# m2 = np.full(m1.shape, (100, 100, 100), np.uint8) #m1圖檔修改過後的
# m2 = cv2.add(m1, m2)
# m3 = cv2.subtract(m1, m2) #圖片相減，任何值減掉255則等於黑色0 subtract方法低於0的值會直接等於0
# m4 = cv2.absdiff(m1, m2)  #圖片相減，低於0的值會做絕對值運算成為正的值
# m5 = cv2.bitwise_not(m1)  #cv2.bitwise_not 意思是將m1圖片的像素減掉(255, 255, 255)用absdiff的方法，減過頭會取決對值的方式表現只是此方法一張圖就可以處理不用跟別張圖相減
# m2 = m1+100 #由於cv2,imread讀取出來是list, 所以可以直接用list運算, m1的像素值+100放到m2裡面去
# #上面的運算方式，如果所加的數字本身就大於255 則會將原本的圖片改變成不是圖片，imshow就打印不出來，
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# #cv2.imshow("m3", m3)
# #cv2.imshow("m4", m4)
# cv2.imshow("m5", m5)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#小程式監控目前按下的按鍵
import cv2
m1 = cv2.imread("./cloud.jpg",1)
cv2.imshow("m1", m1)
print(cv2.waitKey(0)) #打印出目前按下按鍵對應的ASCII數字, 老師的可以...
cv2.destroyAllWindows()

# #小程式用waitKey()監控所按的按鍵，決定圖片顏色深淺
# m1 =cv2.imread("./3d-green-letter-o.png", 1)
# m2 = np.array([])
# m3 = np.full(m1.shape, 10, np.uint8)
# val = True
# while True:
#     cv2.imshow("m1", m1) #打印出最原始的圖
#     k = cv2.waitKey(0) #監測所按的按鍵
#     if k ==97 : #97 = A
#         if m2.shape[0] == 0 or val == False:
#             m2 = m1.copy()
#         val = True
#         m2 = cv2.add(m2, m3)
#     if k == 98: #98 = B
#         if m2.shape[0] ==0 or val == True:
#             m2 = m1.copy()
#         val = False
#         m2 = cv2.subtract(m2, m3)
#     cv2.imshow("m2", m2)
# cv2.destroyAllWindows()

#縮放及翻轉
# m1 =cv2.imread("./3d-green-letter-o.png", 1)
# #圖像縮放
# m2 = cv2.resize(m1, (50, 50)) #不會自動抓取圖片長與寬,
# #等比例縮放
# nw = int(input("請輸入寬數值:")) #定義寬度, 高度根據寬度計算出和原圖等比大小
# nh = int((nw/m1.shape[1]*m1.shape[0]))
#
# m5 = cv2.resize(m1, (nw, nh))
# cv2.imshow("m5", m5)
#
# cv2.imshow("m1", m1)
# cv2.imshow("m2", m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #圖像翻轉
# m4 = cv2.flip(m1, 1) #1->左右翻轉,
# m5 = cv2.flip(m1, 0)
# cv2.imshow("m1", m1)
# cv2.imshow("m4", m4)
# cv2.imshow("m5", m5)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #圖像旋轉
# print("圖片高:", m1.shape[0])
# print("圖片寬:", m1.shape[1])
# w = cv2.getRotationMatrix2D((150,150), 53, 1)
# m6 = cv2.warpAffine(m1, w, (450, 450))
#
# cv2.imshow("m6", m6)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #圖片裁切, 複製跟貼上
# m7 = m1[0:150, 50:250]
# cv2.imshow("m7", m7)
# cv2.waitKey(0)
# cv2.destroyAllWindows()