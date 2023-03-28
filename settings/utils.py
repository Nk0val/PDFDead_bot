import os
import shutil

def Clear_all(username):
    pathes = [f'rar_archive/{username}', f'splited_files/{username}', f'downloads_pdf/{username}']
    for path in pathes:
        shutil.rmtree(path)
