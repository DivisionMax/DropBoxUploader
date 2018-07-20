import dropbox
import os
from dropbox.files import WriteMode

token = 'lPMo4FcCrwAAAAAAAAABqsVaWnzOqyMlWJmqSWowFiWL01Ci2tQYYoEjY3ogPeaf'
upload_folder = 'Pi Frames V1'

dbx = dropbox.Dropbox(token)

def backup(filepath):
    with open(filepath, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        upload_path = os.path.join(filepath) 
        print("Uploading " + filepath + " to Dropbox as " + upload_path + "...")
        dbx.files_upload(f.read(), '/test_folder/' + upload_path, mode=WriteMode('overwrite'))

backup('image.png')
