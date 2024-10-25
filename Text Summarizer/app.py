from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import nltk

# Download stopwords
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)  # Enable CORS

# Function to read and split the article text
def read_article(text):
    article = text.split(".")
    sentences = []
    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()  # Remove last empty sentence if present
    return sentences

# Function to compute sentence similarity
def sentence_similarity(sen1, sen2, stopwords=None):
    if stopwords is None:
        stopwords = []
    sen1 = [w.lower() for w in sen1]
    sen2 = [w.lower() for w in sen2]
    all_words = list(set(sen1 + sen2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    
    for w in sen1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
    
    for w in sen2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
    
    return 1 - cosine_distance(vector1, vector2)

# Generate similarity matrix
def gen_sim_matrix(sentences, stopwords):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stopwords)
    
    return similarity_matrix

# Summarize the text using PageRank
def summarize_text(text, top_n=5):
    stop_words = set(stopwords.words('english'))
    sentences = read_article(text)
    sentence_similarity_matrix = gen_sim_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    
    top_n = min(top_n, len(ranked_sentence))
    summary = []
    
    for i in range(top_n):
        summary.append(" ".join(ranked_sentence[i][1]))
    
    return ". ".join(summary)

# Route to serve the frontend HTML
@app.route("/")
def index():
    return render_template("index.html")

# Route for text summarization
@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data['text']
    try:
        summary = summarize_text(text, top_n=5)
        return jsonify({"summary": summary})
    except Exception as e:
        print("Error in summarization:", e)  # Print the error details in console
        return jsonify({"error": "An error occurred while summarizing the text."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
