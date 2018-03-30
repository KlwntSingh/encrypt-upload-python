#!/usr/bin/env python
import config
from distutils.core import setup

import distutils.sysconfig as syspath
print(dir(syspath))


setup(name=config.NAME,
      version=config.VERSION,
      description=config.DESCRIPTION,
      author=config.AUTHOR,
      author_email=config.AUTHOR_EMAIL,
      url=config.URL,
      license=config.LICENSE,
      packages=['services'],
      py_modules = ['config'],
      scripts=['eu']
     )