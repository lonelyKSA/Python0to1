# open函数的用法  
## 最简单的用法：打开文件，读取，并输出。
>test = open('a.txt','r')  
testSTR = test.read()  
print testSTR  

第一句表示以读的方式打开a.txt文件，第二句表示将文件的内容读入并赋值给testSTR变量，第三句打印文件内容。   

**下面的方式更为简单：**
>test = open(r'c:\a.txt','r')  
print test.read()**

##一个常见的错误  
IOError: [Errno 22] invalid mode ('r') or filename:
这种错误的出现是在使用built-in函数file()或者open()的时候。或者是因为文件的打开模式不对，或者是文件名有问题。前者的话只需要注意文件是否可读或者可写就可以了。后者则是与文件路径相关的问题，需要在文件名前加r或者R转义，如：file(r'e:\Test.txt','r').或者将反斜杠\变成两个，如file('e:\\Test.txt','r').

## 注意事项  
打开文件的时候要填好文件路径，或者把文件放在和脚本同一个文件夹里即可。

## 关闭文件  
打开了文件以后要关闭，关闭语句是对变量使用的：test.close()
