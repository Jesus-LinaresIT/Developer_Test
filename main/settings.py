# -*- coding: utf-8 -*-
"""
    main.settings
    ~~~~~~~~~~~~~~~
    main settings module
"""
from dotenv import load_dotenv
load_dotenv()

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/podcast.db')

class DevelopementConfig(Config):
  PYTHONPROFILEIMPORTTIME = 1
  DEBUG = True

config = {
  'development': DevelopementConfig,
  'default': DevelopementConfig
  }