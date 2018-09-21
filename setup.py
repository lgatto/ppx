import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ppx",
    version="0.1.2",
    author="William E Fondrie",
    author_email="fondriew@gmail.com",
    description="A Python interface to the ProteomeXchange Repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wfondrie/ppx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
)
