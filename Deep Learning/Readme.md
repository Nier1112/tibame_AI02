## 深度學習：
 + CNN-Convolution Neural Networks(捲積網路)為眼睛，萃取特徵用
 + MLP-Multilayer Perception(神經網路)為大腦，
 + CNN+MLP 則為一個完整的神經網路，當訓練到一定程度後，拿來判斷未知物品用
## 遷移學習：可以將訓練好的 CNN 拿來自己的 MLP 使用
 + weights="imagenet" 要放上去, 才能抓到 imagenet 訓練結果
 + tensorflow.keras 目前 tensorflow_version 2.X 版本 in colab
 + keras中文說明： https://keras.io/zh/layers/core/

## 模型在預測時會將所預測的分類由機率由高排名到低, ImageNet 內有1000種分類 
+  Top1 accuracy: 指排名第一個的類別與實際結果相同
+  Top5 accuracy: 指前面五個預測的結果與實際結果相同

## 當神經網路表現不理想時：
先了解是否為訓練結果不理想或是測試結果不理想
#### 當訓練結果不理想時：
+ 調整激活函數
+ 調整學習率 adam(learning_rate=0.000001~0.1)
#### 訓練結果好，測試結果不理想時：
+ 收集更多資料
+ Earlystoping, 當準確率不再提高時就停止訓練, 避免過擬和
+ batch_normalization, 用於避免資料不均勻的正則化,使 function 更平滑
+ dropout, 丟掉一些神經元限制其擬和能力
+ data augmentation, 圖片資料時可以考慮, 讓圖片產生多種角度增加數量


##### VGG16 and VGG19 ->傳統CNN
   + 由2014年時牛津大學計算機視覺組(Visual Geometry Group)和Google DeepMind 公司一起研究出來的VGG Net, 取得ILSVRC 2014比賽分類項目第二名
   + VGG發展的背景建立於CNN (AlexNet 於2012年獲得影像識別冠軍) 的成功而開始發展，且因為GPU出現以後，加速了CNN的發展速度
   + VGG最重要的概念是，使用大量的 3 x 3 CNN處理，在此之前都是較大的CNN在處理，當VGG開始使用較小的CNN時，可以讓特徵擷取的訊息量提高
   +	兩個 3x3 CNN = 一個5x5 CNN ->兩者 output皆為4
   + 三個 3x3 CNN = 一個7x7 CNN-> 兩者 output 皆為 2
   + 論文：https://arxiv.org/pdf/1409.1556.pdf
##### ResNet, ResNetV2, ResNeXt ->加深的CNN
##### InceptionV3 ->Inception系列是加寬的CNN
##### DesneNet -> 減少特徵消失的CNN
