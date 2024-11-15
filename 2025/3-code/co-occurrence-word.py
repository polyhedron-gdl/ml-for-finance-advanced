import networkx as nx
import matplotlib.pyplot as plt
import nltk
import string

from nltk.tokenize import word_tokenize
from nltk.corpus   import stopwords
from collections   import Counter
from itertools     import combinations

# Ensure nltk tokenizers are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Step 0: Preprocessing function
def preprocess_text(sentence):
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Remove punctuation
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    return tokens

sentence = '''
The same principle, the same love of
system, the same regard to the beauty
of order, of art and contrivance, frequently
serves to recommend those institutions
which tend to promote the
public welfare.
'''

# Step 1: Tokenize the sentence
#tokens = word_tokenize(sentence.lower())
tokens = preprocess_text(sentence)
print(tokens)

# Step 2: Create word co-occurrence pairs (bigram pairs)
window_size = 5  # You can adjust this size
co_occurrence_pairs = []

for i in range(len(tokens) - window_size + 1):
    window = tokens[i:i + window_size]
    co_occurrence_pairs.extend(combinations(window, 2))
    
print(co_occurrence_pairs)    

# Step 3: Count the occurrences of each pair
pair_counts = Counter(co_occurrence_pairs)
print(pair_counts)

# Step 4: Build the graph
G = nx.Graph()
# Add edges to the graph
for pair, weight in pair_counts.items():
    G.add_edge(pair[0], pair[1], weight=weight)
    
# Step 5: Visualize the network
plt.figure(figsize=(10, 8))

# Use spring layout with increased repulsion for better separation
#pos = nx.spring_layout(G, k=0.5, seed=42)  # `k` controls spacing between nodes; increase `k` for more separation
#pos = nx.circular_layout(G)
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=10)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Word Co-occurrence Network")
plt.show()    

