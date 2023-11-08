# def divide(a, b):
#     assert b != 0, "除数不能为0"
#     return a / b
#
# # 正常情况
# print(divide(10, 2))  # 输出 5.0
#
# # 引发 AssertionError
# divide(10, 0)  # AssertionError: 除数不能为0
# # print(divide(10, 0))  # AssertionError: 除数不能为0


# def calculate_age(year_of_birth, current_year):
#     assert current_year >= year_of_birth, "当前年份必须大于出生年份"
#     return current_year - year_of_birth
#
# # 正常情况
# age = calculate_age(1980, 2023)  # 输出 43
# print(age)
#
# # 引发 AssertionError
# age = calculate_age(2023, 1980)  # AssertionError: 当前年份必须大于出生年份

# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "只能添加正数"
#     return x + y
#
# # 正常情况
# print(add_positive_numbers(1, 2))  # 输出 3
#
# # 测试一个条件不满足时的情况
# try:
#     print(add_positive_numbers(-1, 2))  # AssertionError: 只能添加正数
# except AssertionError as error:
#     print(error)
# print('end')

# class Person:
#     def __init__(self, name, age):
#         assert isinstance(name, str), "名字必须是字符串"
#         assert isinstance(age, int), "年龄必须是整数"
#         assert age > 0, "年龄必须大于0"
#
#         self.name = name
#         self.age = age
#
#
# # 正常情况
# p = Person("Alice", 30)
#
# # 不合法的输入
# try:
#     p = Person("Alice", -5)  # AssertionError: 年龄必须大于0
# except AssertionError as error:
#     print(error)



