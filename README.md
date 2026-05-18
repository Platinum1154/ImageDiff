# ImageDiff

ImageDiff 是一个基于 Python 的智能图像差异检测工具。项目结合视觉语言模型与 OpenCV，能够对比两张图片，自动识别第二张图片相对于第一张图片的可见差异，并以边界框的形式进行可视化展示。

该项目适用于 UI 设计稿对比、图片版本检查、视觉 QA、图像内容变更检测等场景。

## 功能特性

- 支持输入两张远程图片 URL 进行对比
- 使用视觉语言模型识别图片中的语义差异
- 输出结构化 JSON 差异结果
- 支持差异区域的 bounding box 标注
- 使用 OpenCV 在图片上绘制检测框
- 支持置信度 `confidence` 输出
- 使用 `.env` 管理 API Key
- 使用 `uv` 进行依赖管理和运行

## 技术栈

- Python 3.10+
- uv
- OpenAI SDK
- DashScope / Qwen3-VL
- OpenCV
- NumPy
- requests
- python-dotenv

## 项目结构

```text
ImageDiff/
├── src/
│   └── ImageDiff/
│       ├── application/
│       │   └── main.py
│       ├── interface/
│       │   └── GPT/
│       │       └── ali.py
│       └── processing/
│           ├── draw_bounding_boxes.py
│           └── get_image_data.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

### 目录说明

| 路径 | 说明 |
| --- | --- |
| `application/main.py` | 项目主入口，负责组织图片输入、模型调用和结果绘制流程 |
| `interface/GPT/ali.py` | 视觉模型接口层，负责调用 DashScope 兼容 OpenAI API |
| `processing/get_image_data.py` | 图片数据处理模块，用于读取图片尺寸等基础信息 |
| `processing/draw_bounding_boxes.py` | 结果可视化模块，用于绘制差异检测框 |
| `pyproject.toml` | 项目配置与依赖声明 |
| `uv.lock` | uv 生成的依赖锁定文件 |

## 环境要求

请确保本地环境已安装：

- Python >= 3.10
- uv
- 可用的 DashScope API Key

## 安装方式

克隆项目：

```bash
git clone https://github.com/Platinum1154/ImageDiff.git
cd ImageDiff
```

安装依赖：

```bash
uv sync
```

## 配置环境变量

在项目根目录下新建 `.env` 文件：

```env
DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

其中 `DASHSCOPE_API_KEY` 为你的 DashScope API Key。

## 快速开始

运行主程序：

```bash
uv run .\src\ImageDiff\application\main.py
```

Linux / macOS 环境下可使用：

```bash
uv run ./src/ImageDiff/application/main.py
```

程序会执行以下流程：

1. 读取两张图片 URL
2. 获取图片尺寸信息
3. 调用视觉语言模型进行图像差异分析
4. 解析模型返回的 JSON 结果
5. 使用 OpenCV 绘制差异检测框
6. 弹出窗口展示标注结果

## 输出格式

模型输出为 JSON 格式，结构如下：

```json
{
  "diffs": [
    {
      "box": [x, y, w, h],
      "conf": 0.95
    }
  ]
}
```

字段说明：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `diffs` | array | 检测到的差异列表 |
| `box` | array | 差异区域边界框 |
| `conf` | float | 模型对该差异判断的置信度，范围为 0~1 |

当前绘制模块会将 `box` 视为 `0~1000` 范围内的归一化坐标，并根据图片实际宽高映射为像素坐标。

例如：

```json
{
  "diffs": [
    {
      "box": [120, 230, 180, 90],
      "conf": 0.92
    }
  ]
}
```

表示检测到一个差异区域：

- 左上角 x 坐标：`120`
- 左上角 y 坐标：`230`
- 宽度：`180`
- 高度：`90`
- 置信度：`0.92`

## 核心流程

ImageDiff 的主要工作流程如下：

```text
图片 A URL + 图片 B URL
        ↓
下载并读取图片尺寸
        ↓
调用 Qwen3-VL 视觉模型
        ↓
输出差异区域 JSON
        ↓
解析 bounding boxes
        ↓
OpenCV 绘制检测框
        ↓
展示可视化结果
```

## 使用场景

### UI / UX 设计对比

对比两版 UI 截图，快速发现按钮、文字、布局、图标等变化。

### 软件测试与视觉回归

在前端页面、客户端界面或图像输出场景中，辅助检测版本更新后的视觉变化。

### 图片内容审核

检测图片是否出现局部修改、遮挡、替换或新增内容。

### 图像版本管理

对多版本图片进行差异定位，辅助人工审核和归档。

## 常见问题

### 1. API Key 没有生效

请检查根目录是否存在 `.env` 文件，并确认内容格式如下：

```env
DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

同时确认程序是在项目根目录下运行的。

### 2. 图片加载失败

如果出现图片加载失败，请检查：

- 图片 URL 是否可以直接访问
- 网络连接是否正常
- 图片格式是否能被 OpenCV 解码
- 远程图片服务是否限制了访问

### 3. OpenCV 窗口没有显示

请确认当前运行环境支持 GUI 窗口显示。  
如果在服务器、WSL 或无桌面环境中运行，`cv2.imshow()` 可能无法正常工作。

### 4. 坐标绘制位置不准确

当前绘制逻辑会将模型输出的坐标按 `0~1000` 归一化坐标处理。  
如果模型直接输出像素坐标，需要同步修改 `draw_bounding_boxes.py` 中的坐标映射逻辑。

## 后续可优化方向

- 支持本地图片路径输入
- 支持命令行参数传入图片路径或 URL
- 支持保存标注后的结果图片
- 支持批量图片对比
- 支持输出差异检测报告
- 支持选择不同视觉模型
- 支持 Web 可视化界面
- 增加异常处理和日志输出
- 增加单元测试与示例数据

## License

This project is licensed under the MIT License.
Copyright (c) 2026 Platinum1154
See the [LICENSE](LICENSE) file for details.

## Author

Platinum1154