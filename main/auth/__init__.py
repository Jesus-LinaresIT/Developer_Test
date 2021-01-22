# -*- coding: utf-8 -*-
"""
    main.auth
    ~~~~~~~~~~~~~~
    main auth package
"""

from .services import auth
from ..router import route
from ..core import guard
from flask import Blueprint, request


bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['POST'])
def signin():
  """
  Logs a user in by parsing a POST request containing user credentials and
  issuing a JWT token.
  """
  req = request.get_json(force=True)
  return auth.signin(req)


@bp.route('/refresh', methods=['POST'])
def refresh():
  """
    Refreshes an existing JWT by creating a new one that is a copy of the old
    except that it has a refrehsed access expiration.
  """
  return auth.refresh_token()


@bp.route('/logout', methods=['DELETE'])
def logout():
  """
    invalidate token on user logout
  """
  return auth.invalid_token()
