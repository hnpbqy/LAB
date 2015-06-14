#!/bin/python
#coding=utf-8
import sys
import pickle
import MySQLdb



print"hello world"
#raw_input("your name")
a=10
b=9
c=4
print (a+b)*5
print '''
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
'''
i=5
while i:
    print "processing...",i
    i = i-1
else:
    print "done",i

for i in range(1,5):
    print"processing...",i
else:
    print("done"),i

def Hi():
    print"hi"
Hi()

def Hi():
    print"hi1"
Hi()

def Ti(x,y):
    print "hello",y
Ti(1,2)

print"the path is :", sys.path

age=26
name="jhone"
print"myname is %s,and I am %d years old."%(name,age)
'''
class TT:
    def t2(self):
        print "hi t2"

Myclass = TT()
Myclass.t2()

class TT:
    def t2(self):
        print "hi t2"
'''

'''
class TTT:
    def__init__(self,message):
        self.message = message
    def tt2(self):
        print "hello %s."%self.message

def select():
    conn=MySQLdb.connect(host="192.168.1.166",user="foreman",passwd="odotboss",db="foreman",charset="utf8")
    cursor = conn.cursor()
    n = cursor.execute("select * from userinfo")
    cursor.scroll(0)
    for row in cursor.fetchall():
        print row[0]
        print row[1]
        print row[2]
    conn.close()

def usage():
 print __doc__
 select()

if __name__=='__main__':
 usage()
'''

a = 3
a -=2
a +=2
print a

if a==4:
    print "yes"
else:
    print "no"
# GB231 2->GBK ->扩成了 GB18030。  后来 ISO制定 UNICODE统一各国编码UTF标准 分utf-8（每次8个位传输数据） utf-16
#从UNICODE到 UTF时并不是直接的对应，而是要过一些算法和规则来转换。 所以推荐所有的网页使用统一编码：UTF-8。
# BOM头（0xEF 0xBB 0xBF，即BOM）。它是一串隐藏的字符，用于让记事本等编辑器识别这个文件是否以UTF-8编码
print  u"list列表一维数组 tuple元祖不可变一维数组  dictionaries哈希表 sets集合".encode('GB2312')
print  "list列表一维数组 tuple元祖不可变一维数组  dictionaries哈希表 sets集合".decode('utf-8').encode('gbk')

type = sys.getfilesystemencoding()
print  "list列表一维数组 tuple元祖不可变一维数组  dictionaries哈希表 sets集合".decode('utf-8').encode(type)
'''
list 列表 sample_list = [1,2,3,'abc']
tuple 数组 只读的序列 sample_tuple = (1,3,"ab")
dictionary 字典 sample_dic = {"key":value, 2:3}

数组下标0开始 tuplename=(tupleitem1,tupleitem2,tupleitem3,tupleitem4) 定义元组的是逗号
'''
sample_list = ['a',1,('a','b')]
print sample_list.__len__()
sample_list[2:2]=['2']

print sample_list
for i in sample_list: print(i)
print u"取值"
sample_list[1]
sample_list[-1]
print sample_list.__len__()
print sample_list[:]
print sample_list[0:2]
print sample_list[1:]
print sample_list[-2:-1]
print sample_list[::2]
str ="hello my friend"
print str
#str[:2]


print "Name: %s\
Number: %s\
String: %s" % ('myclass.name', 3, 3 * "-")


strString = """This is
a multiline
string."""
#可以使用取模运算符(%)和一个元组 使用方式是在目标字符串中从左至右使用%s来指代变量的位置，或者使用字典来代替，示例如下
print "This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"}

rangelist = range(10)
print rangelist

for number in rangelist:
    # Check if number is one of
    # the numbers in the tuple.
    print "ranglist for"
    if number in (3, 4, 7, 9):
        break
    else:
        # "Continue" starts the next iteration
        # of the loop. It's rather useless here,
        # as it's the last statement of the loop.
        continue
    #else:
    # The "else" clause is optional and is
    # executed only if the loop didn't "break".
    #pass # Do nothing

