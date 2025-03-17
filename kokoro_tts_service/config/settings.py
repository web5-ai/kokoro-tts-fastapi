import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# API 设置
API_HOST = os.getenv('API_HOST', '0.0.0.0')
API_PORT = int(os.getenv('API_PORT', 8000))
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# 输出目录设置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# TTS 设置
DEFAULT_LANG_CODE = 'a'  # 美式英语
DEFAULT_VOICE = 'af_heart'
DEFAULT_SPEED = 1.0