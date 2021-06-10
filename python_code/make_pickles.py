import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
import re
from compress_pickle import dump, load

index_num = 0


# Note: creating this many pickle files at once will be very slow
files = files = ['clean_sentences_mont_analog.txt', 'clean_sentences_beauverie.txt']
nlp = spacy.load("fr_dep_news_trf")


for f in files:
    with open(f) as file:
        text_data = file.read()


    doc = nlp(text_data)


    fname1 = ("nlp_" + (files[index_num]) + ".pkl")
    fname2 = ("nlp_" + (files[index_num]) + ".gz")

    dump(doc,fname1)
    dump(doc, fname2)

    index_num += 1