if rangelist[1] == 2:
    print "The second item (lists are 0-based) is 2"
elif rangelist[1] == 3:
    print "The second item (lists are 0-based) is 3"
else:
    print "Dunno"

#while rangelist[1] == 1:
#    pass

class MyClass(object):
    common = 10
    def __init__(self):
        self.myvariable = 3
    def myfunction(self, arg1, arg2):
        return self.myvariable
classinstance=MyClass()
print classinstance.myfunction(1, 2)

classinstance2=MyClass()
print classinstance2.common

MyClass.common=30
print classinstance.common
print classinstance2.common

classinstance.common =10
print classinstance.common
print classinstance2.common

MyClass.common = 50
print classinstance.common
print classinstance2.common

'''
class OtherClass(MyClass):
    def __init__(self,agr1):
        self.myvariable=3
        print arg1
classinstance =OtherClass("hello")
print classinstance
classinstance.myfunction(1, 2)
classinstance.test = 10
classinstance.test
'''
def some_function():
    try:
        10/0
    except ZeroDivisionError:
        print "oops,invaild"
    else:
        pass
    finally:
        print"we are done with that"
some_function()

myfile =open(r"c:\\LAB\\python\\python-cookbook-master\\python_file_name.txt","w")
pickle.dump(rangelist,myfile)
myfile.write("this is a string.")
myfile.close()

#类的基本定义和使用方法，这只体现了面向对象编程的三大特点之一：封装
print u"私有属性不可访问。通过实例方法访问私有"
class people:
    name = 'jack'
    age = 12

p = people()
print p.name,p.age

class people:
    __name = 'jack'
    __age = 12

p = people()
#错误 print p.__name,p.__age 私有属性不可访问。通过实例方法访问私有


class people:
    __name = 'jack'
    __age = 12

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

p = people()
print p.getName(),p.getAge()

print u"#实例对象 类对象不可以直接访问私有属性"
class people:
    name = 'jack'  #公有的类属性
    __age = 12     #私有的类属性

p = people()
print p.name             #正确
print people.name        #正确
#错误print p.__age，不能在类外通过实例对象访问私有的类属性
#错误print people.__age，不能在类外通过类对象访问私有的类属性

print u"# 类属性没定义age 不能通过类对象访问实例属性"

class people:
    name = 'jack'

p = people()
p.age =12
print p.name    #正确
print p.age     #正确

print people.name    #正确
#错误  print people.age    不能通过类对象访问实例属性

#产生了一个实例对象p，然后p.age = 12这句给p添加了一个实例属性age，赋值为12。这个实例属性是实例对象p所特有的，注意，类对象people并不拥有它（所以不能通过类对象来访问这个age属性）。
#？ 当然还可以在实例化对象的时候给age赋值。
class people:
    name = 'jack'

p = people()
p.age =12
print p.name    #正确
print p.age     #正确

print people.name    #正确
#错误print people.age    类对象无法访问实例对象属性



class people:
    name = 'jack'

    #__init__()是内置的构造方法，在实例化对象时自动调用
    def __init__(self,age):
        self.age = age

p = people(12)  #在实例化对象的时候给age赋值。
print p.name    #正确
print p.age     #正确

print people.name    #正确
#错误 print people.age

class people:
    country = 'china'


print people.country
p = people()
print p.country
p.country = 'japan'
print p.country      #实例属性会屏蔽掉同名的类属性.类对象不能访问实例属性
print people.country
del p.country    #删除实例属性
print p.country

print u"类方法"
class people:
    country = 'china'

    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

p = people()
print p.getCountry()    #可以用过实例对象引用
print people.getCountry()    #可以通过类对象引用

class people:
    country = 'china'

    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls,country):
        cls.country = country


p = people()
print p.getCountry()    #可以用过实例对象引用
print people.getCountry()    #可以通过类对象引用

p.setCountry('japan')

print p.getCountry()
print people.getCountry()

