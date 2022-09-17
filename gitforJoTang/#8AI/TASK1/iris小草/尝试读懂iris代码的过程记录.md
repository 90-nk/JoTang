# <p align="middle"> iris相关记录
### 尝试弄懂各个package的作用
##### 1.NumPy（Numerical Python）
*“  
是 Python 语言一个重要的扩展库，支持大量的数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。NumPy 通常与其他库 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于模仿 MatLab 的功能。  
”*
##### 2.Matplotlib
*"  
大概是用于绘图的，类似于Matlab的一个package。  
”*
##### 3.Torch
*"  
用来创建、处理张量的库。  
”*  
附一点对于张量的理解：  
> 张量是数据的基本单位，它可以是数字，向量，矩阵或任何n维数组。

##### 4.sklearn
### 开始学习摸索代码内容（其实该标题写于4.sklearn之前）
##### 1.了解python基本语法，基本结构
*“大部分学习内容来自焦糖招新上的超链接《零基础入门学习Pyhton》”* 
> 一些与C语言的比较基本的区别：
>  
①语句的结束不使用“；”，而是使用回车换行  
②函数，逻辑判断不使用“{}”，而是使用空格缩进  
③使用#号来表示单行注释，多行注释使用三个引号，如""" '''  
④不需要int float char来声明变量
> 一些语句的词语

①条件语句：*if/elif/else*  
②循环语句：*while/for/continue/pass*  

> 字符串

①访问：print(*字符变量*[a:b*(范围)*])  
②转义符：*\*  
③运算符：略（XD  
### 跟随CSDN上的 [学习笔记](https://blog.csdn.net/zhu_rui/article/details/105900142?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166341277116800184160339%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166341277116800184160339&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-105900142-null-null.142^v47^pc_rank_34_ecpm25,201^v3^control&utm_term=python%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B&spm=1018.2226.3001.4187)进行一些理解工作
##### 1.“#获得神奇的iris数据集”
from sklearn import datasets  
> 从sklearn里面引进datasets  

dataset = datasets.load_iris()  
> 将datasets.load_iris赋值到dataset
> datasets.load_iris()从datasets里面加载iris数据集  

##### 2.“#善用print功能，观察数据集”
在《iris小草的辅助理解尝试代码1》中，使用了print(dataset.keys())  
xxxx.keys()  
> keys() 函数：获得字典中的所有的键  
> 对于“键”的理解:
> 比如：  
> tinydict = {'Name': 'Zara', 'Age': 7}  
> print "Value : %s" %  tinydict.keys()  
> 则会打印出Value : ['Age', 'Name']  
> “键”的意思大概就是这样  

print(dataset['data'])
> 打印dataset里面'data’键内的全部内容。（只是学习过程中的了解过程，真实运行代码时不是必要的一步）
##### 3.“#完善代码：寻找合适的函数”
