## 深度學習，CNN-Convolution Neural Networks(捲積網路)為眼睛，萃取特徵 + MLP-Multilayer Perception(神經網路)為大腦，認識特徵
## 可以將訓練好的 CNN 拿來自己的 MLP 使用
## tensorflow.keras 目前 tensorflow_version 2.X 版本 in colab
keras中文說明： https://keras.io/zh/layers/core/
當模型在預測的時候會將所預測的分類由機率高排名到機率低, 尤其是 ImageNet 內有1000種分類, 
> Top1 accuracy: 指排名第一個的類別與實際結果相同
> Top5 accuracy: 指前面五個預測的結果與實際結果相同
