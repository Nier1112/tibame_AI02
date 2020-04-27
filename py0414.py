#影像處理
import cv2
import numpy as np

# #讀取圖片四部曲, 讀取, show, 等待時間, 關掉視窗
# m1 =cv2.imread("./3d-green-letter-o.png", 1)　＃若設定參數為 0(灰階)則讀取之後無法恢復彩色
# print(m1.shape) #看維度，當cv2.imerd 參數為 0 (灰階)時只有兩種維度
# print("圖片高", m1.shape[0])
# print("圖片寬",m1.shape[1])
# print("圖片色彩通道量", m1.shape[2])
# cv2.ishow("m1", m1) #將 m1的東西以 "m1"的視窗呈現
# cv2.waitKey(0) #等待時間
# cv2.destroyAllWindows() #關視窗

#讀取影片或攝影機, 通常攝影機只有一台是數字0
#c = cv2.VideoCapture(0) #攝影機參數為數字0, 輸入路徑則為讀取影片檔
# print("高度", c.get(4))
# print("寬度", c.get(3))
# print("fps", c.get(5))
# print("總共影片格數", c.get(7))
# #c.set(1, 1200) #參數1 為當前影格, 設定在2500這一格, 可以直接跳躍到2500片段開始播放的功能
# while c.isOpened() ==True: #要讓影片持續抓圖成為影像
#     r, m2 = c.read()
#     if r ==True:
#         print("當前影格",c.get(1))
#         cv2.imshow("m2", m2)
#         #cv2.waitKey(33) #沒回圈時只打cv2.waitKey(33)會出現一張靜態圖片,
#     else:
#         break
#     if cv2.waitKey(33) != -1:
#         break
# while c.isOpened() ==True: #動態影片, 當 c 一直有收到畫面,則持續讀取攝像機畫面內容
#     r, m1 = c.read() #r是判斷有沒有讀到畫面, r =True
#     if r == True:
#         cv2.imshow("m1", m1)
#     else:
#         break
#     #cv2.waitKey(33)
#     if cv2.waitKey(33) != -1: #如果不按下按鍵會繼續執行, 按下則關掉
#         break
#waitKey(33)參數內放33就是fps=33, if 設定為0 or 不設定:會等待使用者按下按鍵,
# 若設定為33則表示時間到繼續執行, 但需配合式影機fps, if 設定144, 攝影機只有60 ->lag or 當機
#cv2.destroyAllWindows() #關閉所有視窗

# #儲存影片
# c = cv2.VideoCapture(0) #攝影機參數為數字0, 輸入路徑則為讀取影片檔
# print("高度", c.get(4))
# print("寬度", c.get(3))
# w = cv2.VideoWriter("./test1.mp4", cv2.VideoWriter_fourcc(*'MP4V'), 25, (640, 480)) #儲存影片高度跟寬度要一致
# while c.isOpened() ==True:
#     r, m2 = c.read()
#     if r ==True:
#         print("當前影格",c.get(1))
#         cv2.imshow("m2", m2)
#         w.write(m2) # 將w拿取到的影片寫入磁碟內
#         #cv2.waitKey(33) #會出現一張靜態圖片,
#     else:
#         break
#     if cv2.waitKey(33) != -1:
#         break
# w.release() #釋放控制變數避免資源被佔用
# cv2.destroyAllWindows()

# #圖片色彩空間轉換
# m1 = cv2.imread("./3d-green-letter-o.png", 1)
# m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2HSV) #將 BGR 轉換成HSV imshow 只支援 BGR
# m3 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY) #將 BGR 轉換成 GRAY 灰階
# cv2.imshow("m1", m1) #將 m1的東西以 "m1"的視窗呈現
# cv2.imshow("m2", m2)
# cv2.imshow("m3", m3)
# cv2.imwrite("test3.png", m3) #png不使用第三個參數
# cv2.imwrite("test4.jpg", m2, [cv2.IMWRITE_JPEG_QUALITY, 50]) #[cv2.IMWRITE_JPEG_QUALITY, 50]為壓縮比, 數字越大壓縮越大畫質越差
# cv2.waitKey(0) #等待時間
# cv2.destroyAllWindows() #關視窗

# #創建一個空白圖片
# m4 = np.full((200,600, 3), (255, 255, 255), np.uint8) #創建一個長
# m5 = np.full((350, 170), 150, np.uint8)
# #cv2.imshow("m4", m4)
# #cv2.imshow("m5", m5)
# #在畫布上畫直線
# cv2.line(m4, (10, 10),(300, 10), (0, 0, 255), 3) #在 m4畫布上面(10, 10)畫到(300,10) 顏色為(0,0,255), 粗細為5
# #cv2.imshow("m4", m4)
#
# #在畫布上畫矩形
# cv2.rectangle(m4, (20, 20), (150, 130), (0, 0, 155), 2) #m4畫布上從左上角(20, 20)畫到右下角(150,130), 顏色(0,0,155)
# cv2.rectangle(m4, (160, 20), (300, 130), (0, 0, 155), -1)
# cv2.circle(m4, (350, 80), 40, (0, 0, 155), 3) #用m4的畫布畫上圓型, 中心點在(350, 80), 半徑40, 顏色(0,0,155), 線體粗度3
# cv2.circle(m4, (450, 80), 40, (0,0,155), -1) #-1為實心圓
# cv2.imshow("m6", m4)


#cv2.waitKey(0)
#cv2.destroyAllWindows()

#寫字
from PIL import ImageFont, ImageDraw, Image
m4 = np.full((200,600, 3), (255, 255, 255), np.uint8) #先寫一個畫布
m4 = Image.fromarray(m4)  #改變大小
ImageDraw.Draw(m4).text((50,50), "Hi python, JO!!", (0, 0, 255), ImageFont.truetype("kaiu.ttf", 50))
m4 = np.array(m4)

cv2.imshow("m5", m4)
cv2.waitKey(0)
cv2.destroyAllWindows()