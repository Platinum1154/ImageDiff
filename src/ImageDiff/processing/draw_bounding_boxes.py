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
    response_a = requests.get(image_a_url)
    response_b = requests.get(image_b_url)

    # 将下载的内容转换为numpy数组
    image_array_a = np.asarray(bytearray(response_a.content), dtype=np.uint8)
    image_array_b = np.asarray(bytearray(response_b.content), dtype=np.uint8)

    # 解码成OpenCV图像格式
    image_a = cv2.imdecode(image_array_a, cv2.IMREAD_COLOR)
    image_b = cv2.imdecode(image_array_b, cv2.IMREAD_COLOR)


    for idx, diff in enumerate(iterable=boxes.get("diffs", [])):
        x, y, w, h = diff["box"]
        confidence = diff.get("conf", 0)

        # 左上角和右下角坐标
        pt1 = (x, y)
        pt2 = (x + w, y + h)

        # image_a
        cv2.rectangle(image_a, pt1, pt2, (0,255,0), 2)

        # 显示文字
        label = f"diff {idx+1}: {confidence:.2f}"
        text_pos = (x, y - 10 if y - 10 > 10 else y + 20)

        cv2.putText(
            image_a,
            label,
            text_pos,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,255,0),
            1,
            cv2.LINE_AA
        )
    cv2.imshow("Image A with Bounding Boxes", image_a)
    cv2.imshow("Image B with Bounding Boxes", image_b)
    cv2.waitKey(0)

    return image_a