## 演算法正確率不是唯一評分的重點，並且需要告訴你哪一個特徵是重要的，好處是可以告訴你那些特徵是評斷重點
## 有些時候 feature_importance_ 可以告訴你特徵的重要性，是比較重要的。
## sklearn

遇到機器學習首先了解，的資料是分類還是回歸，

分類：
1. 文字型資料：單純貝式(Navie-Bayes)
    + MulitnomialNB:對於特徵是是整數，且是次數的分布優化，對於文字類型資料通常使用 MultinomialNB，四個重點
      + 避免文字類型資料造成的維度災難
      + Navie-Bayes 自己會判斷哪一個資料重要性高，不用人工判斷
      + alpha=1，是指所有人都+1 避免出現機率=0 的情況 alpha可以是0.1, 只要不是0就可
    + GaussianNB:用於高斯分布的連續數字優化，例如 iris 資料型態
    + BernoulliNB:對於特徵是 True 或是 Fasle 的二分化資料用, 想像成是簡單版的 MulitnomialNB
    + 通常 GaussianNB 和 BernoulliNB 可以用決策樹或是隨機森林取代 較不常用
  
2. 非文字資料：決策樹(DecisionTreeClasifier) or 隨機森林(Random Forest classifier)
    + 決策樹的優點
        + 看資料相對而言較全面
        + 可以告訴你哪種特徵是重要的
        + 劃出決策樹後好理解
    + 隨機森林的優點
      + 看資料比較全面
      + 可以告訴你哪一種特徵是重要的，KNN 就不行
      
3. KNN：K最近鄰(k-nearest neighbor classification)
    + 目標最近的屬於哪一類就算哪一類一般 k:5~20 附近效果較好，主要看資料量多寡

回歸：
1. 隨機森林(Random Forest regression)：基本要會
2. Liner regression-Lasso：針對太多欄位處理，加強版 LassoCV
3. Liner regression-Ridge：針對依賴某個欄位而處理，加強版 RidgeCV
4. Liner regression-ElasticNet：綜合Lasso和Ridge兩種方式，針對欄位太多以及太依賴某個欄位而處理，加強版ElasticNetCV

分群：
+ K means：分群

衡量方法：
+ 分類： accuracy_score
+ 回歸： r2_score
+ 分群： silhouette_score
