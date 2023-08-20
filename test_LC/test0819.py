# import heapq
#
# # Create a list
# arr = [5, 3, 7, 2]
#
# # Convert the list into a min heap using heapq.heapify()
# heapq.heapify(arr)
# # Now, arr will be a min heap
# print((arr))  # [2, 3, 7, 5]
# print((heapq))  # <module 'heapq' from '/Users/pc/miniconda3/envs/py39/lib/python3.7/heapq.py'>
#

# import heapq
# # Create a list
# arr = [5, 3, 7, 2]
# print((arr))  # [5, 3, 7, 2]
# # Convert the list into a min heap using heapq.heapify()
# heapq.heapify(arr)
# print((arr))  # [2, 3, 7, 5]
# print((heapq))  # <module 'heapq' from '/Users/pc/miniconda3/envs/py39/lib/python3.7/heapq.py'>
# node = heapq.heappop(arr)
# print('node: ', node)
# node = heapq.heappop(arr)
# print('node: ', node)
# node = heapq.heappop(arr)
# print('node: ', node)
# node = heapq.heappop(arr)
# print('node: ', node)
# print(arr)

# 加上负号，构造大顶堆
# import heapq
# # Create a list
# arr = [5, 3, 7, 2]
# # Negate all elements in the list
# arr = [-x for x in arr]
# print(arr)
#
# heapq.heapify(arr)
# print(arr)  # [-7, -3, -5, -2]
#
# node = heapq.heappop(arr)
# print('node: ', node)
# node = heapq.heappop(arr)
# print('node: ', node)
# node = heapq.heappop(arr)
# print('node: ', node)
# node = heapq.heappop(arr)
# print('node: ', node)
#
# print(arr)