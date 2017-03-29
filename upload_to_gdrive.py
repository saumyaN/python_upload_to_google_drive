import logging
from apiclient.http import MediaFileUpload
from apiclient import discovery
from httplib2 import Http
import constants
from oauth2client.client import OAuth2WebServerFlow, SignedJwtAssertionCredentials
from oauth2client.tools import run_flow
from oauth2client.file import Storage
from oauth2client.tools import argparser
import requests, ast

logger = logging.getLogger(__name__)


class DriveService(object):

    @staticmethod
    def get_credentials():
        flow = OAuth2WebServerFlow(client_id=constants.CLIENT_ID, client_secret=constants.CLIENT_SECRET,
                                   scope=constants.SCOPE,
                                   redirect_uri='http://example.com/auth_return')
        flags = argparser.parse_args(args=[])
        storage = Storage('creds.data')
        credentials = run_flow(flow, storage, flags)
        print "access_token: %s" % credentials.access_token

    @staticmethod
    def authenticate_google_docs():
        credentials = SignedJwtAssertionCredentials(constants.EMAIL_ID, constants.SIGNED_KEY, constants.SCOPE)
        data = {
            'refresh_token': constants.REFRESH_TOKEN,
            'client_id': constants.CLIENT_ID,
            'client_secret': constants.CLIENT_SECRET,
            'grant_type': 'refresh_token',
        }
        r = requests.post('https://accounts.google.com/o/oauth2/token', data = data)
        credentials.access_token = ast.literal_eval(r.text)['access_token']
        service = discovery.build('drive', 'v2', http=credentials.authorize(Http()))
        media_body = MediaFileUpload('/tmp/dgtech.csv', mimetype='text/csv', resumable=True)
        file_metadata = {
          'title': 'dgtech.csv',
          'mimeType': 'application/vnd.google-apps.spreadsheet',
          'parents': [{'id': constants.FOLDER_ID}]
            }
        try:
            import pdb
            pdb.set_trace()
            param = {}
            children = service.children().list(folderId=constants.FOLDER_ID, **param).execute()
            file_list = [str(item['id']) for item in children['items']]
            print(file_list)
            service.children().delete(folderId=constants.FOLDER_ID, childId=file_list[0]).execute()
            file = service.files().insert(body=file_metadata, media_body=media_body, fields='id').execute()
            #logger.info("file id of the file upoaded = %s ", (file.get('id')))
        except Exception as e:
            print(str(e))
            #logger.exception("Exception occured while uploading the file")