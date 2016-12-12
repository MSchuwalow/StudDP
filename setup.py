# -*- coding: utf-8 -*-
from setuptools import setup
from os.path import expanduser, join
home = expanduser("~")

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='StudDP',
    version='1.1',
    author='Maxim Schuwalow',
    author_email='mschuwalow@uos.de',
    packages=['studdp'],
    install_requires = required,
    data_files=[(join(home,".config/studdp"), ["studdp/config.json"])],
    url='https://github.com/MSchuwalow/StudDP.git',
    license='MIT',
    description='StudIP file downloader in python',
    long_description=open('README.md').read(),
    keywords = "StudIP Downloader Osnabrueck UOS utility",
    zip_safe=False,
    entry_points={
      "console_scripts": [
        "StudDP = studdp.StudDP:main",
        "stopDP = studdp.stopDP:stop",
        ],
    },
)
