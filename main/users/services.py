from flask import current_app
from ..core import Service, guard
from .models import User
import flask_praetorian as preatorian


class UsersService(Service):
  __model__ = User

  def get_authenticated_user_id(self):
    token = guard.read_token_from_header()
    claims = guard.extract_jwt_token(token)

    return claims['id']


  def get_authenticated_user(self):
    registration_token = guard.read_token_from_header()
    user = guard.get_user_from_registration_token(registration_token)

    return user


  def signup(self, req):
    """
      Registers a new user by parsing a POST request containing new user info and
      dispatching an email with a registration token
    """
    username = req.get('username', None)

    if self.first(username=username):
      return {'message': 'There is an user related with this username'}, 400

    # Hasing password to save encrypted
    req['password'] = guard.hash_password(req['password'])

    new_user = self.create(**req)

    ret = {'message': 'Success your user {}, has'.format(
        new_user
    )}, 201

users = UsersService()