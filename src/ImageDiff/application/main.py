import ImageDiff.interface.GPT.ali as ali_gpt
from ImageDiff.processing.draw_bounding_boxes import draw_bounding_boxes
def main() -> None:
    print("Hello from imagediff!")
    img1 = "https://pic1.imgdb.cn/item/6940bd5f4a4e4213d00b3d6a.png"
    img2 = "https://pic1.imgdb.cn/item/6940bd5e4a4e4213d00b3d68.png"

    result = ali_gpt.ask_vl_model(
        image_a_url=img1,
        image_b_url=img2,
        question='''任务描述
            目标：比较两张图片，找出不同之处，并以字典的形式返回：
            坐标：每个不同区域的坐标，以 OpenCV 格式表示。一般来说，OpenCV 使用 (x, y, w, h) 格式，其中 (x, y) 是矩形的左上角坐标，w 和 h 是矩形的宽度和高度。
            可信度：为每个不同区域返回一个可信度评分。可信度可以基于图像差异的计算，比如通过模板匹配、图像减法或图像差异度量来得出。
            输出字典格式示例
            {
                "differences": [
                    {
                        "coordinates": (50, 100, 80, 60),  # 该区域的坐标，(x, y, width, height)
                        "confidence": 0.95  # 可信度评分，0到1之间
                    },
                    {
                        "coordinates": (200, 150, 100, 70),
                        "confidence": 0.89
                    }
                ]
            }",
    ''')
    print("\n\n思考过程：")
    print(result["reasoning"])
    print("\n\n回答：")
    print(result["answer"])

    draw_bounding_boxes(
        image_a_url=img1,
        image_b_url=img2,
        boxes={
            "image_a": [[50, 50, 200, 200]],
            "image_b": [[60, 60, 210, 210]]
        }
    )



    
if __name__ == "__main__":
    main()