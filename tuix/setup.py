""" \
    This Is A Module Which Write For Configuring \
    The Package For Building That. \
"""

from setuptools import setup, find_packages


with open("./../README.md", "r", encoding="utf-8") as the_long_description_file:
    the_long_description = the_long_description_file.read()

setup(
    name="tuix",
    version="0.0.1",
    author="ABOLFAZL MOHAMMADPOUR",
    author_email="ABOLFAZLMOHAMMADPOURQAEMSHAHR@GMAIL.COM",
    url="https://github.com/abolfazlmohammadpour/tuix.git",
    description="""
                    Tuix is a powerful Python library designed to
                    revolutionize terminal interface development through
                    advanced ANSI escape code implementation. This toolkit
                    empowers developers to create sophisticated CLI
                    applications, interactive shells, and visually dynamic
                    terminal outputs with unprecedented ease.
                """,
    long_description=the_long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.13.2",
    install_requires=[
    ],
    extras_require={

    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
