#!/bin/bash

# 创建虚拟环境（如果不存在）
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "安装依赖..."
pip install -r requirements.txt
pip install "kokoro>=0.8.2" "misaki[zh]>=0.8.2" soundfile

# 启动服务
echo "启动 Kokoro TTS 服务..."
python -m kokoro_tts_service.main