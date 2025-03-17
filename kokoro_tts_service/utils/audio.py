from typing import Optional
import soundfile as sf
import io
import numpy as np

class AudioProcessor:
    @staticmethod
    def save_audio(audio_data: np.ndarray, sample_rate: int = 24000) -> io.BytesIO:
        """将音频数据保存为字节流"""
        audio_bytes = io.BytesIO()
        sf.write(audio_bytes, audio_data, sample_rate, format='WAV')
        audio_bytes.seek(0)
        return audio_bytes

    @staticmethod
    def save_to_file(audio_data: np.ndarray, file_path: str, sample_rate: int = 24000) -> None:
        """将音频数据保存到文件"""
        sf.write(file_path, audio_data, sample_rate)