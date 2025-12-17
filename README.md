# 概述
ImageDiff 是一个基于 Python 的图像对比系统，利用 AI 视觉模型自动检测并可视化图像之间的差异。该项目结合了计算机视觉处理与 AI 分析，为图像变化提供精确的边界框检测。

# 项目简介

ImageDiff 是一个结合 AI 视觉模型和 OpenCV 的图像差异检测工具：
使用 AI 视觉模型 自动识别图像内容差异
输出结构化差异坐标（bounding boxes + confidence）
使用 OpenCV 绘制框并展示对比结果
支持通过 HTTP 图像 URL 输入

# 快速开始
在根目录配置.env文件，在内部存入DASHSCOPE_API_KEY="sk-xxxxxx"
```bash
uv run .\src\ImageDiff\application\main.py
```


# 如果出现错误
```bash
uv run .\src\ImageDiff\application\main.py
      Built imagediff @ file:///C:/wo
Uninstalled 1 package in 12ms        
Installed 1 package in 61ms
Hello from imagediff!
Traceback (most recent call last):
  File "C:\work\ImageDiff\src\ImageDiff\application\main.py", line 71, in <module>
    main()
  File "C:\work\ImageDiff\src\ImageDiff\application\main.py", line 11, in main
    pixel = get_image_data.get_image_pixel(img1)
  File "C:\work\ImageDiff\src\ImageDiff\processing\get_image_data.py", line 9, in get_image_pixel
    response = requests.get(img_url)
  File "C:\work\ImageDiff\.venv\lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "C:\work\ImageDiff\.venv\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\work\ImageDiff\.venv\lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "C:\work\ImageDiff\.venv\lib\site-packages\requests\sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "C:\work\ImageDiff\.venv\lib\site-packages\requests\adapters.py", line 644, in send
    resp = conn.urlopen(
  File "C:\work\ImageDiff\.venv\lib\site-packages\urllib3\connectionpool.py", line 787, in urlopen
    response = self._make_request(
  File "C:\work\ImageDiff\.venv\lib\site-packages\urllib3\connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "C:\work\ImageDiff\.venv\lib\site-packages\urllib3\connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "C:\work\ImageDiff\.venv\lib\site-packages\urllib3\connection.py", line 759, in connect
    self.sock = sock = self._new_conn()
  File "C:\work\ImageDiff\.venv\lib\site-packages\urllib3\connection.py", line 204, in _new_conn
    sock = connection.create_connection(
  File "C:\work\ImageDiff\.venv\lib\site-packages\urllib3\util\connection.py", line 73, in create_connection   
    sock.connect(sa)
```
则重新运行即可