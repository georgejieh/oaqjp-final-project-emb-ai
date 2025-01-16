from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A package for emotion detection using the Watson NLP Emotion Predict API.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/EmotionDetection",  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)