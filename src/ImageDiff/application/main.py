import ImageDiff.interface.GPT.ali as ali_gpt

def main() -> None:
    print("Hello from imagediff!")
    img1 = "https://pic1.imgdb.cn/item/6940bd5f4a4e4213d00b3d6a.png"
    img2 = "https://pic1.imgdb.cn/item/6940bd5e4a4e4213d00b3d68.png"

    result = ali_gpt.ask_vl_model(
        image_a_url=img1,
        image_b_url=img2,
        question="这两张图片有什么区别？"
    )
    print("\n\n思考过程：")
    print(result["reasoning"])
    print("\n\n回答：")
    print(result["answer"])



    
if __name__ == "__main__":
    main()