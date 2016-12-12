# -*- coding: utf-8 -*-
from distutils.core import setup
from os.path import expanduser, join
from shutil import copyfile
home = expanduser("~")

copyfile("studdp/default_config.json", "studdp/config.json")

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='StudDP',
    version='1.0',
    author='Maxim Schuwalow',
    author_email='mschuwalow@uos.de',
    packages=['studdp'],
    install_requires = required,
    data_files=[(join(home,".config/studdp"), ["studdp/config.json"])],
    url='https://github.com/MSchuwalow/StudDP.git',
    license='MIT',
    description='StudIP file downloader in python',
    long_description=open('README.md').read(),
    zip_safe=False,
    entry_points={
      "console_scripts": [
        "StudDP = studdp.StudDP:main",
        "stopDP = studdp.stopDP:stop",
        ],
    },
)
