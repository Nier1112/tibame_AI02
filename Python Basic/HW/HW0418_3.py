import cv2
import numpy as np
#抓取影片前景輪廓, 前景藍色暗, 背景亮, 先處理把筆變成白色,抓框是抓白色最外圍的框

v = cv2.VideoCapture("./homework3.mp4")


while v.isOpened():
    r, m2 = v.read()
    if r == True:
        #取其中一個顏色通道做影像二值化, 門檻值為60,最大值255, 色彩超過60設定為255, 色彩低於60設定為0
        th, m4 = cv2.threshold(m2[:,:,2], 60, 255, cv2.THRESH_BINARY) #b=0, g=1, r=2
        m4 = cv2.bitwise_not(m4) #顏色相反
        x, y, w, h = cv2.boundingRect(m4) #取邊框值
        cv2.rectangle(m2, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow("m2", m2)
        cv2.waitKey(29)
    else:
        break
cv2.destroyAllWindows()