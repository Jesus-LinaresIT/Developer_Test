from flask import current_app
from ..core import Service, guard
from ..users.services import users
from .models import Token


class AuthService(Service):
  __model__ = Token

  def signin(self, req):

    username = req.get('username', None)
    password = req.get('password', None)

    user = guard.authenticate(username, password)
    ret = {'jwtToken': guard.encode_jwt_token(
      user,
      username=user.username,
      roles=user.rolenames
    )}

    return ret, 200

  def refresh_token(self):

    old_token = guard.read_token_from_header()
    new_token = guard.refresh_jwt_token(old_token)
    ret = {'jwtToken': new_token}

    return ret, 200


  def invalid_token(self):
    token = guard.read_token_from_header()
    jti = guard.extract_jwt_token(token)["jti"]
    blacklist.blacklist_jti(jti)
    rv, code = {"success": True, "message": "token invalidated"}, 200
    return rv, code


  def check_permissions(self, model_instance):
    if not model_instance:
      return {'message': 'This appointment doesn\'t exist.'}, 404

    if model_instance.user_id is not users.get_authenticated_user_id():
      return ({'message': 'Access denied'}, 401)


auth = AuthService()
