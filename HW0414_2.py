#剔除照片上除了文字以外的景物, 文字變黑色, 背景值去除
import numpy as np
import cv2
#原圖
m1 = cv2.imread("./homework2.png", 1)
m2 = np.full(m1.shape, (0, 0, 255), np.uint8) #255, 0, 0藍色  0,255,0 綠色  0,0,255 紅色
#扣掉紅色之後，讓字體變成黑色
m3 = cv2.subtract(m1, m2)
print("圖片高:", m3.shape[0])
print("圖片寬:", m3.shape[1])
for i in range(0, 1087):
    for j in range(0, 612):
        if m3[j, i].any() != 0: #如果m3在跑過的位子不是黑色
            m3[j, i]=255 #m3就設定為白色(255)


cv2.imshow("m3", m3)
# cv2.imshow("m4", m4)
# cv2.imshow("m7", m3)

cv2.waitKey(0)
cv2.destroyAllWindows()