class people:
    country = 'china'

    #实例方法
    def getCountry(self):
        return self.country


p = people()
print p.getCountry()         #正确，可以用过实例对象引用
#错误print people.getCountry()  ，不能通过类对象引用实例方法

class people:
    country = 'china'

    @staticmethod
    #静态方法
    def getCountry():
        return people.country

print people.getCountry()     #静态方法必须通过类对象来引用

class UniversityMember:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

print u"继承和多态"
class Student(UniversityMember):

    def __init__(self,name,age,sno,mark):
        UniversityMember.__init__(self,name,age)     #注意要显示调用父类构造方法，并传递参数self
        self.sno = sno
        self.mark = mark

    def getSno(self):
        return self.sno

    def getMark(self):
        return self.mark



class Teacher(UniversityMember):

    def __init__(self,name,age,tno,salary):
        UniversityMember.__init__(self,name,age)
        self.tno = tno
        self.salary = salary

    def getTno(self):
        return self.tno

    def getSalary(self):
        return self.salary

T= Teacher("wangjie",30,21,8000)
S= Student("wangmazi",21,100,432)

print T.name,T.age,T.getTno(),T.getSalary()
print S.name,S.name,S.getSno(),S.getMark()

##函数的定义def 函数参数params可以是零个、一个或者多,return语句是可选的，它可以在函数体内任何地方出现，表示函数调用执行到此结束；如果没有return语句，会自动返回NONE，如果有return语句，但是return后面没有接表达式或者值的话也是返回NONE
# Python中不允许前向引用，即在函数定义之前，不允许调用该函数
def printHello():
    print 'hello'

def printNum():
    for i in range(0,10):
        print i
    return

def add(a,b):
    return a+b

print printHello()
print printNum()
print add(1,2)

##形参全称是形式参数，在用def关键字定义函数时函数名后面括号里的变量称作为形式参数。实参全称为实际参数，在调用函数时提供的值或者变量称作为实际参数。
#这里的a和b就是形参
def add(a,b):
    return a+b

#这里的1和2是实参
add(1,2)
x=2
y=3
#这里的x和y是实参
add(x,y)


#参数的传递和改变在Python中一切皆对象，变量中存放的是对象的引用
print id(5)
print id('python')
x=2
print id(x)
y='hello'
print id(y)

print '---------'
x=2
print id(2)
print id(x)
y='hello'
print id('hello')
print id(y)
##x看成是对象2的一个引用
#在Python中一切皆对象，像2，'hello'这样的值都是对象，只不过5是一个整型对象，而'hello'是一个字符串对象。上面的x=2，
# 在Python中实际的处理过程是这样的：先申请一段内存分配给一个整型对象来存储整型值2，然后让变量x去指向这个对象，实际上就是指向这段内存（这里有点和C语言中的指针类似）。
# 而id(2)和id(x)的结果一样，说明id函数在作用于变量时，其返回的是变量指向的对象的地址。因为变量也是对象，所以在这里可以将x看成是对象2的一个引用。


print '---------'
x=2
print id(x)
y=2
print id(y)
s='hello'
print id(s)
t=s
print id(t)
#t=s这句变量互相赋值，也相当于是让t指向了已经存在的字符串类型的对象'hello'

#########################再看以下例子
#?两次的id(x)的值不同，这个可能让人有点难以理解。注意，在Python中，单一元素的对象是不允许更改的，比如整型数据、字符串、浮点数等。x=3这句的执行过程并不是先获取x原来指向的对象的地址，再把内存中的值更改为3，而是新申请一段内存来存储对象3，再让x去指向对象3，所以两次id(x)的值不同。然而为何改变了L中的某个子元素的值后，id(L)的值没有发生改变？在Python中，复杂元素的对象是允许更改的，比如列表、字典、元组等。Python中变量存储的是对象的引用，对于列表，其id()值返回的是列表第一个子元素L[0]的存储地址。就像上面的例子，L=[1,2,3]，这里的L有三个子元素L[0]，L[1]，L[2]，L[0]、L[1]、L[2]分别指向对象1、2、3，id(L)值和对象3的存储地址相同，看下面这个图就明白了
#?因为L和M指向的是同一对象，所以在更改了L中子元素的值后，M也相应改变了，但是id(L)值并没有改变，因为这句L[0]=2只是让L[0]重新指向了对象2，而L[0]本身的存储地址并没有发生改变，所以id(L)的值没有改变（ id(L)的值实际等于L[0]本身的存储地址）。
print '---------'
L=[1,2,3]
print (L[2])

