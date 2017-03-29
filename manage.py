
from flask_script import Manager
from app import create_app
from populatesheet import PopulateSpreadSheet


app = create_app()


manager = Manager(app)
manager.add_command('populate_spreadsheet', PopulateSpreadSheet())


if __name__ == '__main__':
    manager.run()

