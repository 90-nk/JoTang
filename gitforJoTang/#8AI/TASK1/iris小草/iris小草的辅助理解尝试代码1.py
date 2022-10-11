#请先根据以下代码先安装好对应的package哦
#ps:大致了解各个package的作用而不需要仔细学习每个package的用法
import numpy as np
import torch
from sklearn import datasets
import torch.nn as nn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#获得神奇的iris数据集
dataset = datasets.load_iris()
#善用print功能,观察数据集的特点哦,它分为data和target两个部分,属性和种类分别是用哪些数据表示的呢?想清楚之后就可以继续往下啦!
print(dataset.keys())
#完善代码:寻找一个合适的函数按照二八比例划分测试集和数据集数据
X=dataset['data']
y=['target']
print(dataset['data'])
print(dataset['target'])
print(dataset['target_names'])
print(dataset['DESCR'])
print(dataset['feature_names'])
print(dataset['filename'])
