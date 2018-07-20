import os
import logging
import yaml
import dropbox
from dropbox.files import WriteMode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = None

with open("config.yml", 'r') as stream:
    try:
        config = yaml.load(stream)
    except yaml.YAMLError as exc:
        logger.error(exc)

logger.info(config)

token = config['token']
upload_folder = config['dbx_folder']

dbx = dropbox.Dropbox(token)

def backup(filepath):
    with open(filepath, 'rb') as f:
        # Upload path must include a forward-slash at the start
        upload_path = os.path.join(filepath) 
        print("Uploading " + filepath + " to Dropbox as " + upload_path + "...")
        dbx.files_upload(f.read(), '/test_folder/' + upload_path, mode=WriteMode('overwrite'))

backup('image.png')
