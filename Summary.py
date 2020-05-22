#spacy summary test

import spacy

import textacy.extract

# Load NLP model

nlp = spacy.load('en_core_web_lg')

text ="""An invoice specifies what a buyer must pay the seller 
according to the seller’s payment terms. Payment terms indicate 
the maximum amount of time that a buyer has to pay for the 
goods and/or services that they have purchased from the seller.

An invoice indicates that a buyer owes money to a seller. 
Therefore, from a seller’s point of view, an invoice for the 
sale of goods and/or service is called a sales invoice. From a 
buyer’s point of view, an invoice for the cost of goods 
and/or services rendered is called a purchase invoice.

An invoice has historically been a paper document mailed 
to the buyer, but these days sellers can request 
payments online with electronic invoices.

"""

doc = nlp(text)

# Extract semi-structured statements

i="invoice"

statements = textacy.extract.semistructured_statements(doc,i)

# Print the results

print("highlights of " +i)

for statement in statements:

 subject, verb, fact = statement

 print(f" -{fact}")

