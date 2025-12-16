import cv2
import numpy as np
import requests


def draw_bounding_boxes(
        image_a_url : str, 
        image_b_url : str, 
        boxes : dict, 
):
    """
    在两张图片上绘制边界框。

    参数:
    - image_a: 图片A的文件链接。
    - image_b: 图片B的文件链接。
    - boxes: 包含边界框信息的字典，格式如下：
        {
            "image_a": [ [x1, y1, x2, y2], ... ],
            "image_b": [ [x1, y1, x2, y2], ... ]
        }

    返回:
    - image_a_with_boxes: 绘制边界框后的图片A。
    - image_b_with_boxes: 绘制边界框后的图片B。
    """


    # 使用requests库下载图片
    response = requests.get(image_a_url)

    # 将下载的内容转换为numpy数组
    image_array = np.asarray(bytearray(response.content), dtype=np.uint8)

    # 解码成OpenCV图像格式
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # 检查图像是否成功读取
    if image is not None:
        # 显示图片
        cv2.imshow("Downloaded Image", image)

        # 等待按键，退出显示窗口
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Failed to load image.")



