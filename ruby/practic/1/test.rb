class Person
  def say
    puts "hello"
  end
end
tom=Person.new
tom.say

def tom.bye
  puts "bye"
end
def tom.bye
puts "bye1"
end
tom.bye

class Person
  def touch
    puts "touch"
  end
end
tom.say
tom.touch
tom.bye

class Person

  def say
    @start="today"
  end

  def bye
    puts "we meets #{@start}"
  end

end
tom=Person.new
tom.say
tom.bye

class Person
  def initialize(age,sex)
    @age=age
    @sex=sex
  end
  def age
    @age
  end
  def sex
    @sex
  end
end

tom=Person.new(20,"boy")
puts tom.sex
puts tom.age
=begin
class Person
  def age=(age)
    @age=age
  end
  def age
    @age
  end
end
tom=Person.new
tom.age=(21)
puts tom.age
=end
=begin
#1. 计算器：
puts "Please input Number1:"
number1 = gets
puts "Please input a operator(+,-,*,/):"
op = gets
puts "Please input Number2:"
number2 = gets
case op.chomp
  when "+"
    result = number1.to_i + number2.to_i
  when "-"
    result = number1.to_i - number2.to_i
  when "*"
    result = number1.to_i * number2.to_i
  when "/"
    result = number1.to_i / number2.to_i
end
puts "Result: #{number1.chomp} #{op.chomp} #{number2.chomp} = #{result}"
=end

#2.在项目中访问变量：

$qj="We can see the social progressing from the following phenomenon:"
class TestCL
  CHANGE = "In changing..."
  before = "We are living in the grass house"
  now = "We are living in the tall buildings"
  future = "We are living in the sky buildings"
  puts CHANGE + "\n" + $qj + "\n before : " + before + "\n now :" + now + "\n future :" + future
end

#3. 范围range的常用方法

a=0..59
b=60...100
c=b.to_a
puts "The minimum value in range a is: " + (a.min).to_s
puts "The maximum value in range b is: " + (b.max).to_s
puts "The last value in range a is: " + (a.end).to_s
puts "The first value in range b is: " + (b.first).to_s
puts b.include?100
puts "The length of array c is: " + (c.size).to_s

#范围对象的常用迭代器方法

count=10..20
print count.reject{ |i| i<15}
puts "\n"
print count.select{ |i| i<15}
puts "\n"
count.each do |i|
  puts "The current item is: " + i.to_s
end

alph="A".."J"
alph.each do |i|
  puts "The current item is: " + i.to_s
end

#5.使用Ruby语言的基本数据类型写一个比较字符串内容和字符串对象的小例子

cpContent="I am the compared content"
cContent=:"I am the compared content"
puts "The result of compare content with method to_sym: ",cpContent.to_sym==cContent
puts "The result of compare content with method to_s: ",cContent.to_s==cpContent

cpObject="I am the compared object"
cObject=:cpObject
cObjectS=%s{cpObject}
puts "The result of compare object is: ",cObjectS==cObject

#6. 辨别该数值是否属于一个范围

puts (1..12)===8

#7. 判断用户是否通过审核？ 从数据库中读取状态的值0或1，然后使用三目运算符

#puts statusY=1 ? "已审核" : '未审核'

#8. 使用if流程语言也可以有返回值
score=569
res=if score > 600
      score.to_s + "There is out of question to get access to the FuDan University!"
    else
      score.to_s + "score, I'm so embarrassment, I'm failed, \n It's really pity that I failed to access FuDan, but it is OK, I'll try it again from the beginning."
    end
puts res

#9. 并行赋值

c,d="I'm variable c","I'm variable d"
puts "The variable c before exchange " +c, "The variable d before exchange " + d
c,d=d,c
puts "The variable c before exchange " +c, "The variable d before exchange " + d

--------------------------------------------------------------------------------------

weather=["Spring","Summer","Autumn","Winter"]
eg=["sp represent the warmer Spring(77F)","su represents the hot Summer(95F)","au represents the cool Autumn(59F)","wi represents the cold Winter(41F)"]
a,b=weather
puts "a presents " + a, "b persents " +b
a, *b=eg
puts "a presents " + a +"\n array b presents " ,b
a,b="rain and wind Harward road", *weather
puts a,b

#10.跟我一起操作字符串
=begin
#encoding:gbk
str1="登岳阳楼\n"
str2="昔闻洞庭水，今上岳阳楼\n"
str3="吴楚东南坼，乾坤日夜浮\n"
str4="亲朋无一字，老病有孤舟\n"
str5="戎马关山北，凭轩涕泗流\n"
str6=str1+str2+str3+str4+str5
puts str6
str="this is an ancient poetry"
puts str6.replace(str)
puts str6.dup
puts str6.capitalize
puts str6[11,14]
puts str6<=>str

