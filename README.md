
# Kokoro TTS Service

基于 Kokoro-82M-v1.1-zh 模型的中文语音合成服务。

## 项目简介

本项目是一个基于 FastAPI 的 Web 服务，提供高质量的中文语音合成功能。使用了专门针对中文优化的 Kokoro-82M-v1.1-zh 模型，支持多种女声音色，可调节语速等参数。

## 项目背景

随着人工智能技术的发展，语音合成在各个领域的应用越来越广泛。本项目旨在提供一个简单易用的中文语音合成服务，可以快速部署和集成到其他应用中。

## 运行环境要求

- Python >= 3.8
- MacOS/Linux（Windows 未经完整测试）
- 内存 >= 4GB
- 磁盘空间 >= 1GB

## 项目依赖

主要依赖包版本：
- kokoro >= 0.8.2
- misaki[zh] >= 0.8.2
- fastapi >= 0.68.0
- uvicorn >= 0.15.0
- python-dotenv >= 0.19.0
- soundfile

## 快速开始

1. 克隆项目：
```bash
git clone <repository_url>
cd kokoro
```

2. 运行启动脚本：
```bash
chmod +x start.sh
./start.sh
```

3. 测试服务：
```bash
curl -X POST "http://localhost:8000/tts" \
     -H "Content-Type: application/json" \
     -d '{
           "text": "你好，世界！",
           "voice": "zf_001",
           "speed": 1.0
         }' \
     --output test.wav
```

## 开发和调试

1. 安装开发依赖：
```bash
pip install -e .
```

2. 启动开发服务器：
```bash
python -m kokoro_tts_service.main
```

3. API 文档访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 接口

### POST /tts

请求参数：
```json
{
    "text": "要转换的文本",
    "voice": "zf_001",  // 可选，默认 zf_001
    "speed": 1.0,       // 可选，默认 1.0
    "save_file": false  // 可选，是否保存文件
}
```

## 关键技术

- FastAPI：高性能的 Python Web 框架
- Kokoro TTS：基于 StyleTTS 2 的语音合成引擎
- Python 异步编程
- RESTful API 设计

## 使用的模型

模型名称：Kokoro-82M-v1.1-zh
- 架构：StyleTTS 2
- 参数量：82M
- 支持语言：中文、英文
- 训练数据：100+ 位中文发音者

### 可用音色列表

女声音色：
- zf_001 ~ zf_008
- zf_017 ~ zf_019

## 模型特点

1. 针对中文优化
   - 使用专业中文语音数据集训练
   - 支持多种语气和语速调节

2. 轻量级设计
   - 模型大小仅 82M
   - 运行时内存占用小

3. 高质量输出
   - 自然的语音韵律
   - 清晰的发音效果

## 项目结构

```
kokoro/
├── kokoro_tts_service/     # 主要代码目录
│   ├── __init__.py
│   ├── main.py            # 主程序
│   └── config/            # 配置文件
├── tests/                 # 测试目录
├── .env                   # 环境变量
├── setup.py              # 安装配置
├── requirements.txt      # 依赖列表
└── start.sh             # 启动脚本
```

## 常见问题

1. ModuleNotFoundError: No module named 'src'
   - 解决方案：确保使用 `pip install -e .` 安装项目

2. 音色下载失败
   - 解决方案：检查网络连接，确保能访问 huggingface.co

## 参考资料

1. [Kokoro TTS 官方文档](https://github.com/hexgrad/kokoro)
2. [StyleTTS 2 论文](https://arxiv.org/abs/2306.07691)
3. [FastAPI 官方文档](https://fastapi.tiangolo.com/)

## 开源协议

Apache License 2.0

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 致谢

- LongMaoData 提供的中文语音数据集
- StyleTTS 2 的开发团队
- FastAPI 开发团队

## 更新日志

### v0.1.0
- 初始版本发布
- 支持基本的文本转语音功能
- 支持多种中文女声音色
