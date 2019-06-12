#打印字符串
print('hello world')
#多个字符串用逗号隔开
print('This is pythone3 Demo','hello','jack')
#打印整数
print(300)
#打印计算结果
print(100+200)
#输入
name = input()
print(name)
print('1024*768=',1024*768)

#python数据类型:整数，浮点数，字符串，布尔值(True/False)，空值(None不能理解为0)，列表，字典，自定义等数据类型
#转义字符
print('I\'m "OK"')
print('\n','\\n表示换行')
print('r\'\'',r'内部不转意\\')
print('''第一行
第二行
第三行''')
print(r'''第一行,\n
第二行''')
#动态语言:变量类型不固定
a = 123
print('a=',a)
a = 'adc'
print('a=',a)
#静态语言:Java

#字符串和编码
#ASCII编码:数字大小写英文共计127个字符(1字节)
#GB2312编码:中文编码
#各国标准不一，多语言混合导致乱码
#Unicode编码统一语言规范(通常2字节,非常偏僻的字符4字节)
#全英文文本Unicode比ASCII多需要一倍存储空间
#可变长编码UTF-8(英文1字节，汉字3字节，很生僻的字符4-6字节，节省空间)
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(555))
print('\u4e2d\u6587')
#网络传输或保存到磁盘需把str转为bytes
x = b'ABC'
print(x)
#Unicode表示的str可以通过encode()指定编码byte
print('ABX'.encode('ascii'))
print('中午'.encode('utf-8'))
#decode()转bytes为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))
#计算str包含多少字符或者bytes字节数
print(len('ABC'))
print(len(b'ABC'))

#!/usr/bin/env python3 告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
# -*- coding: utf-8 -*- 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

#格式化字符串(%d整数,%f浮点数,%s字符串,%x十六进制整数)
print('%2d-%02d'%(2,1))
print('%.2f'%3.14156)

input('\n\n按下enter退出')