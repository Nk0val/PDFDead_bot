import patoolib
import pathlib
import os

def Create_rar(file_name,username):

    path = f'rar_archive/{username}'
    if not os.path.exists(path):
        os.mkdir(path)

    current_directory = pathlib.Path(f'splited_files/{username}/')
    current_pattern = '*.pdf'

    try:
        files_to_archive = []
        for currentFile in current_directory.glob(current_pattern):
            files_to_archive.append(str(currentFile))

        patoolib.create_archive(f'{path}/{username}.rar', files_to_archive)

        return "Archive was created!"

    except:

        return "Error, archive dont created"





