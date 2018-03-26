#!/usr/bin/env python
import config
from distutils.core import setup

setup(name=config.NAME,
      version=config.VERSION,
      description=config.DESCRIPTION,
      author=config.AUTHOR,
      author_email=config.AUTHOR_EMAIL,
      url=config.URL,
      packages=['.'],
      scripts=['eu']
     )
