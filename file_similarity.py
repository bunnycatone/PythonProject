import spacy
from spacy import displacy
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

#load nlp
nlp=spacy.load('en_core_web_lg')

#pdf
def read_pdf(pdfFile):
    rsm = PDFResourceManager()
    str = StringIO()
    lap = LAParams()
    device = TextConverter(rsm, str, laparams=lap)
    process_pdf(rsm, device, pdfFile)
    device.close()
    content = str.getvalue()
    str.close()
    return content


pdf1 = urlopen("http://www.samsontech.com/site_media/legacy_docs/H4n-manual.pdf")
pdf2 = urlopen("http://www.arbowebforest.com/android/ArboWebForestUserManual.pdf")
output1 = read_pdf(pdf1)
output2 = read_pdf(pdf2)
text1 = nlp(output1)
text2 = nlp(output2)
target = nlp("bunny is the best. What is H4n? Can you explain?") #test file, change to other pdf files


#similarity of files
print(target.similarity(text1))
print(target.similarity(text2))

