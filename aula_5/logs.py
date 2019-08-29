import os
import logging

import dotenv

dotenv.load_dotenv()

FORMAT_STRING = '''

%(asctime)s | %(levelname)s | 
%(filename)s | %(message)s

'''.replace('\n', '').strip()

DATE_FORMAT_STRING = '''

%d/%m/%Y %H:%M:%S

'''.replace('\n', '').strip()

opts = {
    'filename': 'app.log',
    'level': int(os.getenv('DEBUG_LEVEL') or 0),
    'format': FORMAT_STRING,
    'datefmt': DATE_FORMAT_STRING
}

logging.basicConfig(**opts)

logging.debug('Message de DEBUG')
logging.info('Message de INFO')
logging.warning('Message de WARNING')
logging.error('Message de ERROR')
logging.critical('Message de CRITICAL')