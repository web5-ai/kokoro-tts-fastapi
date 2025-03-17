import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional
from kokoro import KPipeline
import soundfile as sf
import io
from .config.settings import API_HOST, API_PORT, DEBUG, OUTPUT_DIR

app = FastAPI(
    title="Kokoro TTS API",
    description="中文语音合成服务 API",
    version="1.0.0"
)

# 初始化 TTS 管道
pipeline = KPipeline(lang_code='z', repo_id='hexgrad/Kokoro-82M-v1.1-zh')

class TTSRequest(BaseModel):
    text: str
    voice: Optional[str] = "zf_001"
    speed: Optional[float] = 1.0
    save_file: Optional[bool] = False

@app.get("/")
async def root():
    return {"message": "欢迎使用 Kokoro TTS API"}

@app.post("/tts")
async def text_to_speech(request: TTSRequest):
    try:
        # 生成音频
        generator = pipeline(
            text=request.text,
            voice=request.voice,
            speed=request.speed
        )
        
        # 获取音频数据
        for _, (_, _, audio) in enumerate(generator):
            # 保存音频
            audio_bytes = io.BytesIO()
            sf.write(audio_bytes, audio, 24000, format='WAV')
            audio_bytes.seek(0)
            
            return StreamingResponse(
                audio_bytes,
                media_type="audio/wav"
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def run():
    import uvicorn
    uvicorn.run(
        "kokoro_tts_service.main:app",
        host=API_HOST,
        port=API_PORT,
        reload=DEBUG
    )

if __name__ == "__main__":
    run()