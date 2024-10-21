import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

def read_article(file_name):
    file = open(file_name, "r")
    filedata = file.readlines()
    article = filedata[0].split(".")
    sentences = []
    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))  
    sentences.pop()  # remove last empty sentence
    return sentences


def sentence_similarity(sen1,sen2,stopwords=None):
    if stopwords is None:
        stopwords=[]
    sen1=[w.lower() for w in sen1]
    sen2=[w.lower() for w in sen2]
    all_words=list(set(sen1+sen2))
    vector1=[0]*len(all_words)
    vector2=[0]*len(all_words)
    for w in sen1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)]+=1
    for w in sen2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)]+=1
    return 1-cosine_distance(vector1,vector2)

def gen_sim_matrix(sentences,stopwords):
    similarity_matrix=np.zeros((len(sentences),len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1==idx2:
                continue
            similarity_matrix[idx1][idx2]=sentence_similarity(sentences[idx1],sentences[idx2],stopwords)
    return similarity_matrix

def generate_summary(file_name, top_n=5):
    stop_words = set(stopwords.words('english'))
    summarize_text = []

    # Read the article and generate sentence similarity matrix
    sentences = read_article(file_name)
    sentence_similarity_matrix = gen_sim_matrix(sentences, stop_words)

    # Use the similarity matrix to build a graph and apply PageRank
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Rank the sentences based on their scores
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    # If there are fewer sentences than the top_n requested, adjust the limit
    top_n = min(top_n, len(ranked_sentence))

    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))

    print("Summary:\n", ". ".join(summarize_text))


generate_summary("msft.txt",2)