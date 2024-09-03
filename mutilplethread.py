import sys
from time import sleep
import pygetwindow as gw
import pyautogui
import threading
from pynput import keyboard
from datetime import datetime

# 转圈标志
should_circle = False
# 捡箱子标志
should_pickup_box = False

#打完怪捡箱子转圈，怪出现也要转圈对准怪
def circle_right():
    print('start circle')
    while True:
        if should_circle:
            print('circling...')
            sleep(0.5)
            #TODO
        #else:

def pick_up_box():
    print('捡箱子')
    while True:
        if should_pickup_box:
            #判断箱子在不在,如果在就停止转圈，且停止捡箱子

            sleep(0.2)

# 组合键监听器
def on_activate():
    global should_circle
    if should_circle:
        should_circle = False
    else:
        should_circle = True
    convert_to_str = 'exiting' if should_circle else 'starting'
    print(f"Ctrl+O pressed, {convert_to_str} loop...")


# 创建转圈线程
thread = threading.Thread(target=circle_right)
thread.start()
# 创建捡箱子线程
thread2 = threading.Thread(target=pick_up_box)
thread2.start()
# 监听组合键
with keyboard.GlobalHotKeys({'<ctrl>+o': on_activate}) as listener:
    while True:
        #print(f'监听键盘Ctrl+o按下 should_circle = {should_circle}')
        sleep(1)


