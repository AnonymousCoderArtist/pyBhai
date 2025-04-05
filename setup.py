from setuptools import setup, find_packages

setup(
    name="bhai_py",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bhai_py = bhai_py:main",
        ],
    },
    author="Your Name",
    description="A fun programming language with Hinglish syntax",
    long_description="A simple programming language that translates Hinglish syntax into Python.",
    license="MIT",
    keywords="programming language Hinglish",
)