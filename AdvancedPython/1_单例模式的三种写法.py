# singleton pattern的三种写法   -- 2023.02.23

# # 方法一：装饰器模式
# def singleton(cls):
#     print("step1")
#
#     def inner(*args, **kwargs):
#         print('step2')
#         if hasattr(cls, '__instance'):
#             return getattr(cls, '__instance')
#         obj = cls()
#         setattr(cls, '__instance', obj)
#         return obj
#     print('step3')
#     return inner
#
#
# @singleton
# class Person:
#     pass


# # 方法二：闭包
# def singleton2(cls):
#     _instance = {}
#     print('step1')
#
#     def inner(*args, **kwargs):
#         print('step2')
#         if cls not in _instance:
#             print('step3')
#             obj = cls()
#             _instance[cls] = obj
#         return _instance[cls]
#
#     print('step4')
#     return inner
#
#
# @singleton2
# class Person:
#     pass


# # 方法三：metaclass方式
# class singletonMeta(type):  # 继承type类
#     print('step1')
#
#     def __call__(cls, * args, **kwargs):
#         print('step2')
#         if hasattr(cls, '_instance'):  # 注意，检查的不是实例属性，而是类属性
#             print('step3')
#             return getattr(cls, '_instance')
#         obj = super().__call__(*args, **kwargs)
#         setattr(cls, '_instance', obj)
#         return obj
#
#
# class Person(metaclass=singletonMeta):  # 不用装饰器的模式了，改用metaclass的方式
#     def __init__(self, a):
#         self.a = [a]
#     pass
#
#
# if __name__ == '__main__':
#     p1 = Person(1)
#     p1.a.append(3)
#     print(p1.a)
#     p2 = Person(2)
#     print(p1 is p2)
#     print(p1.a)
#     print(p2.a)



# class A():
#     _instance = None
#     def __init__(self, x) -> None:
#         self.a = [x]
#     def __new__(cls, *args, **kargs):
#         if cls._instance is None:
#             cls._instance = super(A, cls).__new__(cls)
#         return cls._instance
#
# a = A(1)
# a.a.append(2)
# print(a.a)
# b = A(1)
#
# print(id(a)==id(b))
# print(a.a)


# # 新创建对象的时候，对象的值会被重置。
# class A():
#     # _instance = None
#     def __init__(self, x) -> None:
#         self.a = [x]  # 当下面函数返回值是实例对象时，每次新建对象就会调用此处的__init__函数
#     def __new__(cls, *args, **kargs):
#         if hasattr(cls, '_instance'):
#             return getattr(cls, '_instance')
#         # obj = super(A, cls).__new__(cls)
#         obj = super().__new__(cls)
#         setattr(cls, '_instance', obj)
#         return obj
#
# a = A(1)
# a.a.append(2)
# print(a.a)
# b = A(1)
#
# print(id(a)==id(b))
# print(a.a)

# 第2遍  2023.03.01
# # 1. 装饰器方法实现单例模式
# def singleton(cls):
#     def inner(*args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             obj = cls(*args, **kwargs)
#             setattr(cls, '_instance', obj)
#             # return getattr(cls, '_instance')
#             return obj
#         return getattr(cls, '_instance')
#     return inner
#
# @singleton
# class Person:
#     def __init__(self, a):
#         self.s = [a]
#     pass
#
# p1 = Person(1)
# p1.s.append(3)
# print(p1.s)  # [1, 3]
# p2 = Person(2)  # [1, 3]
# print(p1.s)
# print(p1 is p2)  # True
#
# #  2.闭包实现单例模式
# def singletone(cls):
#     _instance = {}
#
#     def inner(*args, **kwargs):
#         if cls not in _instance:
#             obj = cls(*args, **kwargs)
#             _instance[cls] = obj
#             return obj
#         return _instance[cls]
#     return inner
#
# @singletone
# class Person:
#     def __init__(self, a):
#         self.s = [a]
#
# p1 = Person(1)
# p1.s.append(3)
# print(p1.s)  # [1, 3]
# p2 = Person(2)
# print(p1.s)  # [1, 3]
# print(p1 is p2)  # True


# 3. 使用metaclass方法实现单例模式

