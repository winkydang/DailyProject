# 1。 生成器的异常处理
# def generator_with_exception():
#     yield 1
#     yield 2
#     raise ValueError("An error occurred")
#
# gen = generator_with_exception()
#
# try:
#     for value in gen:
#         print(value)
# except ValueError as e:
#     print(f"Caught an exception: {e}")


# # 2。 生成器的发送值
# def generator_with_input():
#     while True:
#         received = yield
#         print(f"Received: {received}")
#
#
# gen = generator_with_input()
# next(gen)  # 启动生成器
# gen.send("Hello")

# # 3。生成器的状态保存和恢复
# import itertools
#
#
# def generator_with_shared_state():
#     for i in range(1, 4):
#         yield i
#
# gen = generator_with_shared_state()
# gen1, gen2 = itertools.tee(gen, 2)  # 使用 itertools.tee 函数来创建多个生成器，它们都共享相同的状态。
#
# print(list(gen1))  # 输出 [1, 2, 3]
# print(list(gen2))  # 输出 [1, 2, 3]

# 4。生成器表达式的惰性计算
# data = [x for x in range(1, 1000000)]  # 列表推导式，立即生成所有值
# gen = (x for x in range(1, 1000000))  # 生成器表达式，惰性生成值
# print(data[10])  # 11
# print(gen[10])  # TypeError: 'generator' object is not subscriptable


# # 生成器（Generators）通常是一种惰性计算的机制，它们不支持随机访问，因为生成器在生成值时通常不会将所有值存储在内存中，而是按需生成。因此，要随机访问生成器中的某个位置的值，你需要将生成器的值迭代到目标位置，然后获取该位置的值。
# # 以下是一种方法，通过迭代生成器来访问特定位置的值：
# def generate_numbers(n):
#     for i in range(1, n + 1):
#         yield i
#
#
# # 创建生成器
# gen = generate_numbers(10)
#
# # 随机访问生成器中的第 5 个值
# target_position = 5
# for _ in range(target_position - 1):
#     next(gen)  # 迭代到目标位置的前一个位置
#
# value_at_target_position = next(gen)  # 获取目标位置的值
# print(value_at_target_position)  # 输出：5


# # # 5。生成器的嵌套
# import itertools
# def generator_with_shared_state():
#     for i in range(1, 4):
#         yield i
#
# gen = generator_with_shared_state()
# gen1, gen2 = itertools.tee(gen, 2)
#
# def generator_chain():
#     yield from gen1
#     yield from gen2
#
# tmp = generator_chain()
# print(tmp)  # <generator object generator_chain at 0x104bc34a0>
# for item in tmp:
#     print(item)

# 使用 itertools.tee 函数来创建多个生成器，它们都共享相同的状态
# import itertools
#
# # 创建一个迭代器
# original_iter = iter([1, 2, 3, 4, 5])
#
# # 使用 tee() 函数创建两个生成器对象
# gen1, gen2 = itertools.tee(original_iter, 2)
#
# # 迭代 gen1 和 gen2
# for value in gen1:
#     print("gen1:", value)
#
# for value in gen2:
#     print("gen2:", value)
# 输出如下：
# gen1: 1
# gen1: 2
# gen1: 3
# gen1: 4
# gen1: 5
# gen2: 1
# gen2: 2
# gen2: 3
# gen2: 4
# gen2: 5

# # 嵌套使用生成器
# def generate_numbers(n):
#     for i in range(1, n + 1):
#         yield i
#
# def filter_even(iterable):
#     for num in iterable:
#         if num % 2 == 0:
#             yield num
#
# numbers = generate_numbers(10)
# even_numbers = filter_even(numbers)
#
# for num in even_numbers:
#     print(num)
# # 2
# # 4
# # 6
# # 8
# # 10

# # 使用yield from实现生成器嵌套
# def generate_numbers(n):
#     for i in range(1, n + 1):
#         yield i
#
# def filter_even(iterable):
#     yield from (num for num in iterable if num % 2 == 0)
#
# numbers = generate_numbers(10)
# even_numbers = filter_even(numbers)
#
# for num in even_numbers:
#     print(num)


# 生成器的嵌套使用
def generator1():
    yield "A"
    yield "B"
    yield "C"

def generator2():
    yield 1
    yield 2
    yield 3

def generator_chain():
    yield from generator1()
    yield from generator2()

# 调用 generator_chain() 函数，创建生成器对象
gen = generator_chain()

# 迭代生成器并获取值
for value in gen:
    print(value)





