import os
import setuptools

if os.path.exists('README.md'):
    with open('README.md', 'r') as fh:
        long_description = fh.read()

else:
    long_description = 'A python package for developing stack based execution tools'

setuptools.setup(
    name='xstack',
    version='1.0.1',
    author='Mike Malinowski',
    author_email='mike.external@outlook.com',
    description='xstack is an execution framework',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mikemalinowski/xstack',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        "factories",
        "signalling",
    ],
    keywords="xstack",
)
