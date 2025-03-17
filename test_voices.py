from kokoro import KPipeline
import os

def test_all_voices():
    # 测试文本
    texts = {
        'z': "今天天气真不错，阳光明媚。",  # 中文
        'a': "The weather is nice today.",  # 美式英语
        'b': "The weather is lovely today.",  # 英式英语
        'j': "今日の天気は本当にいいですね。",  # 日语
        'e': "El tiempo está muy bueno hoy.",  # 西班牙语
        'f': "Le temps est très beau aujourd'hui.",  # 法语
        'h': "आज मौसम बहुत अच्छा है।",  # 印地语
        'i': "Il tempo è molto bello oggi.",  # 意大利语
        'p': "O tempo está muito bom hoje."  # 葡萄牙语
    }
    
    # 所有可能的音色
    voices = [
        'af_heart', 'af_bright', 'af_calm',
        'am_calm', 'am_warm', 'am_bright'
    ]
    
    # 创建输出目录
    os.makedirs("voice_samples", exist_ok=True)
    
    # 测试每种语言
    for lang_code, text in texts.items():
        print(f"\n测试语言代码: {lang_code}")
        try:
            # 初始化管道
            pipeline = KPipeline(lang_code=lang_code)
            
            # 测试每种音色
            for voice in voices:
                try:
                    print(f"\n尝试音色: {voice}")
                    
                    # 生成音频
                    generator = pipeline(
                        text=text,
                        voice=voice,
                        speed=1.0
                    )
                    
                    # 保存音频
                    for _, (gs, ps, audio) in enumerate(generator):
                        output_file = f"voice_samples/{lang_code}_{voice}.wav"
                        import soundfile as sf
                        sf.write(output_file, audio, 24000)
                        print(f"✓ 成功生成: {output_file}")
                        print(f"音素: {ps}")
                        break
                        
                except Exception as e:
                    print(f"✗ 音色 {voice} 不支持: {str(e)}")
                    
        except Exception as e:
            print(f"✗ 语言 {lang_code} 初始化失败: {str(e)}")

if __name__ == "__main__":
    test_all_voices()