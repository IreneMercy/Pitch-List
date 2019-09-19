from flask_script import Manager , Server
from app import create_app,db
from app.models import User,Post,Commenting,Upvote,Downvote
from flask_migrate import Migrate,MigrateCommand


app=create_app()
manager =  Manager(app)
migrate = Migrate(app,db)
manager.add_command('server',Server(use_debugger=True))
manager.add_command('db', MigrateCommand    )


@manager.shell
def add_shell_context():
    return {"app":app,"db":db,"User":User,"Post":Post}

if __name__=="__main__":
    manager.run()
