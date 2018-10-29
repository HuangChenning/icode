# -* - coding: UTF-8 -* -
# Strings can be added too!
# 字符串也可以相加！
from __future__ import print_function

import print_log




####################################################
## 2. Variables and Collections
## 2. 变量和集合
####################################################

# Printing is pretty easy
# 打印输出很简单
# print("I'm Python. Nice to meet you!")

print_log.println("I'm Python. Nice to meet you!")

# No need to declare variables before assigning to them.
# 在赋值给变量之前不需要声明
some_var = 5  # Convention is to use lower_case_with_underscores

# 变量名的约定是使用下划线分隔的小写单词
print(some_var)  # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
# 访问一个未赋值的变量会产生一个异常。
# 进一步了解异常处理，可参见下一节《控制流》。

# 会抛出一个名称错误
# some_other_var  # Raises a name error


# 会报以下错误
# some_other_var  # Raises a name error
# NameError: name 'some_other_var' is not defined

# if can be used as an expression
# if 可以作为表达式来使用
print("yahoo!" if 3 > 2 else 2)  # => "yahoo!"

if 3 > 2:
    print("yahoo!")
else:
    print("2")

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


print_log.println('Lists store sequences')

# Lists store sequences
# 列表用于存储序列
# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 用索引来访问list中每一个位置的元素，记得索引是从0开始的

li = []

# You can start with a prefilled list
# 我们先尝试一个预先填充好的列表
other_li = [4, 5, 6]
print_log.printvar('other_li',other_li)
print('li is null', li)





print_log.println('Add stuff to the end of a list with append')


# Add stuff to the end of a list with append
# 使用 append 方法把元素添加到列表的尾部
li.append(1)  # li is now [1]

print_log.printvar('li append 1',li)

# li 现在是 [1]
li.append(2)  # li is now [1, 2]

print_log.printvar('li append 2',li)

# li 现在是 [1, 2]
li.append(4)  # li is now [1, 2, 4]

print_log.printvar('li append 4',li)

# li 现在是 [1, 2, 4]
li.append(3)  # li is now [1, 2, 4, 3]
print_log.printvar('li append 3',li)

# li 现在是 [1, 2, 4, 3]
# Remove from the end with pop
# 使用 pop 来移除最后一个元素
li.pop()  # => 3 and li is now [1, 2, 4]
print_log.printvar('li pop 3',li)

# => 3，然后 li 现在是 [1, 2, 4]
# Let's put it back
# 我们再把它放回去

li.append(3)  # li is now [1, 2, 4, 3] again.
# li 现在又是 [1, 2, 4, 3] 了

print_log.printvar('li append 3',li)




print_log.printvar('li[0] ', li[0])
print_log.printvar('li[1] ', li[1])
print_log.printvar('li[2] ', li[2])
print_log.printvar('li[3] ', li[3])


# 如果是负数的序号，则是倒序显示
print_log.printvar('li[-1] ', li[-1])
print_log.printvar('li[-2] ', li[-2])
print_log.printvar('li[-3] ', li[-3])
print_log.printvar('li[-4] ', li[-4])



# Looking out of bounds is an IndexError
# 越界查询会产生一个索引错误
# var_li4 = li[4]  # Raises an IndexError

# 抛出一个索引错误
# var_li4 = li[4]  # Raises an IndexError
# IndexError: list index out of range

# print(var_li4)

# 当然，倒数第5个就越界了。
# print(li[-5])

# print(li[-5])
# IndexError: list index out of range


var_li3 = li[3]

print(var_li3)


# 多维list
print('\n')


s = ['python', 'java', ['asp', 'php'], 'scheme']

print_log.printvar('s[0]',s[0])
print_log.printvar('s[1]',s[1])
print_log.printvar('s[2]',s[2])

print_log.printvar('s[2][0]',s[2][0])
print_log.printvar('s[2][1]',s[2][1])

print_log.printvar('s[3]',s[3])



# You can look at ranges with slice syntax.
# (It's a closed/open range for you mathy types.)
# 你可以使用切片语法来查询列表的一个范围。
# （这个范围相当于数学中的左闭右开区间。）


print_log.println('You can look at ranges with slice syntax')

