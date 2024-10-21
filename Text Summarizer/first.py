import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords 
from nltk.cluster.util import cosine_distance 
import numpy as np  # Import NumPy for numerical operations
import networkx as nx  # Import NetworkX for graph operations

def read_article(file_name):
    file = open(file_name, "r")  # Open the specified text file
    filedata = file.readlines()  # Read all lines from the file
    article = filedata[0].split(".")  # Split the text into sentences based on periods
    sentences = []  # Initialize a list to hold processed sentences
    for sentence in article:  # Iterate through each sentence
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))  # Clean and split into words
    sentences.pop()  # Remove last empty sentence if present
    return sentences  # Return the list of sentences

def sentence_similarity(sen1, sen2, stopwords=None):
    if stopwords is None:  # If no stopwords provided
        stopwords = []  # Initialize as an empty list
    sen1 = [w.lower() for w in sen1]  # Convert first sentence to lowercase
    sen2 = [w.lower() for w in sen2]  # Convert second sentence to lowercase
    all_words = list(set(sen1 + sen2))  # Get unique words from both sentences
    vector1 = [0] * len(all_words)  # Initialize vector for first sentence
    vector2 = [0] * len(all_words)  # Initialize vector for second sentence
    for w in sen1:  # Iterate through words in the first sentence
        if w in stopwords:  # If the word is a stopword
            continue  # Skip it
        vector1[all_words.index(w)] += 1  # Increment the count in the vector
    for w in sen2:  # Iterate through words in the second sentence
        if w in stopwords:  # If the word is a stopword
            continue  # Skip it
        vector2[all_words.index(w)] += 1  # Increment the count in the vector
    return 1 - cosine_distance(vector1, vector2)  # Return the cosine similarity score

def gen_sim_matrix(sentences, stopwords):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))  # Create a square matrix of zeros
    for idx1 in range(len(sentences)):  # Iterate over sentences by index
        for idx2 in range(len(sentences)):  # Compare each sentence with every other sentence
            if idx1 == idx2:  # If comparing the same sentence
                continue  # Skip it
            # Calculate and store similarity score in the matrix
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stopwords)
    return similarity_matrix  # Return the similarity matrix

def generate_summary(file_name, top_n=5):
    stop_words = set(stopwords.words('english'))  # Get English stopwords
    summarize_text = []  # Initialize list for summary sentences

    # Read the article and generate sentence similarity matrix
    sentences = read_article(file_name)  # Read sentences from the file
    sentence_similarity_matrix = gen_sim_matrix(sentences, stop_words)  # Generate similarity matrix

    # Use the similarity matrix to build a graph and apply PageRank
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)  # Create a graph from the matrix
    scores = nx.pagerank(sentence_similarity_graph)  # Apply PageRank to get scores for each sentence

    # Rank the sentences based on their scores
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)  # Sort sentences by score

    # If there are fewer sentences than the top_n requested, adjust the limit
    top_n = min(top_n, len(ranked_sentence))  # Ensure top_n does not exceed available sentences

    for i in range(top_n):  # Iterate for the top_n sentences
        summarize_text.append(" ".join(ranked_sentence[i][1]))  # Join words of the ranked sentence

    print("Summary:\n", ". ".join(summarize_text))  # Print the final summary

# Call the function to generate a summary for the specified file
generate_summary("msft.txt", 5)  # Generate a summary of the file with a maximum of 2 sentences




# import nltk
# # nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.cluster.util import cosine_distance
# import numpy as np
# import networkx as nx # Import NetworkX for graph operations

# def read_article(file_name):
#     file = open(file_name, "r")
#     filedata = file.readlines()
#     article = filedata[0].split(".")
#     sentences = []
#     for sentence in article:
#         sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))  
#     sentences.pop()  # remove last empty sentence
#     return sentences


# def sentence_similarity(sen1,sen2,stopwords=None):
#     if stopwords is None:
#         stopwords=[]
#     sen1=[w.lower() for w in sen1]
#     sen2=[w.lower() for w in sen2]
#     all_words=list(set(sen1+sen2))
#     vector1=[0]*len(all_words)
#     vector2=[0]*len(all_words)
#     for w in sen1:
#         if w in stopwords:
#             continue
#         vector1[all_words.index(w)]+=1
#     for w in sen2:
#         if w in stopwords:
#             continue
#         vector2[all_words.index(w)]+=1
#     return 1-cosine_distance(vector1,vector2)

# def gen_sim_matrix(sentences,stopwords):
#     similarity_matrix=np.zeros((len(sentences),len(sentences)))
#     for idx1 in range(len(sentences)):
#         for idx2 in range(len(sentences)):
#             if idx1==idx2:
#                 continue
#             similarity_matrix[idx1][idx2]=sentence_similarity(sentences[idx1],sentences[idx2],stopwords)
#     return similarity_matrix

# def generate_summary(file_name, top_n=5):
#     stop_words = set(stopwords.words('english'))
#     summarize_text = []

#     # Read the article and generate sentence similarity matrix
#     sentences = read_article(file_name)
#     sentence_similarity_matrix = gen_sim_matrix(sentences, stop_words)

#     # Use the similarity matrix to build a graph and apply PageRank
#     sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
#     scores = nx.pagerank(sentence_similarity_graph)

#     # Rank the sentences based on their scores
#     ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

#     # If there are fewer sentences than the top_n requested, adjust the limit
#     top_n = min(top_n, len(ranked_sentence))

#     for i in range(top_n):
#         summarize_text.append(" ".join(ranked_sentence[i][1]))

#     print("Summary:\n", ". ".join(summarize_text))


# generate_summary("msft.txt",2)