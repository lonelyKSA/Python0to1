# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv 
#导入函数并定义变量
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#以写入的方式打开文件
print "Truncating the file. Goodbye!"
target.truncate()
#清除文件中的内容
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")
#输入内容
print "I'm going to write these to the file."

STR = "%s\n%s\n%s\n"  %(line1, line2, line3)

target.write(STR)

#将输入的内容写入到文件中

print "And finally,we close it."
target.close()
#关闭文件
