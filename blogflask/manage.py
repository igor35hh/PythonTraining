import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Role, Permission, Post

app = create_app(os.getenv('FLASK_CONFIG') or 'production')

manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, Post=Post)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('app.tests', pattern='test*.py', top_level_dir=None)
    print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    #app.run(debug=True)
    manager.run() #runserver --host 0.0.0.0