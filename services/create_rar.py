import patoolib
import pathlib
import os
from settings.config import RAR_FILES_DIR, SPLITED_FILES_DIR

def Create_rar(username):

    path = f'{RAR_FILES_DIR}/{username}'
    if not os.path.exists(path):
        os.mkdir(path)

    current_directory = pathlib.Path(f'{SPLITED_FILES_DIR}/{username}/')
    current_pattern = '*.pdf'

    try:
        files_to_archive = []
        for currentFile in current_directory.glob(current_pattern):
            files_to_archive.append(str(currentFile))

        patoolib.create_archive(f'{path}/{username}.rar', files_to_archive)

        return "Archive was created!"

    except:

        return "Error, archive dont created"