x=2
print ('id2', id(2))
print ('id2', id(x))
x=3
print ('id2', id(3))
print ('id2', id(x))
L=[1,2,3]
M=L
print "L"
print ('idL', id(L))
print ('idL', id(M))
print ('id3', id(L[2]))
L[0]=2
print (L[0])
print ('idL', id(L))
print M

print '---------'

def modify1(m,K):
    m=2
    K=[4,5,6]
    return

def modify2(m,K):
    m=2
    K[0]=0
    return

n=100
L=[1,2,3]
modify1(n,L)
print n
print L

modify2(n,L)
print n
print L
#?从结果可以看出，执行modify1( )之后，n和L都没有发生任何改变；执行modify2( )后，n还是没有改变，L发生了改变。因为在Python中参数传递采用的是值传递方式，在执行函数modify1时，先获取n和L的id( )值，然后为形参m和K分配空间，让m和K分别指向对象100和对象[1,2,3]。m=2这句让m重新指向对象2，而K=[4,5,6]这句让K重新指向对象[4,5,6]。这种改变并不会影响到实参n和L，所以在执行modify1之后，n和L没有发生任何改变；在执行函数modify2时，同理，让m和K分别指向对象2和对象[1,2,3]，然而K[0]=0让K[0]重新指向了对象0（注意这里K和L指向的是同一段内存），所以对K指向的内存数据进行的任何改变也会影响到L，因此在执行modify2后，L发生了改变。

print '---------'
#在Python中，也存在作用域这个问题。在Python中，会为每个层次生成一个符号表，里层能调用外层中的变量，而外层不能调用里层中的变量，并且当外层和里层有同名变量时，外层变量会被里层变量屏蔽掉。举个例子
def function():
    x=2
    count=2
    while count>0:
        x=3
        print x
        count=count-1

function()


#在函数function中，while循环外面和while循环里面都有变量x，此时，while循环外面的变量x会被屏蔽掉。注意在函数内部定义的变量作用域都仅限于函数内部，在函数外部是不能够调用的，一般称这种变量为局部变量。
#还有一种变量叫做全局变量，它是在函数外部定义的，作用域是整个文件。全局变量可以直接在函数里面应用，但是如果要在函数内部改变全局变量，必须使用global关键字进行声明。
x=2
def fun1():
    print x

def fun2():
    global x
    x=3
    print x

fun1()
fun2()
print x


a = 'python'
print 'hello,', a or 'world'

b = ''
print 'hello,', b or 'world'

L = [75, 92, 59, 68]
sum = 0.0
for x in L:
    sum=sum +x
print sum / 4

sum = 0
x = 1
while x <100:
    sum=sum+x
    x=x+2
print sum

sum = 0
x = 1
while True:
    sum = sum + x
    x = x + 2
    if x > 100:
        break
print sum

sum = 0
x = 1
n = 1
while True:
    if n>20:
        break
    sum=sum+x
    x = x * 2
    n =n+1
print sum


for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y

for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print x * 10 + y
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
print d
print d['Lisa']

d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
print d[95]

s = set(['Adam', 'adam', 'Lisa', 'lisa', 'Bart', 'bart', 'Paul', 'paul'])
print 'adam' in s
print 'bart' in s

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ':', x[1]

L = []
x=1
while True:
    if x==101:
        break
    L.append(x**2)
    x=x+1
print sum(L)
