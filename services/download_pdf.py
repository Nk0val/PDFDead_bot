import os
from settings.config import PDF_DIR

def Download_pdf(bot, message):

    username = message.from_user.first_name

    path = f'./{PDF_DIR}/{username}'
    if not os.path.exists(path):
        os.mkdir(path)

    try:
        file_name = message.document.file_name
        file_info = bot.get_file(message.document.file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        with open(f'{path}/{file_name}_by_{username}.pdf', 'wb') as pdf_file:
            pdf_file.write(downloaded_file)

        return "Great! The file was successfully delivered to the server!", 0, file_name

    except:
        return "The file could not be delivered to the server, try again!", 1, None,

