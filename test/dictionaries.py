# -* - coding: UTF-8 -* -
import print_log



# Dictionaries store mappings
# 字典用于存储映射关系
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
#
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
#
# >>> key = [1, 2, 3]
# >>> d[key] = 'a list'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'list'


empty_dict = {}
# Here is a prefilled dictionary
# 这是一个预先填充的字典


filled_dict = {"one": 1, "two": 2, "three": 3}

# Look up values with []
# 使用 [] 来查询键值
filled_dict["one"]  # => 1

print_log.printvar('filled_dict[\"one\"]', filled_dict["one"])

# Get all keys as a list
# 将字典的所有键名获取为一个列表
filled_dict.keys()  # => ["three", "two", "one"]

print_log.printvar('filled_dict.keys()', filled_dict.keys())

# Note - Dictionary key ordering is not guaranteed.
# Your results might not match this exactly.
# 请注意：无法保证字典键名的顺序如何排列。
# 你得到的结果可能跟上面的示例不一致。

# Get all values as a list
# 将字典的所有键值获取为一个列表

filled_dict.values()  # => [3, 2, 1]

print_log.printvar('filled_dict.values()', filled_dict.values())

# Note - Same as above regarding key ordering.
# 请注意：顺序的问题和上面一样。

# Check for existence of keys in a dictionary with in
# 使用 in 来检查一个字典是否包含某个键名
"one" in filled_dict  # => True
1 in filled_dict  # => False

print_log.printvar('"one" in filled_dict', "one" in filled_dict)

print_log.printvar('1 in filled_dict ', 1 in filled_dict)

# Looking up a non-existing key is a KeyError
# 查询一个不存在的键名会产生一个键名错误

# filled_dict["four"]  # KeyError
# 键名错误
# filled_dict["four"]  # KeyError
# KeyError: 'four'


print_log.println('Use get method to avoid the KeyError')
# Use get method to avoid the KeyError
# 所以要使用 get 方法来避免键名错误
filled_dict.get("one")  # => 1
filled_dict.get("four")  # => None

print_log.printvar('filled_dict.get("one") ', filled_dict.get("one"))
print_log.printvar('filled_dict.get("four") ', filled_dict.get("four"))

print_log.println('The get method supports a default argument when the value is missing')
# The get method supports a default argument when the value is missing
# get 方法支持传入一个默认值参数，将在取不到值时返回。
filled_dict.get("one", 4)  # => 1
filled_dict.get("four", 4)  # => 4

print_log.printvar('filled_dict.get("one", 4) ', filled_dict.get("one", 4))
print_log.printvar('filled_dict.get("four", 4) ', filled_dict.get("four", 4))

# Setdefault method is a safe way to add new key-value pair into dictionary
# Setdefault 方法可以安全地把新的名值对添加到字典里
print_log.println('Setdefault method is a safe way to add new key-value pair into dictionary')

filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
# filled_dict["five"] 被设置为 5

print_log.printvar('filled_dict.keys()', filled_dict.keys())

print_log.printvar('filled_dict.values()', filled_dict.values())

filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5
# filled_dict["five"] 仍然为 5

print_log.println('filled_dict.setdefault("five", 6) ')
print_log.printvar('filled_dict.values()', filled_dict.values())
