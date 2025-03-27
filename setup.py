from setuptools import setup, find_packages

setup(
    name="gpt_genie",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Mayank Kumar",
    description="A Python package for free interaction with ChatGPT using an access token, featuring tools and methods to simplify ChatGPT usage.",
    url="https://github.com/kidminks/gpt_genie",
)