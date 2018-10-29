# -* - coding: UTF-8 -* -
# Strings can be added too!
# 字符串也可以相加！
from __future__ import print_function

# "Hello " + "world!"  # => "Hello world!"


####################################################
## 1. Primitive Datatypes and Operators
## 1. 基本数据类型和操作符
####################################################

print("hello," + "world" + "!")

# % can be used to format strings, like this:
# % 可以用来格式化字符串，就像这样：
print("%s can be %s" % ("strings", "interpolated"))

# A newer way to format strings is the format method.
# This method is the preferred way
# 后来又有一种格式化字符串的新方法：format 方法。
# 我们推荐使用这个方法。
print("{0} can be {1}".format("strings", "formatted"))

# You can use keywords if you don't want to count.
# 如果你不喜欢数数的话，可以使用关键字（变量）。
print("{name} wants to eat {food}".format(name="Bob", food="lasagna"))

# None is an object
# None 是一个对象
# None  # => None

# Don't use the equality `==` symbol to compare objects to None
# Use `is` instead
# 不要使用相等符号 `==` 来把对象和 None 进行比较，
# 而要用 `is`。


print("etc" is None)  # => False
print(None is None)  # => True



# The 'is' operator tests for object identity. This isn't
# very useful when dealing with primitive values, but is
# very useful when dealing with objects.
# 这个 `is` 操作符用于比较两个对象的标识。
# （译注：对象一旦建立，其标识就不会改变，可以认为它就是对象的内存地址。）
# 在处理基本数据类型时基本用不上，
# 但它在处理对象时很有用。

# None, 0, and empty strings/lists all evaluate to False.
# All other values are True
# None、0 以及空字符串和空列表都等于 False，
# 除此以外的所有值都等于 True。

# => True
print(0 == False)


print("" == False)  # => True
