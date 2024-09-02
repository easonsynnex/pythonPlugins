import pyautogui
from PIL import Image, ImageDraw
import pytesseract

# 截取屏幕
screenshot = pyautogui.screenshot()

# 保存截图
#screenshot.save("screenshot.png")

# 打开截图进行处理
image = Image.open("login.png")

# 进行OCR文字识别
text_boxes = pytesseract.image_to_data(image, lang="chi_sim+eng", output_type=pytesseract.Output.DICT)
#print(text_boxes)
# 在图片上绘制红框
draw = ImageDraw.Draw(image)
n_boxes = len(text_boxes['level'])
for i in range(n_boxes):
    (x, y, w, h) = (text_boxes['left'][i], text_boxes['top'][i], text_boxes['width'][i], text_boxes['height'][i])
    text = text_boxes['text'][i].strip()
    print(text)
    # 判断是否是“我”，用绿框，否则用红框
    if "文" in text:
        draw.rectangle([(x-10, y), (x + w-10, y + h)], outline="green", width=2)
    else:
        draw.rectangle([(x-10, y), (x + w, y + h)], outline="red", width=2)

# 保存标记后的图片
image.save("screenshot_with_boxes.png")
image.show()