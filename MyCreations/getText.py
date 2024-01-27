#!python3
import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
        
    return '\n'.join(fullText)
    
print(getText('c:\\users\\bryne\\documents\\TestDoc.docx'))
