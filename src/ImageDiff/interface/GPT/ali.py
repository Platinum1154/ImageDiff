from openai import OpenAI
from dotenv import load_dotenv
import os


# 加载环境变量
load_dotenv()  # 自动加载根目录 .env 文件

# 初始化OpenAI客户端
client = OpenAI(
    api_key = os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)



def ask_vl_model(
    image_a_url: str,
    image_b_url: str,
    question: str,
    enable_thinking: bool = False
) -> dict:
    reasoning_content = ""  # 定义完整思考过程
    answer_content = ""     # 定义完整回复
    is_answering = False   # 判断是否结束思考过程并开始回复
    enable_thinking = False
    # 创建聊天完成请求
    completion = client.chat.completions.create(
        model="qwen3-vl-flash",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_a_url
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_b_url
                        },
                    },
                    {"type": "text", "text": question},
                ],
            },
        ],
        stream=True,
        # enable_thinking 参数开启思考过程，thinking_budget 参数设置最大推理过程 Token 数
        extra_body={
            'enable_thinking': True,
            "thinking_budget": 81920},

        # 解除以下注释会在最后一个chunk返回Token使用量
        # stream_options={
        #     "include_usage": True
        # }
    )

    if enable_thinking:
        print("\n" + "=" * 20 + "思考过程" + "=" * 20 + "\n")

    for chunk in completion:
        # 如果chunk.choices为空，则打印usage
        if not chunk.choices:
            print("\nUsage:")
            print(chunk.usage)
        else:
            delta = chunk.choices[0].delta
            reasoning = getattr(delta, "reasoning_content", None)
            if reasoning:
                print(reasoning)

            else:
                # 开始回复
                if delta.content != "" and is_answering is False:
                    print("\n" + "=" * 20 + "完整回复" + "=" * 20 + "\n")
                    is_answering = True
                # 打印回复过程
                print(delta.content, end='', flush=True)
                content = getattr(delta, "content", None)
                if content:
                    answer_content += content
    return {
        "answer": answer_content,
        "reasoning": reasoning_content,
    }

    # print("=" * 20 + "完整思考过程" + "=" * 20 + "\n")
    # print(reasoning_content)
    # print("=" * 20 + "完整回复" + "=" * 20 + "\n")
    # print(answer_content)