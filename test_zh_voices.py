from kokoro import KPipeline
import os

def test_chinese_voices():
    # 测试文本
    texts = [
        "这是一个中文语音合成测试。",
        "春眠不觉晓，处处闻啼鸟。",
        "科技改变生活，创新驱动发展。"
    ]
    
    # 所有可能的中文音色
    voices = [f"zf_{str(i).zfill(3)}" for i in range(1, 21)]  # 女声 1-20
    voices.extend([f"zm_{str(i).zfill(3)}" for i in range(1, 6)])  # 男声 1-5
    
    # 创建输出目录
    os.makedirs("zh_voice_samples", exist_ok=True)
    
    # 初始化管道
    pipeline = KPipeline(lang_code='z', repo_id='hexgrad/Kokoro-82M-v1.1-zh')
    
    # 测试每个音色
    for voice in voices:
        try:
            print(f"\n测试音色: {voice}")
            
            # 生成音频
            generator = pipeline(
                text=texts[0],
                voice=voice,
                speed=1.0
            )
            
            # 保存音频
            for _, (gs, ps, audio) in enumerate(generator):
                output_file = f"zh_voice_samples/{voice}.wav"
                import soundfile as sf
                sf.write(output_file, audio, 24000)
                print(f"✓ 成功生成: {output_file}")
                print(f"音素: {ps}")
                break
                
        except Exception as e:
            print(f"✗ 音色 {voice} 不可用: {str(e)}")

if __name__ == "__main__":
    test_chinese_voices()