#!Python3

import PyPDF2
import os
os.chdir('c:\\users\\bryne\\documents')

'''pdfFile = open('TeacherLoanForgiveness - Copy.pdf','rb') # rb = "read binary"

reader = PyPDF2.PdfReader(pdfFile)

totalPages =len(reader.pages) 

page = reader.pages[0]

page.extract_text()

for pageNum in range(len(reader.pages)):
    #print('Hello World!')
    print(reader.pages[pageNum].extract_text())

'''

pdf1File = open('TeacherLoanForgiveness - Copy.pdf', 'rb')
pdf2File = open('TeacherLoanForgiveness - Copy (2).pdf', 'rb')

reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)

writer = PyPDF2.PdfWriter()

for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)

for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)

outputFile = open('CombinedForvieness.pdf','wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
