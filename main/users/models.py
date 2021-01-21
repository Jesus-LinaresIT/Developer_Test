# -*- coding: utf-8 -*-
"""
    main.users.models
    ~~~~~~~~~~~~~~~~~~~~~
    User models
"""
import datetime
from ..core import db, guard
from ..helpers import JsonSerializer


class UserJsonSerializer(JsonSerializer):
  __json_public__ = ['id', 'username', 'roles']


class User(UserJsonSerializer, db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True, unique=True)
  password = db.Column(db.String(256), nullable=False)
  is_active = db.Column(db.Boolean, default=False, server_default='true')
  last_login_at = db.Column(db.DateTime())
  registered_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
  roles = db.Column(db.Text, nullable=False)


  @property
  def rolenames(self):
      try:
          return self.roles.split(',')
      except Exception:
          return []

  @classmethod
  def lookup(cls, username):
    return cls.query.filter(((cls.username == username))).one_or_none()

    #return cls.query.filter_by(username=username).one_or_none()

  @classmethod
  def identify(cls, id):
      return cls.query.get(id)

  @property
  def identity(self):
      return self.id


  def is_valid(self):
    return self.is_active

