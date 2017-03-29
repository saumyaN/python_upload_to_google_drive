import logging
from flask_script import Command
from upload_to_gdrive import DriveService
__name__ = 'google_spreadsheet'

logger = logging.getLogger(__name__)



class PopulateSpreadSheet(Command):

    def run(self, *args, **options):
        self.populate_db(*args, **options)

    def populate_db(self, *args, **options):
        try:
            DriveService.authenticate_google_docs()
        except Exception as e:
            print(str(e))

