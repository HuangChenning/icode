#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/10 00:54
# @Author  : Huangcn
# @Site    : 
# @File    : control_flow.py
# @Software: PyCharm
# @contact: chenning.huang@enmotech.com
# @desc: Control Flow Test

import print_log

# Let's just make a variable
# 我们先创建一个变量
some_var = 5

# Here is an if statement. Indentation is significant in python!
# prints "some_var is smaller than 10"
# 这里有一个条件语句。缩进在 Python 中可是很重要的哦！
# 程序会打印出 "some_var is smaller than 10"
# （译注：意为“some_var 比 10 小”。）
print_log.println('Here is an if statement. Indentation is significant in python!')
if some_var > 10:
    print "some_var is totally bigger than 10."
    # （译注：意为“some_var 完全比 10 大”。）
elif some_var < 10:  # This elif clause is optional.
    # 这里的 elif 子句是可选的
    print "some_var is smaller than 10."
    # （译注：意为“some_var 比 10 小”。）
else:  # This is optional too.
    # 这一句也是可选的
    print "some_var is indeed 10."
    # （译注：意为“some_var 就是 10”。）

# For loops iterate over lists
# for 循环可以遍历列表
# prints:
# 如果要打印出：
#     dog is a mammal
#     cat is a mammal
#     mouse is a mammal
print_log.println('For loops iterate over lists')
for animal in ["dog", "cat", "mouse"]:
    # You can use % to interpolate formatted strings
    # 别忘了你可以使用 % 来格式化字符串
    print "%s is a mammal" % animal
    # （译注：意为“%s 是哺乳动物”。）

# `range(number)` returns a list of numbers
# from zero to the given number
# `range(数字)` 会返回一个数字列表，
# 这个列表将包含从零到给定的数字。
# prints:
# 如果要打印出：
#     0
#     1
#     2
#     3
print_log.println('from zero to the given number')

print_log.printvar('range(4)', range(4))

for i in range(4):
    print i

# While loops go until a condition is no longer met.
# while 循环会一直继续，直到条件不再满足。
# prints:
# 如果要打印出：
#     0
#     1
#     2
#     3

print_log.println('While loops go until a condition is no longer met.')
x = 0
while x < 4:
    print x
    x += 1  # Shorthand for x = x + 1
    # 这是 x = x + 1 的简写方式

# Handle exceptions with a try/except block
# 使用 try/except 代码块来处理异常

# Works on Python 2.6 and up:
# 适用于 Python 2.6 及以上版本：

print_log.println('Handle exceptions with a try/except block.')
try:
    # Use raise to raise an error
    # 使用 raise 来抛出一个错误
    raise IndexError("This is an index error")
    # 抛出一个索引错误：“这是一个索引错误”。
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here.
    # pass 只是一个空操作。通常你应该在这里做一些恢复工作。
