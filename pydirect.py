import pydirectinput

pydirectinput.moveTo(100, 150)
pydirectinput.click()

pydirectinput.click(200, 220)  # 移动鼠标至坐标200，220，并点击左键

pydirectinput.move(None, 10)  # 鼠标移动相对y位置

pydirectinput.doubleClick()  # 双击鼠标左键

pydirectinput.press('esc')  # 按一下esc

pydirectinput.keyDown('shift')  # 按下shift

pydirectinput.keyUp('shift')  # 弹起shift
