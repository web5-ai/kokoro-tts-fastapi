from kokoro import KPipeline
import os

def test_chinese_voices():
    # 测试文本集合
    texts = [
        "今天天气真不错，阳光明媚，微风轻拂。",
        "欢迎使用语音合成系统，希望能给您带来帮助。",
        "春眠不觉晓，处处闻啼鸟。夜来风雨声，花落知多少。",
        "生活就像一杯茶，不会苦一辈子，但要学会品尝。"
    ]
    
    # 不同音色配置
    voices = [
        {"voice": "af_heart", "desc": "女声温柔"},
        {"voice": "af_bright", "desc": "女声明亮"},
        {"voice": "af_calm", "desc": "女声冷静"},
        {"voice": "am_calm", "desc": "男声冷静"},
        {"voice": "am_warm", "desc": "男声温暖"},
        {"voice": "am_bright", "desc": "男声明亮"}
    ]
    
    # 不同语速
    speeds = [0.8, 1.0, 1.2]
    
    # 创建输出目录
    os.makedirs("chinese_voices", exist_ok=True)
    
    # 初始化管道
    pipeline = KPipeline(lang_code='z')
    
    for voice in voices:
        print(f"\n测试音色: {voice['desc']}")
        
        for speed in speeds:
            print(f"\n当前语速: {speed}")
            
            for i, text in enumerate(texts):
                try:
                    print(f"\n文本 {i+1}: {text}")
                    
                    # 生成音频
                    generator = pipeline(
                        text=text,
                        voice=voice['voice'],
                        speed=speed
                    )
                    
                    # 保存音频
                    for _, (gs, ps, audio) in enumerate(generator):
                        output_file = f"chinese_voices/{voice['voice']}_speed{str(speed).replace('.', '_')}_sample{i+1}.wav"
                        import soundfile as sf
                        sf.write(output_file, audio, 24000)
                        print(f"已保存: {output_file}")
                        print(f"音素: {ps}")
                        break
                        
                except Exception as e:
                    print(f"生成失败: {str(e)}")

if __name__ == "__main__":
    test_chinese_voices()