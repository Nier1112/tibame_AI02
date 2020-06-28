## 深度學習：
 + CNN-Convolution Neural Networks(捲積網路)為眼睛，萃取特徵用
 + MLP-Multilayer Perception(神經網路)為大腦，
 + CNN+MLP 則為一個完整的神經網路，當訓練到一定程度後，拿來判斷未知物品用
## 遷移學習：可以將訓練好的 CNN 拿來自己的 MLP 使用
## tensorflow.keras 目前 tensorflow_version 2.X 版本 in colab
keras中文說明： https://keras.io/zh/layers/core/

#### 當模型在預測的時候會將所預測的分類由機率高排名到機率低, 尤其是 ImageNet 內有1000種分類, 
>  Top1 accuracy: 指排名第一個的類別與實際結果相同
>  Top5 accuracy: 指前面五個預測的結果與實際結果相同

### 當神經網路表現不理想時：
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
##### ResNet, ResNetV2, ResNeXt ->加深的CNN
##### InceptionV3 ->Inception系列是加寬的CNN
##### DesneNet -> 減少特徵消失的CNN
