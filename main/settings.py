# -*- coding: utf-8 -*-
"""
    main.settings
    ~~~~~~~~~~~~~~~
    main settings module
"""
from dotenv import load_dotenv
load_dotenv()

import os

class Config(object):
  DEBUG = False
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
