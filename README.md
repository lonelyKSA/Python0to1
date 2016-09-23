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
