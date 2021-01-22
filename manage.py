import click
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask.cli import with_appcontext

from main.core import db, guard, Service
from main.models import User
from main.users.services import users

from main import create_app
from flask_script import Manager, Command


class create_users(Command):
  """Create a user"""


  def run(self):
    Admin_user = User(username='xzegga', password=guard.hash_password('super.super'), roles='admin')
    users.save(Admin_user)

app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('create_users', create_users())

if __name__ == '__main__':
    manager.run()



