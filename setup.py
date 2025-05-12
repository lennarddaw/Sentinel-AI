from setuptools import setup, find_packages

setup(
    name="sentinel_ai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn"
    ],
    author="Lennard Gross",
    description="Developer toolkit to detect poisoned data and AI model risks",
    license="MIT",
    include_package_data=True,
)
