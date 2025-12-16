import cv2
import numpy as np
import requests


def get_image_pixel(img_url : str) -> dict:

    # 使用requests库下载图片
    response = requests.get(img_url)

    # 将下载的内容转换为numpy数组
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)

    # 解码成OpenCV图像格式
    img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    h, w = img.shape[:2]
    print("宽度:", w)
    print("高度:", h)
    print("分辨率:", f"{w} x {h}")
    return {"width": w, "height": h}
