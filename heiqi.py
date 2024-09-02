import sys
from email.policy import default
from time import sleep
import pygetwindow as gw
import pyautogui
import threading
from pyautogui import ImageNotFoundException
from pynput import keyboard
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
# 指定屏幕上的坐标
x, y = 2359, 19  # 请根据实际情况指定坐标

# 标记是否应该退出循环
should_exit = False
# 标记怪是否出来
monster_appear = False
# 指定颜色
target_color = (132, 134, 139)  # 假设目标颜色为白色 (R, G, B)
#记录count
count = 0
#记录上次刷怪的时间
last_appear_time = datetime.now()


#判断指定坐标颜色
def get_pixel_color(x, y):
    """
    获取屏幕指定坐标的像素颜色。

    :param x: 屏幕上的横坐标
    :param y: 屏幕上的纵坐标
    :return: 返回颜色的 RGB 元组 (R, G, B)
    """
    color = pyautogui.pixel(x, y)
    return color


def compare_colors(screen_color, target_color):
    """
    比较屏幕上的颜色与指定颜色是否一致。

    :param screen_color: 屏幕上的颜色 (R, G, B) 元组
    :param target_color: 目标颜色 (R, G, B) 元组
    :return: 如果颜色一致返回 True，否则返回 False
    """
    return screen_color == target_color


def compare_colors_in_while_true():
    while not should_exit:
        # 获取屏幕上的颜色
        screen_color = get_pixel_color(x, y)
        # 比较颜色
        is_same_color = compare_colors(screen_color, target_color)

        #print(f"屏幕上的颜色: {screen_color}")
        #print(f"目标颜色: {target_color}")
        #print(f"颜色是否一致: {is_same_color}")
        # 判断怪是否出来
        global monster_appear, last_appear_time
        if is_same_color:
            if not monster_appear:
                print('怪出现了')
            monster_appear = True
            last_appear_time = datetime.now()
            #TODO 怪出来了
            #TODO 打怪->捡箱子->切线

        else:
            if monster_appear:
                print('怪消失了')
            monster_appear = False
            #TODO 转圈捡箱子？超过2秒没捡到箱子则切线，下次技能先ss 再按1接近boss
            now = datetime.now()
            diff = abs(now - last_appear_time)
            if diff.total_seconds() <= 1:
                print('捡箱子')
                #F捡箱子
                print('FFFFFFFFF捡箱子')
                # pyautogui.keyDown('F')
                # sleep(0.2)
                # pyautogui.keyUp('F')
                # TODO 切线
                print('切线')
            # else:
            #
            #     print(f'超过1秒 {diff} 等待怪出现')

        #print(f'怪是否出现{monster_appear}')
        sleep_interrupted(0.5)

def judge_rtf_switch():
    print('开始打怪')
    while True:
        if monster_appear and not should_exit:
            execute_macro()
            sleep_interrupted(0.2)
        elif should_exit:
            pass
        else:
            print('没怪不打')
            sleep_interrupted(0.5)

def execute_macro():
    global count
    count = count+1
    print(f'rtf {count}')

def sleep_interrupted(sec):
    try:
        sleep(sec)
        return True
    except KeyboardInterrupt:
        global should_exit
        should_exit = False
        print('KeyboardInterrupt')
        sys.exit(0)
    except:
        print('---')
        sys.exit(0)


# 组合键监听器
def on_activate():
    global should_exit
    if should_exit:
        should_exit = False
    else:
        should_exit = True
    convert_to_str = 'exiting' if should_exit else 'starting'
    print(f"Ctrl+O pressed, {convert_to_str} loop...")

# 创建线程
thread = threading.Thread(target=judge_rtf_switch)
thread.start()
# 监听组合键
with keyboard.GlobalHotKeys({'<ctrl>+o': on_activate}) as listener:
    while True:
        print('监听键盘ctro+o按下')
        # 在这里执行你的程序逻辑

        compare_colors_in_while_true()

        #print(should_exit)
        sleep_interrupted(1)  # 假设你的程序逻辑每秒执行一次


