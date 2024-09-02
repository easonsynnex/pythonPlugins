import numpy
from pyautogui import *
from PIL import Image
import numpy as np


def get_curtime(time_format="%Y-%m-%d %H:%M:%S"):
    curTime = time.localtime()
    curTime = time.strftime(time_format, curTime)
    return curTime


def ocr_get_txt_pos(path="", text=""):
    '''
    获取文字与位置对应map
    :param path:图片路径，图片路径为空则默认获取当前屏幕截图
    :param text: 筛选需要查找的内容，匹配所有位置
    :return:list
    '''

    result, img_path = ocr_img_text(path, saveimg=True)

    print("图片识别结果保存：", img_path)

    poslist = [detection[0][0] for line in result for detection in line]
    txtlist = [detection[1][0] for line in result for detection in line]

    # 用list存文字与位置信息
    find_txt_pos = []

    items = 0

    if text == "":
        find_txt_pos = result
    else:
        for i in range(len(poslist)):
            if txtlist[i] == text:
                find_txt_pos.append(poslist[i])
                items += 1

    print(find_txt_pos)
    return find_txt_pos


def ocr_img_text(path="", saveimg=False, printResult=False):
    '''
    图像文字识别
    :param path:图片路径
    :param saveimg:是否把结果保存成图片
    :param printResult:是否打印出识别结果
    :return:result,img_name
    '''
    image = path

    # 图片路径为空就默认获取屏幕截图
    if image == "":
        image = screenshot()
        image = np.array(image)
    else:
        # 不为空就打开
        image = Image.open(image).convert('RGB')

    ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory

    result = ocr.ocr(image, cls=True)
    if printResult is True:
        for line in result:
            for word in line:
                print(word)

    # 识别出来的文字保存为图片
    img_name = "ImgTextOCR-img-" + get_curtime("%Y%m%d%H%M%S") + ".jpg"
    if saveimg is True:
        boxes = [detection[0] for line in result for detection in line]  # Nested loop added
        txts = [detection[1][0] for line in result for detection in line]  # Nested loop added
        scores = [detection[1][1] for line in result for detection in line]  # Nested loop added
        im_show = draw_ocr(image, boxes, txts, scores)
        im_show = Image.fromarray(im_show)
        im_show.save(img_name)

    return result, img_name


if __name__ == '__main__':
    # test-1
    ocr_img_text(saveimg=True, printResult=True)

    # test-2
    pos_list = ocr_get_txt_pos(text="二、使用步骤")

    # test-3
    pos_list = ocr_get_txt_pos(text="总结")

    # 取一个点进行点击操作
    pos_x, pos_y = pos_list[0]
    moveTo(pos_x + 5, pos_y + 5)
    click()