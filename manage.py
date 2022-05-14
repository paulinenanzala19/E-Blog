from app import create_app,db
from flask_script import Manager,Server
from app.models import Blog,User
from  flask_migrate import Migrate, MigrateCommand

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Blog = Blog,User=User )
if __name__ == '__main__':
    manager.run()