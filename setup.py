import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nigeria-bank-algos", # Replace with your own username
    version="0.1.1",
    author="Samson Ilemobayo",
    author_email="ilemobayosamson@gmail.com",
    description="A small bank algorithm that predict nigeria bank",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samkayz/nigeria-bank-algo.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)