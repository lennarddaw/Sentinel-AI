from setuptools import setup, find_packages

setup(
    name="sentinel-ai",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn"
    ],
    author="Lennard Gross",
    author_email="lennarddaw@gmail.com",
    description="Developer toolkit to detect poisoned data and protect AI models",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lennarddaw/Sentinel-AI",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)
