"""
Convert document files to raw text file
For text lemmatization process
"""
from docx import Document
import io
import shutil
import os

def convertDocxToText(path):
    for d in os.listdir(path):
        fileExtension=d.split(".")[-1]
        if fileExtension =="docx":
            docxFilename = path + d
            print(docxFilename)
            document = Document(docxFilename)
            textFilename = path + d.split(".")[0] + ".txt"
            with io.open(textFilename,"w", encoding="utf-8") as textFile:
                for para in document.paragraphs: 
                    textFile.write(unicode(para.text))

path= "C:\Desktop\python\text.docx"
convertDocxToText(path)