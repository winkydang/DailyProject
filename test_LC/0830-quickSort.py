# def quick_select(arr, k):
#     if k < 1 or k > len(arr):
#         return None
#
#     pivot = arr[-1]
#     left = [x for x in arr if x < pivot]
#     right = [x for x in arr if x > pivot]
#     equal = [x for x in arr if x == pivot]
#
#     if k <= len(right):
#         return quick_select(right, k)
#     elif k <= len(right) + len(equal):
#         return pivot
#     else:
#         return quick_select(left, k - len(right) - len(equal))
#
#
# # 示例用法
# arr = [3, 1, 4, 4, 2, 2, 4, 3, 5]
# k = 3
# result = quick_select(arr, k)
# print(f"The {k}-th largest element is: {result}")


def quickSort(arr, k):
    if k < 1 or k > len(arr):
        return None

    privot = arr[-1]
    left = [x for x in arr if x < privot]
    right = [x for x in arr if x > privot]
    equal = [x for x in arr if x == privot]

    if k < len(right):
        return quickSort(right, k)
    elif k <= len(right) + len(equal):
        return privot
    else:
        return quickSort(left, k-len(right)-len(equal))


arr = [3, 1, 4, 4, 2, 2, 4, 3, 5]
k = 3
result = quickSort(arr, k)
print(f"The {k}-th largest element is: {result}")



