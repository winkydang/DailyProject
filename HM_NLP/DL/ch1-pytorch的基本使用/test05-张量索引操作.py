import torch

data = torch.randint(0, 10, [4, 5])
print(data)
print('-' * 50)

# 2. 列表索引
def test02():

    # 返回 (0, 1)、(1, 2) 两个位置的元素
    print(data[[0, 1], [1, 2]])
    print('-' * 50)

    # 返回 0、1 行的 1、2 列共4个元素
    print(data[[[0], [1]], [1, 2]])  # The first set [[[0], [1]]] is indexing the rows, and the second set [1, 2] is indexing the columns.
    # [[[0], [1]]], is indexing the rows. This is a nested list of indices: [[0]] selects the first row, and [[1]] selects the second row.
    # The second part, [1, 2], is indexing the columns. This means you're trying to select elements from the columns with indices 1 and 2.

if __name__ == '__main__':
    test02()
