# Python学习笔记
## 第一天 
Python2 与Python3 的区别
去除print语句，加入print()函数实现相同的功能。同样的还有 exec语句，已经改为exec()函数 
举例如下：
> 2.X: print "The answer is", 2*2    
> 3.X: print("The answer is", 2*2) 

详细情况可以看链接：
[python2和3的区别](http://www.cnblogs.com/codingmylife/archive/2010/06/06/1752807.html)

##第二天
ctrl+z=^z 回车退出python  

常用的命令行  
dir:显示当前目录下的文件  
md:在当前目录下创建文件夹  格式：md 文件名  
cd：跳转目录  
cd.. 回到上一级目录  
cd/  回到根目录  
cd 文件名 跳转到当前文件夹的下一级文件夹

##第三天（ex1.py）
-在脚本文件存放的路径下运行即--当powershell中的路径为脚本存放的位置时才能输入命令 python ex1.py 运行。  
-关于print:  
 1.#并空格能让该行无法显示  
 2.,能使输出不换行  
 3.print输出1行空行，print"\n"能输出2行空行，print"\n"*3输出3行空行  

##第四天（ex2.py&ex3.py）
1.#号的用法和名字  
-英文为 octothorpe，在引号中不会被忽略掉因为此时的#号是句子的一部分。  
print "Hi # there." 里的 # 没被忽略掉。  
-在引号结束后的#号会被忽略掉，具体可见ex2.py。

2.运算符和数据类型  
-%表示求余数，即“X 除以 Y 还剩余 J”求J  
-/表示除，当不能整除时，对于整数型得到整数，[浮点数](http://blog.csdn.net/suchangming/article/details/1957066)则得到小数。  
例如5/4和5.0/4.0的结果就不一样

-运算优先级是什么样子的？
美国我们用 PEMDAS 这个简称来辅助记忆，它的意思是“括号、指数、乘、除、加、减”——
Parentheses Exponents Multiplication Division Addition Subtraction ——这也是 Python 里的
运算优先级。
