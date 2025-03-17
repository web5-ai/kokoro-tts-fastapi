from setuptools import setup, find_packages

setup(
    name="kokoro-tts-service",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "python-dotenv>=0.19.0",
        "python-multipart>=0.0.5",
        "kokoro>=0.8.2",
        "misaki[zh]>=0.8.2",
        "soundfile",
        "torch>=1.10.0",
    ],
    entry_points={
        "console_scripts": [
            "kokoro-tts-service=kokoro_tts_service.main:run",
        ],
    },
)