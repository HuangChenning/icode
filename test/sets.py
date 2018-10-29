# -* - coding: UTF-8 -* -

import print_log

# Sets store ... well sets
# set 用于保存集合

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#
# 要创建一个set，需要提供一个list作为输入集合：




empty_set = set()
# Initialize a set with a bunch of values
# 使用一堆值来初始化一个集合


print_log.println('Initialize a set with a bunch of values')

some_set = set([1, 2, 2, 3, 4])  # some_set is now set([1, 2, 3, 4])
# some_set 现在是 set([1, 2, 3, 4])

print_log.printvar('some_set', some_set)

# >>> s = set([1, 2, 3])
# >>> s
# set([1, 2, 3])
# 注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。
#
# 重复元素在set中自动被过滤：
#
# >>> s = set([1, 1, 2, 2, 3, 3])
# >>> s
# set([1, 2, 3])


# Since Python 2.7, {} can be used to declare a set
# 从 Python 2.7 开始，{} 可以用来声明一个集合
filled_set = {1, 2, 2, 3, 4}  # => {1, 2, 3, 4}

# （译注：集合是种无序不重复的元素集，因此重复的 2 被滤除了。）
# （译注：{} 不会创建一个空集合，只会创建一个空字典。）


print_log.printvar('filled_set = {1, 2, 2, 3, 4} ', filled_set)

# Add more items to a set
# 把更多的元素添加进一个集合
print_log.println('Add more items to a set')

filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}
# filled_set 现在是 {1, 2, 3, 4, 5}

print_log.printvar('filled_set.add(5) ', filled_set)

# Do set intersection with &
# 使用 & 来获取交集

print_log.println('Do set intersection with &')

other_set = {3, 4, 5, 6}
filled_set & other_set  # => {3, 4, 5}

print_log.printvar('filled_set',filled_set)
print_log.printvar('other_set',other_set)
print_log.printvar('filled_set & other_set',filled_set & other_set)


# Do set union with |
# 使用 | 来获取并集

print_log.println('Do set union with')
filled_set | other_set  # => {1, 2, 3, 4, 5, 6}

print_log.printvar('filled_set',filled_set)
print_log.printvar('other_set',other_set)
print_log.printvar('filled_set | other_set',filled_set | other_set)


# Do set difference with -
# 使用 - 来获取补集
print_log.println('Do set difference with')
{1, 2, 3, 4} - {2, 3, 5}  # => {1, 4}
print_log.printvar('{1, 2, 3, 4} - {2, 3, 5}',{1, 2, 3, 4} - {2, 3, 5})


# Check for existence in a set with in
# 使用 in 来检查是否存在于某个集合中

print_log.println('Check for existence in a set with in')
2 in filled_set  # => True
10 in filled_set  # => False


print_log.printvar('2 in filled_set',2 in filled_set)
print_log.printvar('10 in filled_set',10 in filled_set)