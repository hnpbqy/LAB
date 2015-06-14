# coding:utf-8
print u"源代码以.py为扩展名由python解释，经编译后生成.pyc文件。经过优化的源文件会以.pyo 生成pyo：python -O -m py_complie hello.py"

print "欢迎使用python中文处理1".decode('utf-8')
#print "欢迎来中国 中文处理1"
str1 = u"欢迎使用python中文处理2"
#str1 = "欢迎使用python中文处理2"
print str1
print  u"欢迎使用python中文处理3"

# 使用中文的例子
#raw_input("Press enter key to close this window");
#print "Hello,world!"
#raw_input("Press enter key to close this window");
#print "欢迎来到奥运中国!"
#raw_input("Press enter key to close this window");

a=100.0
b=201.1
c=234
print  (a+b+c)/c
print u'计算器%d' % ((a+b+c)/c)

#可以如下打印出预定义输出格式的字符串:
print """
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
print u"#变量"
x = 1
print id(x)
x = 2
print id(x)

_a = 1
_b = 2
def fun():
   print _a
   print _b 
fun()
#全局变量也可以专门放文件 improt  引用文件.变量
#常量
#字符串是怎么访问 。python有3种表示字符串类型的方式，即单引号、双引号、三引号
word="abcdefg"
a=word[2]
print "a is: "+a
b=word[1:3]
print "b is: "+b # index 1 and 2 elements of word.
c=word[:2]
print "c is: "+c # index 0 and 1 elements of word.
d=word[0:]
print "d is: "+d # All elements of word.
e=word[:2]+word[2:]
print "e is: "+e # All elements of word.
f=word[-1]
print "f is: "+f # The last elements of word.
g=word[-4:-2]
print "g is: "+g # index 3 and 4 elements of word.
h=word[-2:]
print "h is: "+h # The last two elements.
i=word[:-2]
print "i is: "+i # Everything except the last two characters
l=len(word)
print "Length of word is: "+ str(l)

#请注意ASCII和UNICODE字符串的区别
print "Input your Chinese name:"
s=raw_input("Press enter to be continued");
print "Your name is  : " +s;
l=len(s)
print "Length of your Chinese name in asc codes is:"+str(l);
a=unicode(s,"GBK")
l=len(a)
print "I'm sorry we should use unicode char!Characters number of your Chinese \
name in unicode is:"+str(l);

# 类似Java里的List,这是一种方便易用的数据类型:
word=['a','b','c','d','e','f','g']
a=word[2]
print "a is: "+a
b=word[1:3]
print "b is: "
print b # index 1 and 2 elements of word.
c=word[:2]
print "c is: "
print c # index 0 and 1 elements of word.
d=word[0:]
print "d is: "
print d # All elements of word.
e=word[:2]+word[2:]
print "e is: "
print e # All elements of word.
f=word[-1]
print "f is: "
print f # The last elements of word.
g=word[-4:-2]
print "g is: "
print g # index 3 and 4 elements of word.
h=word[-2:]
print "h is: "
print h # The last two elements.
i=word[:-2]
print "i is: "
print i # Everything except the last two characters
l=len(word)
print "Length of word is: "+ str(l)
print "Adds new element"
word.append('h')
print word

#运算符与表达式 没有自增自减运算i++。但可以i+=1、!= <> 不等于、==等于、 and逻辑与、or逻辑或、not逻辑非。
'''
if (表达式)：
    语句1
else：
    语句2

if (表达式)：
   语句1
elif（表达式）：
   语句2
else：
   语句2
while（表达式）：
   ...
else：
   ...
   
for x in jihe:
   ....
else:
   
'''
# Multi-way decision
x=int(raw_input("Please enter an integer:"))
if x<0:
    x=0
    print "Negative changed to zero"

elif x==0:
    print "Zero"

else:
    print "More"


# Loops List
a = ['cat', 'window', 'defenestrate']
for x in a:
    print x, len(x)

# Define and invoke function.
def sum(a,b):
    return a+b


func = sum
r = func(5,6)
print r

# Defines function with default argument
def add(a,b=2):
    return a+b
r=add(1)
print r
r=add(1,5)
print r


#函数
# The range() function
a =range(5,10)
print a
a = range(-2,-7)
print a
a = range(-7,-2)
print a
a = range(-2,-11,-3) # The 3rd parameter stands for step
print a


spath="D:/download/baa.txt"
f=open(spath,"w") # Opens file for writing.Creates this file doesn't exist.
f.write("First line 1.\n")
f.writelines("First line 2.")

f.close()

f=open(spath,"r") # Opens file for reading

for line in f:
    print line

f.close()


"""
#2.9 异常处理

s=raw_input("Input your age:")
if s =="":
    raise Exception("Input must no be empty.")

try:
    i=int(s)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unknown exception!"
else: # It is useful for code that must be executed if the try clause does not raise an exception
    print "You are %d" % i," years old"
finally: # Clean up action
    print "Goodbye!"

#--------------------------------------------------------------------------------


#2.10 类和继承

class Base:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

# Child extends Base
class Child(Base):
    def plus(self,a,b):
        return a+b

oChild =Child()
oChild.add("str1")
print oChild.data
print oChild.plus(2,3)

#--------------------------------------------------------------------------------


#2.11 包机制每一个.py文件称为一个module,module之间可以互相导入.请参看以下例子:
# a.py
def add_func(a,b):
    return a+b
# b.py
from a import add_func # Also can be : import a

print "Import add_func from module a"
print "Result of 1 plus 2 is: "
print add_func(1,2)    # If using "import a" , then here should be "a.add_func"

# module可以定义在包里面.Python定义包的方式稍微有点古怪,假设我们有一个parent文件夹,该文件夹有一个child子文件夹.child中有一个module a.py . 如何让Python知道这个文件层次结构?很简单,每个目录都放一个名为_init_.py 的文件.该文件内容可以为空.这个层次结构如下所示:
#parent
  --__init_.py
  --child
    -- __init_.py
    --a.py

#b.py
#    那么Python如何找到我们定义的module?在标准包sys中,path属性记录了Python的包路径.你可以将之打印出来:

import sys

print sys.path
 #   通常我们可以将module的包路径放到环境变量PYTHONPATH中,该环境变量会自动添加到sys.path属性.另一种方便的方法是编程中直接指定我们的module路径到sys.path 中:

import sys
sys.path.append('D:\\download')

from parent.child.a import add_func


print sys.path

print "Import add_func from module a"
print "Result of 1 plus 2 is: "
print add_func(1,2)

"""