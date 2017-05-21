## 第二十一天-list


1. join（）
将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串。

> str = "-";  
seq = ("a", "b", "c"); # 字符串序列  
print str.join( seq );

2.[:] 对字符串和列表等切片。
[:]截取所有元素
[1:] 截取列表中从第2个到最后一个。
[:2] 截取列表中第1个和第2个。



## 第二十二天-dicts

字典有key和value组成。
字典的局限在于其无序性，而列表是有序的。

1.item（）：返回字典中的key和value组成一个元组，并放在列表中返回。没有item时用for循环遍历只会返回key值。

2.get（）：返回指定key的value，如果值不在字典中返回默认值，不输入时为none，若输入值，当不存在时则返回其输入值。
>city = cities.get('TX', 'Does Not Exist')  
print "The city for the state 'TX' is : %s" % city  


如果TX存在，则返回TX在字典中对应的值（不一定是括号里面的值）；  
如果TX不存在，切表达为get（'TX'）则为none；  
如果TX不存在于字典中，且表达为get('TX', 'Does Not Exist')，则返回‘Does Not Exist’。
