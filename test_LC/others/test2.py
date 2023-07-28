# class Context(object):
#     def __enter__(self):
#         print("进入上下文")
#         return "hello world"
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("关闭上下文")
#
#
# with Context() as context:
#     print("执行")

# 2nd
class Context(object):
    def __enter__(self):
        print("进入上下文")
        return "hello world"
        # pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭上下文")

with Context() as context:
    print("执行")
    # print(Context().__enter__())

