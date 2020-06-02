## 演算法正確率不是唯一評分的重點，並且需要告訴你哪一個特徵是重要的，好處是可以告訴你那些特徵是評斷重點，讓使用者體驗好
## 有些時候 feature_importance_ 可以告訴你特徵的重要性，是比較重要的。

怎麼用?遇到機器學習首先了解，我的資料是分類還是回歸，

分類：
1. 文字型資料：單純貝式(Navie-Bayes)
2. 非文字資料：隨機森林(Random Forest classifier)

回歸：
1. 隨機森林(Random Forest regression)：基本要會
2. Liner regression-Lasso：針對太多欄位處理，加強版 LassoCV
3.	Liner regression-Ridge：針對依賴某個欄位而處理，加強版 RidgeCV
4.	Liner regression-ElasticNet：綜合Lasso和Ridge兩種方式，針對欄位太多以及太依賴某個欄位而處理，加強版ElasticNetCV

分群：
+ K means：分群
