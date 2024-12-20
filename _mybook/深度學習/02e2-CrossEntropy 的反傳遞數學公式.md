## CrossEntropy 的反傳遞數學公式


ChatGPT:

CrossEntropy 是用來評估機器學習模型機率預測的好壞程度，通常用於分類問題中。

給定 $n$ 個樣本數據，假設對於第 $i$ 個樣本，真實分類為 $y_i$，模型預測為 $p_i$，則 CrossEntropy 的公式如下：

$$
H(p, q) = -\frac{1}{n}\sum_{i=1}^n y_i \log{p_i} + (1-y_i)\log{(1-p_i)}
$$

其中 $p_i$ 是指模型對於樣本 $i$ 屬於正類的機率，$y_i$ 則是指樣本 $i$ 的實際標籤，如果是正類則為 1，反之則為 0。

在反向傳播算法中，我們需要對 CrossEntropy 的損失函數求梯度，這樣才能進行參數的更新。假設 $L$ 為損失函數，$w$ 為參數向量，則 $L$ 對於 $w$ 的梯度可表示為：

$$
\nabla_w L = \frac{1}{n}\sum_{i=1}^n(p_i-y_i)x_i
$$

其中 $x_i$ 是指樣本 $i$ 的特徵向量。根據此公式，可以使用梯度下降算法或其它優化方法，以最小化 CrossEntropy 損失。