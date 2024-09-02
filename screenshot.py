import cv2
import pytesseract

# 配置Tesseract OCR的路径
#pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# 读取图片
img = cv2.imread('login.png')

if img is None:
    print("Error: Image not found or unable to read the image.")
else:
    # 将图片转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 对灰度图像进行二值化处理
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # 使用Tesseract OCR进行文字检测
    text = pytesseract.image_to_string(thresh, lang="chi_sim")
    print(text)
    # 获取字符位置信息
    boxes = pytesseract.image_to_boxes(thresh)
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(img, (int(b[1]), img.shape[0] - int(b[2])), (int(b[3]), img.shape[0] - int(b[4])), (0, 255, 0), 2)

    # 或者使用 image_to_data 方法来获取详细的边界框信息
    data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
    n_boxes = len(data['text'])
    for i in range(n_boxes):
        if int(data['conf'][i]) > 60:
            (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示结果图片
    cv2.imshow('Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
