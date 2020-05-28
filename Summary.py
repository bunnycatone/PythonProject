import codecs
import spacy
import textacy.extract

#1 extract text from pdf
from tika import parser

source = parser.from_file('/home/bunny/Documents/pm_plottu/H4n-manual.pdf')
#print(raw['content'])
with open('file.txt', 'w') as f:
    print(source['content'], file=f)

#2 clean file
clean_lines = []
with open("file.txt", "r") as f:
    lines = f.readlines()
    clean_lines = [l.strip() for l in lines if l.strip()]

with open("file.txt", "w") as f:
    f.writelines('\n'.join(clean_lines))

file = codecs.open('file.txt', encoding='utf-8')
content = file.read()
#print(content)

#3 load nlp
nlp = spacy.load('en_core_web_lg')
text =nlp(content)

#4 extract semi-structured statements

i="H4n"

statements = textacy.extract.semistructured_statements(text,i)

#5 print the results

print("highlights of " +i +":")

for statement in statements:

    subject, verb, fact = statement

    print(f" ---{fact}")



