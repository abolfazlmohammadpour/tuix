""" \
    This Is A Module Which Write For Configuring \
    The Package For Building That. \
"""

from setuptools import setup, find_packages


with open("./../README.md", "r", encoding="utf-8") as the_long_description_file:
    the_long_description = the_long_description_file.read()

setup(
    name="tuix",
    version="0.0.3",
    author="ABOLFAZL MOHAMMADPOUR",
    author_email="ABOLFAZLMOHAMMADPOURQAEMSHAHR@GMAIL.COM",
    url="https://github.com/abolfazlmohammadpour/tuix.git",
    description="A Revolution In UI/UX Of Terminal: tuix",
    long_description=the_long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.10",
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
