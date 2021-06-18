# NLP-on-Daumal
NLP on novels by René Daumal. This repository is an outgrowth of the [Non-English NLP Tutorial](https://github.com/ian-nai/Non-English-NLP-Tutorial).
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/3/32/Charles_P%C3%A9guy_by_Eug%C3%A8ne_Pirou.jpg" height="426" width="272"/>
</p>
## Getting Started
Install required dependencies:

```
pip3 install -r requirements.txt
```
## Scope
This repository is a starting point for using NLP to analyze and visualize various aspects of the two novels written by René Daumal. Code may be updated and added as necessary while the project progresses.

## What This Repository Contains
#### <span style="text-decoration: underline">CSVs</span>
A collection of .csv files containing data gleaned from analyzing the texts using NLP. The sub-folders in this section contain data for different models that were used to process the texts, the fr_core_news_lg and fr_dep_news_trf models from spaCy and the Stanza French model from Stanford's Stanza library. There is also a folder for data used in visualizing the texts using graphs.

#### Original Texts
The original texts of Daumal's two novels: <em>La grande beuverie</em> and <em>Le Mont Analogue. Roman d'aventures alpines, non euclidiennes et symboliquement authentiques</em>.

#### Pickle Files
These are pickled NLP models (using the fr_dep_news_trf spaCy model) of the original texts, broken up into smaller chunks to avoid file size limitations.

#### Python Code
The Python files contained here perform the NLP used to generate the CSVs and visualizations. The files are as follows:
* analog_network_map.py - Generate a network map of select characters in Mount Analogue.
* clean_sentences.py - Tokenize texts by sentences and remove stopwords, then output the results to a new text file.
* csv_fr_core_news_lg.py - Run the spaCy csv_fr_core_news_lg model on the text(s) included in the code and output the results to a CSV file.
* csv_fr_dep_news_trf.py - Run the spaCy csv_fr_dep_news_trf model on the text(s) included in the code and output the results to a CSV file.
* csv_stanza.py - Run Stanford's Stanza library on the text(s) included in the code and output the results to a .csv file.
* less_clean_sentences.py - An alternate version of clean_sentences.py that leaves more of the original sentence intact.
* make_pickles.py - Create the pickle files for uploading to GitHub.
* visualizations.py - Code to generate various visualizations of textual data using matplotlib.

#### Tokenized Sentences
These folders contain text files of the texts tokenized into sentences.

#### Visualizations
Visualizations of textual data in PNG and interactive HTML/JS format. This folder may be added to in the future.
