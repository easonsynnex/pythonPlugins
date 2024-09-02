import pyautogui
from PIL import Image
import pytesseract

# 打开图像
#image = cv2.imread('login.png')

# 去除噪声
#denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
#cv2.putText(denoised_image, 'Hello, OpenCV!', (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#content = pytesseract.image_to_string(image, lang="chi_sim")   # 识别图片
#print('识别内容' + content)
# 显示去除噪声后的图像
#cv2.imshow('Denoised Image', denoised_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

screenshot = pyautogui.screenshot()

# 保存截图（可选）
screenshot.save("screenshot.png")

# 打开截图进行OCR处理
image = Image.open("screenshot.png")
content = pytesseract.image_to_string(image, lang="chi_sim+eng")   # 识别图片
print(content)
#cv2.imshow('Denoised Image', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()