from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='li_wrapper',
    version='0.0.1',
    description="A Python API Wrapper for 'Loja Integrada' e-commerce platform.",
    # url="https://github.com/javatechy/dokr",
    author="Thiago Costa",
    author_email="thiagodacosta@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['lojaintegrada'],
    install_required=['requests'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
