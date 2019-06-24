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

#有序集合list,索引从0开始
list1 = ['xiaoming','sanmao','shazi']
print(list1[0])
print(list1)
#使用len()获得list元素个数
print(len(list1))
#可直接用-1获取最后一个索引(倒推)
print(list1[-1])
list1.append('addmode')
print(list1)
#插入数据到指定索引位置
list1.insert(1,'sierge')
print(list1)
#删除末尾元素pop(),删除指定元素pop(i)
list1.pop()
print(list1)
list1.pop(3)
print(list1)
#替换元素，直接赋值
list1[1] = 'tihuan'
print(list1)

#有序列表tuple(元组),一旦初始化不可更改(指向对象不可变,指向对象本身可变))

#条件判断
name = int(input('请输入你的年龄'))
if name<18:
  print('未成年')
else:
  print('黄花大闺女')

#for循环
for name in list1:
  print(name)

lists = range(5)
print(lists)
sum = 0
for x in range(5):
  sum = sum + x
print(sum)

#while循环
sum = 0
n = 5
while n > 0:
  sum = sum + n
  n = n - 2
print(sum)

#break
n = 1
while n <= 100:
  if n > 10: # 当n = 11时，条件满足，执行break语句
    break # break语句会结束当前循环
  print(n)
  n = n + 1

#continue
n = 0
while n < 10:
  n = n + 1
  if n % 2 == 0: # 如果n是偶数，执行continue语句
    continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
  print(n)

#字典dict,set(非重复key的集合)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#汉诺塔
def move(n, a, b, c):
  while n > 1:
    if n%2 != 0:
      print(a, '-->', c)
      n = n - 1
    else:
      print(a, '-->', b)
      print(c, '-->', b)
      print(b, '-->', c)
      n = n - 1


move(3, 'A', 'B', 'C')

#切片
#[::1]中省略起止位置，步进为1
#python中步进为正，从左往右取，步进为负，从右往左取
print(list1[:3])
print(list1[1:3])
print(list1[-2:])
print(list1[-2:-1])

#自定义字符串去空格方法
def trim(s):
  if len(s)==0:
    return s
  elif s[0]==' ':
    return trim(s[1:])
  elif s[-1]==' ':
    return trim(s[:-1])
  return s
print(trim('    dsfsd     '))

#迭代
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

for i, value in enumerate(['A','B','C','D']):
  print(i,value)

#查找一个list中最小和最大值
def findMinAndMax(L):
  min = L[0]
  max = L[0]
  for i in L:
    if i < min:
      min = i
    if i > max:
      max = i
  return (min, max)
print(findMinAndMax([1,2,3,4,5,6,7,8,50,11,15,10,-5]))

#列表生成式
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n + z for m in 'ABC' for n in 'XYZ' for z in '123'])
#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
  print(k, '=', v)

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])

#首字母大写
def normalize(name):
  name=name[0].upper()+name[1:].lower()
  return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#filter
def is_odd(n):
  return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


def is_palindrome(n):
	return str(n)==str(n)[::-1]
output=filter(is_palindrome, range(1,1001))
print(list(output))

#sorted排序
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))

def by_name(t):
  return t[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=by_name))
print(L)
#input('\n\n按下enter退出')