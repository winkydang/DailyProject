def singleton(cls):
    __instance = {}
    print('step1')

    def inner(*args, **kwargs):
        print('step2')
        if cls not in __instance:
            print('step3')
            obj = cls(*args, **kwargs)
            __instance[cls] = obj
        return __instance[cls]

    return inner()


# @singleton
# class Person:
#     pass


class SingletonMeta(type):  # 继承type类
    def __call__(cls, *args, **kwargs):
        if hasattr(cls, '__instance'):  # 注意，检查的不是实例属性，而是类属性
            return getattr(cls, '__instance')

        # obj = cls(*args, **kwargs)  # 报错了。RecursionError: maximum recursion depth exceeded
        obj = super().__call__(*args, **kwargs)
        setattr(cls, '__instance', obj)

        return obj


class Person(metaclass=SingletonMeta):  # 不用装饰器的方式了，该用metaclass的方式
    pass


if __name__ == '__main__':
    p1 = Person()
    p2 = Person()
    print(p1 is p2)