#11. 使用哈希表保存学生成绩

math_score={
    "王红"=>100,
    "岳峰"=>99,
    "李佳路"=>98,
    "张小春"=>97,
    "关世晓"=>94
}
puts "This record "+math_score.size.to_s+" students' math score."
puts "With each method to output every student's math score: "
math_score.each { |key, value| puts key.to_s + ": " +value.to_s }

#11. 使用哈希表保存学生成绩

math_score={
 "王红"=>100,
 "岳峰"=>99,
 "李佳路"=>98,
 "张小春"=>97,
 "关世晓"=>94
}
puts "This record "+math_score.size.to_s+" students' math score."
puts "With each method to output every student's math score: "
math_score.each do |key, value|
 puts key.to_s + ": " +value.to_s
end

======================================================================================

#12.使用数组保存学生成绩

#encoding:gbk
score_array=["王红:100","岳峰:99","李佳路:98","张小春:98","关世晓:97"]
score_array[5]="于小六:96"
puts "The new array after add the new element: "
puts score_array
score_array.unshift("李云龙:100")
score_array.push("张顺:95")
puts "The new array after add the element at the begin and end of the array: "
puts score_array
puts "The first two student's score: "
puts score_array[0,2]

==================================================================================

#13. 制作手机报价表

brand = "Nokia"
model = "5000"
color = "Purple"
listing_date = "May 2008"
price = "410"
sale = 0.8
puts "Brand: " + brand
puts "Model: " + model
puts "Color: " + color
puts "Lifting date: " + listing_date
puts "Marketing Price: " + price
puts "Sale: " + (price.to_i*sale).to_s

==========================================================================================

#14. Ruby求素数的算法

$arr = []
$arr[0] = 2
def add_prime(n)
 3.step(n,2) {|num| $arr << num if is_prime? num }
end
def is_prime?(number)
 j = 0
 while $arr[j] * $arr[j] <= number
  return false if number % $arr[j] == 0
  j += 1
 end
 return true
end
add_prime(50)
print $arr.join(", "), "\n"

==============================================================================================

#15. 为计算器类添加处理方法

class Counter
 def add(n1,n2)
  n1+n2
 end

 def subtract(n1,n2)
  n1-n2
 end

 def ride(n1,n2)
  n1*n2
 end

 def divide(n1,n2)
  n1/n2
 end
end

c = Counter.new
puts "8+4=#{c.add(8,4)}"
puts "8-4=#{c.subtract(8,4)}"
puts "8*4=#{c.ride(8,4)}"
puts "8/4=#{c.divide(8,4)}"

===================================================================================

#16. 创建一个会自我介绍的人

class Person
 def setName(name)
  @name = name
 end
 def setAge(age)
  @age = age
 end
 def setIsMale(isMale)
  @isMale = isMale
 end
 def say
  sex = @isMale ? "Little Boy" : "Little Girl"
  puts "Hello, everyone, My name is #{@name}, I'm a #{sex}, and I'm #{@age} years old"
 end
end

lzm = Person.new
lzm.setName("Lizzy")
lzm.setAge(22)
lzm.setIsMale(false)
lzm.say

================================================================================

#17. 抽象出一辆跑车

class Roadster
 def init
  @brand="BYD"
  @color="yellow"
  @weight="1800kg"
  @F_zero="210km/h"
 end
 attr :brand, false
 attr_accessor :color
 attr_reader :weight, :F_zero
end

def showCar(car)
 puts "================================"
 puts "The brand of this car is: " + car.brand
 puts "The color of this car is: " + car.color
 puts "The highest speed of this car is: " + car.F_zero
 puts "The weight of this car is: " + car.weight
end

roadster = Roadster.new
roadster.init
showCar(roadster)
roadster.color = "red"
showCar(roadster)

==============================================================================

#18.使用代码块实现一个迭代器

class Student
 def initialize(number, name)
  @number=number
  @name=name
 end

 attr_accessor :number, :name
end

def each(stus)
 for stu in stus
  yield(stu)
  puts stu.number + "\t" + stu.name
 end
end

students=Array.new
students[0]=Student.new("001", "Zhang Wen")
students[1]=Student.new("002", "Li Bei")
students[2]=Student.new("003", "Liu Jingsheng")

each(students) do
 |stu| stu.number= "stu" + stu.number
end

=========================================================



=end


