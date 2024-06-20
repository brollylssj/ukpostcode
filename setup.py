from setuptools import setup, find_packages

setup(
    name="ukpostcode",
    version="1.0",
    packages=find_packages(),
    description="A library to validate and format UK postcodes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Tomasz Hanusiak",
    author_email="tomhanusiak@gmail.com",
    url="https://github.com/brollylssj/ukpostcode",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'ukpostcode-cli=ukpostcode.__main__:main',
        ],
    },
)
