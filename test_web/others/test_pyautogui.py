# import os
#
# import pyautogui
# import time
#
# # 提示用户放置鼠标  # 延迟一段时间，以便你有时间切换到目标窗口
# print("请在5秒内将鼠标放置在桌面上...")
# time.sleep(5)
#
# # 获取当前鼠标位置
# current_x, current_y = pyautogui.position()
# print(current_x, current_y)
#
#
# # 获取屏幕的尺寸
# screen_width, screen_height = pyautogui.size()
#
# # # 设置要点击的位置坐标
# # click_x = screen_width // 2  # 屏幕水平中心位置
# # click_y = screen_height // 2  # 屏幕垂直中心位置
#
# # click_x = 1076
# # click_y = 644
#
# # tmp = [(i + 1, j + 1) for i in range(1076, 1100) for j in range(643, 700)]
#
# # 循环点击多次
# for i in range(10):
#     # pyautogui.click(click_x, click_y)
#     pyautogui.click(current_x, current_y)
#
#     # pyautogui.click(item)
#     # time.sleep(0.001)  # 等待一秒钟
#
# # 点击完成后，程序退出
import ctypes
import random

import pyautogui
import time

# # 提示用户放置鼠标  # 延迟一段时间，以便你有时间切换到目标窗口
# print("请在5秒内将鼠标放置在你想点击的位置.")
# time.sleep(5)

# # 弹窗提示用户放置鼠标
# MessageBox = ctypes.windll.user32.MessageBoxW
# MessageBox(None, "请在5秒内将鼠标放置在你想点击的位置.", "提示", 0x40 | 0x1)  # 弹窗类型为信息提示框
time.sleep(5)


# 获取当前鼠标位置
current_x, current_y = pyautogui.position()
print(current_x, current_y)

# 获取屏幕的尺寸
screen_width, screen_height = pyautogui.size()

# 循环点击多次
for i in range(100):
# while True:
    a = random.random()*5
    b = random.random()*6
    pyautogui.click(current_x + a, current_y + b)


