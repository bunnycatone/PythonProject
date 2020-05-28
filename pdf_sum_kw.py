#for now used for pdf

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import spacy
import textacy.extract

#load NLP

nlp = spacy.load('en_core_web_lg')

#needed to install pdfminer3k
def readPDF(pdfFile):
    rsm = PDFResourceManager()
    str = StringIO()
    lap = LAParams()
    device = TextConverter(rsm, str, laparams=lap)
    process_pdf(rsm, device, pdfFile)
    device.close()
    info = str.getvalue()
    str.close()
    return info

#pdf_f = urlopen("http://www.arbowebforest.com/android/ArboWebForestUserManual.pdf")
pdf_f = urlopen("http://www.samsontech.com/site_media/legacy_docs/H4n-manual.pdf")
outputS = readPDF(pdf_f)
#print(outputS)
#pdfFile.close()

text = outputS
doc = nlp(text)

#extract semi-structured statements
n1="ArboWebForest"
n2="H4n"
statements = textacy.extract.semistructured_statements(doc, n2)

#print results

print("highlights of "+n2+":")

for statement in statements:

    subject, verb, fact = statement

    print(f" -{fact}")
    print("--------")

###connected contents
noun_chunks = textacy.extract.noun_chunks(doc, min_freq=3)

#convert noun chunks to lowercase strings

noun_chunks = map(str, noun_chunks)

noun_chunks = map(str.lower, noun_chunks)

#print out ones 2 words long

for noun_chunk in set(noun_chunks):

    if len(noun_chunk.split(" ")) > 1:
        print(noun_chunk)


