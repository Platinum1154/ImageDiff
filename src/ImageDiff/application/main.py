import ImageDiff.interface.GPT.ali as ali_gpt
from ImageDiff.processing.draw_bounding_boxes import draw_bounding_boxes
import ImageDiff.processing.get_image_data as get_image_data
import json
def main() -> None:
    print("Hello from imagediff!")
    # img1 = "https://pic1.imgdb.cn/item/6940bd5f4a4e4213d00b3d6a.png"
    # img2 = "https://pic1.imgdb.cn/item/6940bd5e4a4e4213d00b3d68.png"
    img1 ="https://pic1.imgdb.cn/item/6940f0f80dd29e7e2241c9d2.png"
    img2 ="https://pic1.imgdb.cn/item/6940f0f80dd29e7e2241c9d1.png"
    pixel = get_image_data.get_image_pixel(img1)
    result = ali_gpt.ask_vl_model(
        image_a_url=img1,
        image_b_url=img2,
        question='''任务描述
            目标：比较两张图片，找出不同之处，并以字典的形式返回：
            坐标：每个不同区域的坐标，以 OpenCV 格式表示。一般来说，OpenCV 使用 (x, y, w, h) 格式，其中 (x, y) 是矩形的左上角坐标，w 和 h 是矩形的宽度和高度。
            可信度：为每个不同区域返回一个可信度评分。可信度可以基于图像差异的计算，比如通过模板匹配、图像减法或图像差异度量来得出。
            输出字典格式示例：
            {
            "diffs": [
                {
                "box": [50, 100, 80, 60],
                "conf": 0.95
                },
                {
                "box": [200, 150, 100, 70],
                "conf": 0.89
                }
            ]
            }
            ",这个图片的分辨率是：
    ''' + str(pixel)
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