

import re
from collections import Counter

# Creating a list to count how many times each character's name appears in the text
characters = ['judith', 'sogol', 'alphonse', 'ivan']
char_counts = []

# Open our cleaned, tokenized file
f = open("cleaned_analog.txt", "r")
data = f.readlines()

# Splitting the raw text into chapters to count character co-occurrences
f2 = open("mont_analog.txt", "r")
uncleaned = f2.read()
chapters = uncleaned.split('CHAPITRE')
print(len(chapters)) # print how many chapters are in the text

# Creating an empty dictionary for our character counts
d = dict()

# Looping through each line of the file
for word in data:
    # Remove the leading spaces and newline character
    word = word.strip()

    if word in characters:
     # Check if the word is already in our dictionary
        if word in d:
            # Increment our count by 1
            d[word] = d[word] + 1
        else:
            # Add the word to our dictionary with count 1
            d[word] = 1
    else:
        pass
print(d)

# Setting up our co-occurrence counts, initializing each value as 0
judith_sogol = 0
judith_alphonse = 0
judith_ivan = 0
sogol_alphonse = 0
sogol_ivan = 0
alphonse_ivan = 0

# Looping through our chapters and incrementing our co-occurrence counts by one if the characters both appear
for x in chapters:
    if 'Judith' in x:
        if 'Sogol' in x:
            judith_sogol += 1
        if 'Alphonse' in x:
            judith_alphonse += 1
        if 'Ivan' in x:
            judith_ivan += 1
    if 'Sogol' in x:
        if 'Alphonse' in x:
            sogol_alphonse += 1
        if 'Ivan' in x:
            sogol_ivan += 1
    if 'Alphonse' in x:
        if 'Ivan' in x:
            alphonse_ivan += 1

# Print our co-occurrence counts
print(judith_sogol, judith_alphonse, sogol_alphonse, sogol_ivan, alphonse_ivan)

# Converting our dictionary into a list, then multiplying the values by 10 to make the values visibly
# impact the graph when we adjust node size by frequency of character occurrence.
char_appearances = list(d.values())
char_sizes = [x * 10 for x in char_appearances]

# Adding our numbers of co-occurrences into a list to alter the weighting of the edges connecting our nodes
edge_weights = []
edge_weights.extend([judith_sogol, judith_alphonse, sogol_alphonse, sogol_ivan, alphonse_ivan])

'''
GRAPHING
'''

# Import networkx and matplotlib
import networkx as nx
import matplotlib.pyplot as plt

# Creating our graph and adding in our character names as nodes
G=nx.Graph()
G.add_nodes_from(["Judith", "Alphonse", "Sogol", "Ivan"])

# Setting up edges and their weights based on number of co-occurrences
if judith_sogol > 0:
    G.add_edge("Judith", "Sogol", weight=edge_weights[0])
if judith_alphonse > 0:
    G.add_edge("Judith", "Alphonse", weight=edge_weights[1])
if sogol_alphonse > 0:
    G.add_edge("Sogol", "Alphonse", weight=edge_weights[2])
if sogol_ivan > 0:
    G.add_edge("Sogol", "Ivan", weight=edge_weights[3])
if alphonse_ivan > 0:
    G.add_edge("Alphonse", "Ivan", weight=edge_weights[4])

# Specifying the layout of the graph
pos = nx.circular_layout(G)

# Setting the weights for the edges
weights = nx.get_edge_attributes(G,'weight').values()

# Drawing the graph, saving it to a file, and then displaying it within Python
nx.draw(G, pos, with_labels=True, node_size=char_sizes, width=list(weights))
plt.savefig("network_visualization.png")
plt.show()
