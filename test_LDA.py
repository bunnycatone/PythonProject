#topic model
#lda
#gibbs sampling
#alfa document-topic beta topic-word
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
import pandas as pd
import gensim
from gensim import corpora
import nltk
nltk.download('wordnet')

text1="Bunny is the best thing in the world."
text2="Eating fruits are healthy and fruits are not very expensive."
text3="The best way to learn a language is by living in the country where the language is spoken."
text4="Free math problem solver answers your algebra homework questions with step-by-step explanation."
text5="When a person is feeling empty, they are plunged into an inner abyss. Are you empty inside?"
text6="My sister likes red apples, bananas and grapes."
text_all=[text1,text2,text3,text4,text5]

#stop words
stopwords=pd.read_csv('/home/bunny/Documents/pm_plottu/text/stop_words.txt',index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')
stopwords=stopwords['stopword'].values

#lemma
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stopwords])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in text_all]

# create dic
dictionary = corpora.Dictionary(doc_clean)

# use dic DT matrix
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# use gensim to create LDA model obj
Lda = gensim.models.ldamodel.LdaModel

# train LDA model on DT matrix
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

print(ldamodel.print_topics(num_topics=3, num_words=3))

