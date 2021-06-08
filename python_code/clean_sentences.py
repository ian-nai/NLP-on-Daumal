import codecs
import nltk
from nltk.corpus import stopwords

# We'll use NLTK's default French stopwords
default_stopwords = set(nltk.corpus.stopwords.words('french'))

# Our input file
input_files = ['beauverie.txt']

lines_cleaned = []
for f in input_files:
    fp = codecs.open(f, 'r', 'utf-8')

    t = fp.read()

    tokenizer = nltk.data.load('tokenizers/punkt/PY3/french.pickle')

    lines_split = tokenizer.tokenize(t)

    for f in lines_split:
# Tokenize the text into words
        words = nltk.word_tokenize(f)

# Remove single-character tokens (mostly punctuation)
        words = [word for word in words if len(word) > 1]

# Remove numbers
        words = [word for word in words if not word.isnumeric()]

# Lowercase all words (default_stopwords are lowercase too)
        words = [word.lower() for word in words]

# Remove stopwords
        words = [word for word in words if word not in default_stopwords]

        str_words = " ".join(words)
        lines_cleaned.append(str_words)

        for line in lines_cleaned:
            if not line:
                lines_cleaned.remove(line)
# Save our new file as 'cleaned_text.txt'
        with open('clean_sentences_' + input_files[index_num]), 'w') as g:
            for item in lines_cleaned:
                    g.write("\n" + (str(item)))
        index_num += 1
