# # 装饰器定义
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         # 在调用原始函数之前可以添加一些额外的操作
#         print("Before the function is called")
#         print("Welcome next student:")
#         # args = args + ('tom',)   # 元组是不可变类型。这种元组相加的方式会生成一个新的元组。想添加元素最好用list这种可变数据类型。
#         result = func(*args, **kwargs)
#         # 在调用原始函数之后可以添加一些额外的操作
#         print("After the function is called")
#         print(f"Thank you lovely {args}")  # Thank you lovely ('Alice',)
#         args = args[0].strip("'")
#         print(f"Thank you lovely {args}")  # Thank you lovely Alice
#         return result
#     return wrapper
#
# # 使用装饰器
# @my_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# # 调用被装饰后的函数
# say_hello("Alice")


# # 1. 接受参数的装饰器
# # 这个示例中的 repeat 装饰器接受一个整数 n 作为参数，然后返回一个装饰器函数。装饰器函数 decorator 再次返回一个新函数 wrapper，它会多次执行被装饰的函数。
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @repeat(3)
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("Alice")
# # Hello, Alice!
# # Hello, Alice!
# # Hello, Alice!


# # 2. 多个装饰器
# "加载装饰器时是从上到下，从外到内依次加载装饰器并调用函数。函数调用完再从内到外依次退出装饰器"
# def decorator1(func):
#     def wrapper(*args, **kwargs):
#         print("Decorator 1 - Before")
#         result = func(*args, **kwargs)
#         print("Decorator 1 - After")
#         return result
#     return wrapper
#
# def decorator2(func):
#     def wrapper(*args, **kwargs):
#         print("Decorator 2 - Before")
#         result = func(*args, **kwargs)
#         print("Decorator 2 - After")
#         return result
#     return wrapper
#
# @decorator1
# @decorator2
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("Bob")
# # Decorator 1 - Before
# # Decorator 2 - Before
# # Hello, Bob!
# # Decorator 2 - After
# # Decorator 1 - After

# 3. 类装饰器
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before the function is called")
        result = self.func(*args, **kwargs)
        print("After the function is called")
        return result

@MyDecorator
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Eve")  # 这种用法也是正确的
# Before the function is called
# Hello, Eve!
# After the function is called

# m = say_hello("Eve")  # m: None
# m()  # TypeError: 'NoneType' object is not callable


t = MyDecorator(say_hello("winky"))  # 这种用法也是正确的
# t()  # TypeError: 'NoneType' object is not callable    # 这里t拿到的是装饰器MyDecorator的__call__返回的result，result是None，不可被调用not callable
# Before the function is called
# Hello, winky!
# After the function is called
