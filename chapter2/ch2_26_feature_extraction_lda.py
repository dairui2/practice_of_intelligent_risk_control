# -*- coding: utf-8 -*- 

import sys
import pandas as pd
sys.path.append("./")
sys.path.append("../")

from utils import data_utils
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 导入数值型样例数据
all_x_y = data_utils.get_all_x_y()
x = all_x_y.drop(data_utils.label, axis=1)
y = all_x_y[data_utils.label]
lda = LinearDiscriminantAnalysis(n_components=1)
x_new = lda.fit_transform(x, y)
x_new_df = pd.DataFrame(x_new)
print("利用sklearn进行LDA特征提取结果: \n", x_new_df)
