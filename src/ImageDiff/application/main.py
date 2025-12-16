import ImageDiff.interface.GPT.ali as ali_gpt
from ImageDiff.processing.draw_bounding_boxes import draw_bounding_boxes
import ImageDiff.processing.get_image_data as get_image_data
import json
def main() -> None:
    print("Hello from imagediff!")
    img1 = "https://pic1.imgdb.cn/item/6940bd5f4a4e4213d00b3d6a.png"
    img2 = "https://pic1.imgdb.cn/item/6940bd5e4a4e4213d00b3d68.png"
    # img1 ="https://pic1.imgdb.cn/item/6940f0f80dd29e7e2241c9d2.png"
    # img2 ="https://pic1.imgdb.cn/item/6940f0f80dd29e7e2241c9d1.png"
    pixel = get_image_data.get_image_pixel(img1)
    result = ali_gpt.ask_vl_model(
        image_a_url=img1,
        image_b_url=img2,
        question='''你是一个图像差异检测系统。
            现在我会给你两张图片：
            - 第一张是 image_a
            - 第二张是 image_b

            你的任务是：
            1. 对比 image_a 和 image_b
            2. 找出 image_b 相对于 image_a 的所有可见差异区域
            3. 对每一个差异区域，给出在 image_a 坐标系下的矩形框

            【重要约束】
            - 只输出 JSON，不要任何解释性文字
            - 不要使用 Markdown
            - 不要输出多余字段
            - 坐标必须使用 OpenCV 格式：(x, y, w, h)
            - x, y 为左上角像素坐标
            - w, h 为矩形宽高（像素）
            - 坐标必须是整数
            - confidence 为 0~1 的浮点数，表示你对该差异判断的可信度

            【返回格式示例】
            {
            "diffs": [
                {
                "box": [x, y, w, h],
                "conf": 0.95
                }
            ]
            }

            如果没有检测到明显差异，请返回：
            {
            "diffs": []
            }'''
            ,
        enable_thinking=True
    )
    print("\n\n思考过程：")
    print(result["reasoning"])
    print("\n\n回答：")
    print(result["answer"])


    boxes = json.loads(result["answer"])

    draw_bounding_boxes(
        image_a_url=img1,
        image_b_url=img2,
        boxes=boxes
        
    )



    
if __name__ == "__main__":
    main()