from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
    
VERSION = '0.0.1'
DESCRIPTION = 'Preserving History Through Code- Caesar Cipher'
LONG_DESCRIPTION = "Preserving History Through Code- Julius Caesar's Shift Cipher"

# Setting up
setup(
    name="caesar_cipher",
    version=VERSION,
    author="Statogale (Gabriel Okundaye)",
    author_email="<gabriel.okundaye@statogale.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'caesar_cipher = caesar_cipher.caesar_cipher:main',
        ],
    },
    install_requires=['requests_cache', 'langid'],
    keywords=['python', 'caesar cipher', 'julius caesar', 'history'],
    classifiers=[
        "Development Status :: 1 - Testing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)