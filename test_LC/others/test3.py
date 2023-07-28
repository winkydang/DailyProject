# class Map(object):
#     def get(self):
#         print('我是get')
#         return "你好"
#
#
# if __name__ == '__main__':
#     map = Map()
#     # map.get()
#     result = getattr(map, "get")()
#     print(result)
#
#     setattr(map, "post", "我是post")
#     print(map.post)

#2nd
class Map(object):
    def get(self):
        print('我是get')
        return "你好"

if __name__ == "__main__":
    map = Map()
    # result = map.get()
    result = getattr(map, "get")  # <bound method Map.get of <__main__.Map object at 0x7f812810f3d0>>
    result1 = getattr(map, "get")()
    print(result1)  # 我是get
    #              # 你好
    setattr(map, "post", "我是post")  # setattr() 为类新增新的方法 或 新的属性
    print(map.post)  # 我是post
    result2 = getattr(map, "post")  # getattr() 获取类的方法的地址 或 属性值
    print(result2)  # 我是post