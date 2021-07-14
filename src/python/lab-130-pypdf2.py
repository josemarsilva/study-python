#
# filename    : lab-130-pypdf2.py
# Description : Open, read, write, manipulate PDF files
# Docs        :
#               * https://pythonhosted.org/PyPDF2/
#               * https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
# Requirements:
#               * pip install openpyxl
#

import PyPDF2

pdf_file_name_1_of_2 = 'file-11-pdf-part-1-of-2.pdf'
pdf_file_name_2_of_2 = 'file-12-pdf-part-2-of-2.pdf'

pdf_file_merger = PyPDF2.PdfFileMerger()
pdf_file_name_merged = 'file-13-pdf-joinned.pdf'

pdf_file_1_of_2 = open(pdf_file_name_1_of_2, 'rb')
pdf_file_merger.append(pdf_file_1_of_2)
pdf_file_2_of_2 = open(pdf_file_name_2_of_2, 'rb')
pdf_file_merger.append(pdf_file_2_of_2)

with open(pdf_file_name_merged, 'wb') as file:
    pdf_file_merger.write(file)
