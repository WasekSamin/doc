from googletrans import Translator
import os
from PyPDF2 import PdfFileReader

translator = Translator()

if os.path.exists("test.doc"):
    os.remove("test.doc")

wFile = open("./test.doc", "wb")

with open("./Database.pdf", "rb") as file:
    reader = PdfFileReader(file)

    num_pages = reader.numPages
    
    for p in range(num_pages):
        page = reader.getPage(p)
        text = page.extractText()

        translated_text = translator.translate(text, dest="bn")
        
        lines = translated_text.text
        lines = lines.replace("0", "০")
        lines = lines.replace("1", "১")
        lines = lines.replace("2", "২")
        lines = lines.replace("3", "৩")
        lines = lines.replace("4", "৪")
        lines = lines.replace("5", "৫")
        lines = lines.replace("6", "৬")
        lines = lines.replace("7", "৭")
        lines = lines.replace("8", "৮")
        lines = lines.replace("9", "৯")

        wFile.write(lines.encode())

wFile.close()