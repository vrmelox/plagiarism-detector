import numpy as np
from preprocessing import build_vocabulary
from vectorizer import compute_tfidf, normalize_vector
from utils import dot_product, norma

def tfidf_dict_to_vector(tfidf_dict: dict, vocabulary: dict) -> np.ndarray:
    """Convertit un dictionnaire TF-IDF en vecteur aligné"""
    vector = np.zeros(len(vocabulary))
    for x, value in tfidf_dict.items() :
        if x in vocabulary:
            vector[vocabulary[x]] = value
    return vector

def build_similarity_matrix(documents):
    """
    Construit une matrice N×N de similarités entre tous les documents
    
    Paramètres:
        documents: list of str - tous les documents
    
    Retour:
        numpy array - matrice N×N où [i,j] = similarité entre doc i et doc j
    
    Exemple pour 3 documents:
        [[1.00, 0.45, 0.12],
         [0.45, 1.00, 0.78],
         [0.12, 0.78, 1.00]]
        
        La diagonale = 1.00 (un doc est identique à lui-même)
        [0,1] = 0.45 signifie que doc0 et doc1 ont 45% de similarité
    """
    vocabulary = build_vocabulary(documents)
    documents_tfidf = [compute_tfidf(x, documents) for x in documents]
    list_vector = [normalize_vector(tfidf_dict_to_vector(x, vocabulary)) for x in documents_tfidf]
    matrix = np.zeros((len(documents), len(documents)))
    
    for x in range(len(list_vector)):
        for i in range(len(matrix)):
            a = list_vector[x]
            b = list_vector[i]
            matrix[x][i] = dot_product(a, b) / (norma(a) * norma(b))
    return matrix

