import pyautogui
from PIL import Image
import pytesseract

# 截取屏幕
screenshot = pyautogui.screenshot()

# 保存截图（可选）
#screenshot.save("screenshot.png")

# 打开截图进行OCR处理
image = Image.open("login.png")

# 设置pytesseract的psm模式为6，以识别整个单词或句子
custom_oem_psm_config = r'--oem 3 --psm 6'

# 进行OCR识别，获取多个字符的识别结果
text_boxes = pytesseract.image_to_data(image, lang="chi_sim+eng", config=custom_oem_psm_config,
                                       output_type=pytesseract.Output.DICT)

# 遍历识别的文字区域，查找“确定”
n_boxes = len(text_boxes['level'])
for i in range(n_boxes):
    text = text_boxes['text'][i].strip()
    if text == "MarsGode":
        # 获取“确定”文字区域的中心位置
        x, y, w, h = (text_boxes['left'][i], text_boxes['top'][i], text_boxes['width'][i], text_boxes['height'][i])
        center_x, center_y = x + w / 2, y + h / 2

        # 移动鼠标到“确定”文字的中心位置
        pyautogui.moveTo(center_x, center_y)
        print(f"鼠标移动到 '确定' 位置: ({center_x}, {center_y})")
        break  # 找到第一个“确定”后停止

# 如果没有找到“确定”，则打印信息
else:
    print("未找到 '确定' 文字")