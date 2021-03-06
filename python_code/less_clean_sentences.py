import codecs
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import LineTokenizer
from nltk.tokenize import word_tokenize
import re

index_num = 0

# NLTK's default French stopwords
default_stopwords = set(nltk.corpus.stopwords.words('french'))

input_files = ['mont_analog.txt', 'beauverie.txt']

for f in input_files:
    fp = codecs.open(f, 'r', 'utf-8')


    t = fp.read()

    new_lines = []

    tokenizer = nltk.data.load('tokenizers/punkt/PY3/french.pickle')

    lines_split = tokenizer.tokenize(t)

    compiled_pattern = re.compile(r"([a-zA-ZÀ-Ÿ]+['’])([a-zA-ZÀ-Ÿ]*)")


    for line in lines_split:

        words = []
        final_words = []

        tokens = word_tokenize(line)
        new_tokens = []
        for token in tokens:
            search_results = re.findall(r"['’]",token)
            if search_results and len(search_results) == 1:
                new_tokens.extend(re.split(compiled_pattern,token)[1:3])
            else:
                new_tokens.append(token)


        words.append(new_tokens)
        print(words)

        for x in words:
            for y in x:
                y.lower()

        # Remove single character words/punctuation
                if len(y) <= 1:
                    x.remove(y)

        # Remove stopwords
                if y not in default_stopwords:
                    if  y.isnumeric():
                        pass
                    else:
                        final_words.append(y)


        for word in final_words:
            word = [item.replace("_", "") for item in word]
            word = [item.replace("|", "") for item in word]
            pattern = '[0-9]'
            word = [re.sub(pattern, '', i) for i in word]

        str_words = " ".join(final_words)
        new_lines.append(str_words)

        for line in new_lines:
            if not line:
                new_lines.remove(line)

        print(new_lines)

    with open(('sentences_' + input_files[index_num]), 'w') as f:
                f.write('\n\n'.join(new_lines))

    index_num += 1
