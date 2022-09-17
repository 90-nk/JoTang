# <p align="middle"> 关于配置Python
### 一、安装Python
这个步骤没什么好说的，直接在廖雪峰老师的Python教程上就可以直接进行下载和安装。  
*PS：因为安装程序中可以选择勾选Add Python 3.8 to PATH，故省去了为Python配置环境变量的过程
### 二、pip的安装
在网络上搜索到了一个靠谱的Python的模块安装过程，[教程的网站](https://zhuanlan.zhihu.com/p/27135994)。于是也轻松的进入了pip的[官网下载地址](https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)。于是捏，使用了CMD控制台成功安装好了pip.
### 三、安装numpy包
 一开始配置过程中遇到的错误：  
> 一开始的时候，同样是跟着[网上找的教程](https://zhuanlan.zhihu.com/p/27135994)尝试安装numpy。但是没有思考直接下载安装了最新的版本，适配cp311，于是乎失败了。  

于是之后又在网上检索到了出现 *“...is not a supported wheel on this platform”*的[解决办法](https://blog.csdn.net/weixin_41781973/article/details/88350856)，输入了
> python  
> inport pip._internal
> print(pip._internal.pep425tags.get_supported())  

于是得到了自己安装的版本应该选择cp38，于是便下载之，并完成了在cmd上的安装。  
有些担心在cmd上安装的numpy模块只能在直接打开的python里面用，又是又进入了VSC的终端，重复了一遍安装过程，尽管安装已经成功，但用VSC打开iris代码中的import numpy似乎还是在报错，不理解了，我再看看  
呃呃，原来已经配置好了，重启一下VSC就可以了
### 三、安装torch包
本来想沿用之前安装numpy的办法，在第三方库上面先下载，然后再直接安装。但是直接找torch关键词太难找了，我尝试将网址最后的#numpy改成#torch，但是还是没有直接跳到torch，本来想再开一个插件检索文本内容，但是还是没有尝试。  
于是就直接尝试了在cmd里面输入pip install 指令来尝试安装对应模块。  
但是那天晚上的限速太慢了，然后时间也有点晚了，于是乎就上床睡觉了  
结果捏，第二天早上的下载速度就又恢复正常了。
# <p align="middle">至此，python的环境配置完成