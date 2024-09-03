from time import sleep
import pygetwindow as gw
import pyautogui
import tkinter
from pyautogui import ImageNotFoundException


def openHWCloud():
    #云桌面

    window = gw.getWindowsWithTitle('华为云客户端 - YINSHENG1')[0]
    if window:
        window.activate()
    else:
        print('云桌面没打开')
        return -1
    sleep(1)

    try:
        #点击debug启动
        location=pyautogui.locateOnScreen(image='debug.png')
    except ImageNotFoundException:
        try:
            # 点击eclipse
            location = pyautogui.locateOnScreen(image='eclipse.png', confidence=0.8)
            # 输出坐标
            print(location)
            # 利用center()函数获取目标图像在系统中的中心坐标位置
            x, y = pyautogui.center(location)
            pyautogui.click(x=x, y=y, clicks=1, button='left')
            sleep(1)
        except ImageNotFoundException:
            print("eclipse没启动")
            return -1
    # 点击debug启动
    location2 = pyautogui.locateOnScreen(image='debug.png')
    #输出坐标
    print(location2)
    #利用center()函数获取目标图像在系统中的中心坐标位置
    x,y=pyautogui.center(location2)
    pyautogui.click(x=x+10,y=y,clicks=1,button='left')
    print('debug启动')
    #等newapp启动
    sleep(8)
    isLoginin = -1
    # 循环10次
    for i in range(10):
        try:
            # 使用locateOnScreen函数查找图像
            result = pyautogui.locateOnScreen('login.png')

            # 判断是否找到匹配的图像
            if result:
                print(f"在第{i + 1}次循环中找到匹配的图像，位置为：{result}")
                isLoginin = 0
                break
        except ImageNotFoundException:
            # 等待一段时间再进行下一次循环
            sleep(1)
            print(f"在第{i + 1}次循环中未找到匹配的图像")

    if isLoginin != 0:
        print('newapp未在18秒内启动成功')
        return -1

    pyautogui.press('shift')
    pyautogui.typewrite('devuser')
    sleep(0.1)
    pyautogui.press('tab')
    sleep(0.1)
    pyautogui.typewrite('Newapp@45026')
    sleep(0.1)
    pyautogui.press('enter')

    #进入lgate
    sleep(7)
    try:
        location=pyautogui.locateOnScreen(image='lgate.png', confidence=0.7)
    except ImageNotFoundException:
        print('未找到lgate图标')
    else:
        #利用center()函数获取目标图像在系统中的中心坐标位置
        x,y=pyautogui.center(location)
        #参数x,y代表坐标位置，clicks代表点击次数,button可以设置为左键或者右键
        pyautogui.doubleClick(x=x,y=y)

    #关闭多余的view
    sleep(6)
    try:
        location=pyautogui.locateOnScreen(image='close.png', confidence=0.7)
    except ImageNotFoundException:
        print('未找到close图标')
    else:
        #输出坐标
        #利用center()函数获取目标图像在系统中的中心坐标位置
        x,y=pyautogui.center(location)
        pyautogui.click(x=x,y=y,clicks=1,button='left')

    #输入航班参数
    pyautogui.typewrite('CA1437')
    sleep(0.1)
    pyautogui.press('tab')
    sleep(0.1)
    pyautogui.typewrite('20240806')
    pyautogui.press('enter')
    sleep(1.5)
    pyautogui.press('enter')
    sleep(1.5)
    pyautogui.press('enter')
    sleep(1.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.press('enter')

if __name__ == "__main__":
    openHWCloud()