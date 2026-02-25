import numpy as np

def tfidf_dict_to_vector(tfidf_dict, vocabulary):
    """Convertit un dictionnaire TF-IDF en vecteur aligné"""
    vector = np.zeros(len(vocabulary))
    for x in vocabulary:
        value = tfidf_dict.get(x,0)
        vector[x] = value if value != 0 else 0.0

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
    # VOTRE CODE ICI
    # Étapes :
    # 1. Vectoriser tous les documents (TF-IDF)
    # 2. Normaliser tous les vecteurs
    # 3. Calculer cosine similarity pour chaque paire
