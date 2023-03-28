import os
import shutil
from settings.config import SPLITED_FILES_DIR, RAR_FILES_DIR, PDF_DIR

def Clear_all(username):
    pathes = [f'{RAR_FILES_DIR}/{username}', f'{SPLITED_FILES_DIR}/{username}', f'{PDF_DIR}/{username}']
    for path in pathes:
        shutil.rmtree(path)
