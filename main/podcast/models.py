# -*- coding: utf-8 -*-
"""
    main.users.models
    ~~~~~~~~~~~~~~~~~~~~~
    User models
"""

from ..core import db
from ..helpers import JsonSerializer


class PodcastasJsonSerializer(JsonSerializer):
  __json_public__ = ['id', 'artistName', 'kind']


class Podcasts(UserJsonSerializer, db.Model):
  __tablename__ = 'podcasts'

  id = db.Column(db.String(256), primary_key=True)
  artistName = db.Column(db.String(255))
  kind = db.Column(db.String(255))
  name = db.Column(db.String(255))
  artistName = db.Column(db.String(255))
  url = db.Column(db.String(255))