# 取值范围为li[1]、li[2]

print_log.printvar('li[1:3]',li[1:3])


# 取值范围为li[2]、li[3]
# Omit the beginning


print_log.printvar('li[2:]',li[2:])

# 取值范围为li[0]、li[1]、li[2]
# Omit the end


print_log.printvar('li[:3]',li[:3])



# Remove arbitrary elements from a list with del
# 使用 del 来删除列表中的任意元素

print_log.println('Remove arbitrary elements from a list with del')

print(li)
del li[2]  # li is now [1, 2, 3]
# li 现在是 [1, 2, 3]

print(li)

print_log.println('You can add lists')

# You can add lists
# 可以把列表相加

print_log.printvar('li',li)
print_log.printvar('other_li',other_li)
print_log.printvar('li + other_li',li + other_li) # => [1, 2, 3, 4, 5, 6] - Note: li and other_li is left alone
# => [1, 2, 3, 4, 5, 6] - 请留意 li 和 other_li 并不会被修改




print_log.println('Concatenate lists with extend')

# Concatenate lists with extend
# 使用 extend 来合并列表

print_log.printvar('li',li)
print_log.printvar('other_li',other_li)


li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]
# 现在 li 是 [1, 2, 3, 4, 5, 6]


print_log.printvar('li extend other_li',li)
print_log.printvar('other_li',other_li)


# Check for existence in a list with in
# 用 in 来检查是否存在于某个列表中
1 in li  # => True

# print('1 in li is', 1 in li)

print_log.printvar('1 in li',1 in li)


# Examine the length with len
# 用 len 来检测列表的长度

print_log.printvar('li\'s length ',len(li))   # => 6



print_log.println('Tuples are like lists but are immutable')

# Tuples are like lists but are immutable.
# 元组很像列表，但它是“不可变”的。


# print (tup[0])  # => 1


# tup[0] = 3  # Raises a TypeError
# 抛出一个类型错误
# tup[0] = 3  # Raises a TypeError
# TypeError: 'tuple' object does not support item assignment



# You can do all those list thingies on tuples too
# 操作列表的方式通常也能用在元组身上

print_log.println('You can do all those list thingies on tuples too')

tup = (1, 2, 3)

print_log.printvar('tup',tup)

print_log.printvar('tup length',len(tup))  # => 3

# tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)

print_log.printvar('tup + (4, 5, 6)',tup + (4, 5, 6) )

# tup[:2]  # => (1, 2)

print_log.printvar('tup[:2]',tup[:2])


2 in tup  # => True

print_log.printvar('2 in tup',2 in tup)





# tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
# 它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：

# >>> t = (1, 2)
# >>> t
# (1, 2)
# 如果要定义一个空的tuple，可以写成()：
#
# >>> t = ()
# >>> t
# ()
# 但是，要定义一个只有1个元素的tuple，如果你这么定义：
#
# >>> t = (1)
# >>> t
# 1
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
#
# >>> t = (1,)
# >>> t
# (1,)
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
#
# 最后来看一个“可变的”tuple：

# >>> t = ('a', 'b', ['A', 'B'])
# >>> t[2][0] = 'X'
# >>> t[2][1] = 'Y'
# >>> t
# ('a', 'b', ['X', 'Y'])
# 这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
#
#
# tup = (1, 2, 3)


# You can unpack tuples (or lists) into variables
# 你可以把元组（或列表）中的元素解包赋值给多个变量
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# 现在 a 是 1，b 是 2，c 是 3
# Tuples are created by default if you leave out the parentheses
# 如果你省去了小括号，那么元组会被自动创建
d, e, f = 4, 5, 6
# Now look how easy it is to swap two values



print_log.printvar('a',a)
print_log.printvar('b',b)
print_log.printvar('c',c)

print_log.printvar('d',d)
print_log.printvar('e',e)
print_log.printvar('f',f)

# 再来看看交换两个值是多么简单。
e, d = d, e  # d is now 5 and e is now 4
# 现在 d 是 5 而 e 是 4

print_log.printvar('d',d)
print_log.printvar('e',e)



filled_dict = {"one": 1, "two": 2, "three": 3}

print_log.printvar("filled_dict.values()",filled_dict.values())


