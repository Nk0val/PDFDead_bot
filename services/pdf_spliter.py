from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def Split(file_path, file_name, step, username):
    pdf = PdfFileReader(file_path)
    page_nums = []
    counter = 0

    path = f'splited_files/{username}'

    if not os.path.exists(path):
        os.mkdir(path)

    try:
        for page in range(pdf.getNumPages()):

            page_nums.append(page)

            if page == counter+step:
                pdf_writer = PdfFileWriter()

                for i in range(counter, len(page_nums)):
                    pdf_writer.addPage(pdf.getPage(i))

                    output = f'{file_name}_{counter}_{len(page_nums)}.pdf'
                    with open(f'{path}/{output}', 'wb') as output_file:
                        pdf_writer.write(output_file)

                counter += step

        return "Your file was successfully splited!", 0

    except:

        return "There was an error splitting your file, try again!", 1