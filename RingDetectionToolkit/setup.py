from setuptools import setup, find_packages

setup(
    name="RingDetectionToolkit",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26.0,<1.27.0",
        "matplotlib==3.7.1",
        "scikit-learn==1.2.2",
        "scipy==1.10.1",
        "tqdm==4.65.0",
        "sphinx==7.2.6",
        "sphinx_rtd_theme==1.3.0",
        "ghp-import==2.1.0",
    ],
)
