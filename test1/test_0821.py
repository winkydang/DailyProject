# 创建一个字典
my_dict = {'apple': 3, 'banana': 5, 'cherry': 2}

# 使用 items() 方法获取字典的键值对集合，类型为 dict_items
dict_items = my_dict.items()

# 打印 dict_items 类型和内容
print(type(dict_items))  # 输出：<class 'dict_items'>
print(dict_items)  # 输出：dict_items([('apple', 3), ('banana', 5), ('cherry', 2)])
print('*'*50)
# 遍历 dict_items
for key, value in dict_items:
    print(key, value)
print('*'*50)

for k in my_dict.keys():
    print(k)
print('*'*50)

for v in my_dict.values():
    print(v)
print('*'*50)

for k, v in my_dict.items():
    print(k, v)

# 输出：
# apple 3
# banana 5
# cherry 2
