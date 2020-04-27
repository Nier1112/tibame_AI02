import cv2
import numpy as np

m1 = cv2.imread("./3d-green-letter-o.png", 0)
m2 = cv2.cvtColor(m1, cv2.COLOR_BAYER_BG2GRAY) #弄成灰階
#m2圖設定門檻值為127, 及二值化後的最大值是255, 超過127的像素設為255, 低於127的像素設為0,
th, m2 = cv2.threshold(m2, 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
#cv2.RETR_TREE儲存所有輪廓及對應資料, cv2.CHAIN_APPROX_NONE儲存所有輪廓點
ct, th = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("輪廓點是：", ct)
print("輪廓階層資料:", th)

# #繪製輪廓,
# m3 = np.full(m1.shape, 255, np.uint8)
# #畫m3圖 ct存取全部輪廓索引, -1 是所有輪廓都畫, (0,0,255)用紅色, 粗細度2
# #相臨輪廓:輪廓在旁邊沒有把它包起來, 包覆:外面的輪廓包含住裏面的輪廓
# cv2.drawContours(m3, ct, 2, (0,0,255), 2)
#
# cv2.imshow("m1", m1)
# cv2.imshow("m3", m3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#取輪廓點:
m3 = np.full(m1.shape, 255, np.uint8)
for d in range(0, len(ct)):
    x, y, w, h = cv2.boundingRect(ct[d])
    if w < m1.shape[1]*0.3: #m1.shpe[1]是指圖像的寬的0.2倍. m3裏面物體的寬度小於原圖的20%就取輪廓
        cv2.rectangle(m1,(x,y), (x+w, y+h), (0,0,255), 2) #畫一個矩形.
        #cv2.drawContours(m3, ct, d, (0,0,255), 2)
cv2.imshow("m3", m3)
cv2.imshow("m1", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#取輪廓點
m1 = cv2.imread("./3d-green-letter-o.png", 0)
th, m2 = cv2.threshold(m2, 240, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
m3 = np.full(m1.shape, 255, np.uint8)
for d in range(0, len(ct)):
    x, y, w, h = cv2.boundingRect(ct[d])
    if w>h*2:
        cv2.imshow("m3"+str(d), m1[y:y+h, x:x+w])
        cv2.rectangle(m1, (x,y), (x+w, y+h), (0,0,255), 2)

cv2.imshow("m3", m3)
cv2.imshow("m1", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()
