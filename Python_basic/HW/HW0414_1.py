import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

#讀取圖片
img =input("請輸入圖片檔名:")
w = input("請輸入浮水印內容")
s = int(input("請輸入文字大小:"))
m1 =cv2.imread(img, 1)
#在圖片上輸入文字
m1 = Image.fromarray(m1)
ImageDraw.Draw(m1).text((0,0), w, (0, 0, 255), ImageFont.truetype("kaiu.ttf", s))
m1 = np.array(m1)
#打印
cv2.imshow("m1",m1)
cv2.waitKey(0)
cv2.destroyAllWindows()
