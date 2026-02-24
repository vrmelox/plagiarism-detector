import numpy as np
from collections import Counter
from preprocessing import tokenize, build_vocabulary
from math import log

def text_to_vector(text, vocabulary) -> np.ndarray:
    """
    Convertit un texte en vecteur de fréquences
    
    Paramètres:
        text: str - texte à vectoriser
        vocabulary: dict - vocabulaire {mot: index}
    
    Retour:
        numpy array - vecteur de fréquences (longueur = taille du vocabulaire)
    
    Exemple:
        text = "le chat mange"
        vocab = {"le": 0, "chat": 1, "chien": 2, "mange": 3}
        result = [1, 1, 0, 1]  # le=1, chat=1, chien=0, mange=1
    """
    token = tokenize(text)
    token_counts = Counter(token)
    vector = np.zeros(len(vocabulary))
    for token, count in token_counts.items():
        if token in vocabulary:
            vector[vocabulary[token]] = count
    return vector

def compute_tf(text) -> dict:
    """
    Calcule la fréquence relative de chaque mot dans le document
    
    TF(mot) = (nombre d'occurrences du mot) / (nombre total de mots)
    
    Paramètres:
        text: str - texte du document
    
    Retour:
        dict - {mot: tf_score}
    
    Exemple:
        text = "le chat mange le poisson"
        # "le" apparaît 2 fois sur 5 mots total
        result = {"le": 0.4, "chat": 0.2, "mange": 0.2, "poisson": 0.2}
    """
    tokens = tokenize(text)
    token_counters = Counter(tokens)
    text_tf = {}
    for word, count in token_counters.items():
        text_tf.update({word: count/len(tokens)})
    return text_tf


def compute_idf(documents: list[str]) -> dict:
    """
    Calcule l'IDF pour chaque mot du corpus
    
    IDF(mot) = log(nombre_total_documents / nombre_documents_contenant_le_mot)
    
    Paramètres:
        documents: list of str - tous les documents
    
    Retour:
        dict - {mot: idf_score}
    
    Exemple:
        docs = [
            "le chat mange",
            "le chien dort",
            "le chat dort"
        ]
        # "le" apparaît dans 3/3 docs: IDF = log(3/3) = 0
        # "chat" apparaît dans 2/3 docs: IDF = log(3/2) ≈ 0.176
        # "mange" apparaît dans 1/3 docs: IDF = log(3/1) ≈ 0.477
    """
    text_idf = {}
    vocabulary = build_vocabulary(documents)
    for x in vocabulary:
        for k in documents:
            if x in k: 
                text_idf[x] += 1
        text_idf[x] = log(len(documents)/text_idf[x])
    return text_idf

def compute_tfidf(document, all_documents):
    """
    Calcule le vecteur TF-IDF pour un document
    
    TF-IDF(mot) = TF(mot) × IDF(mot)
    
    Paramètres:
        document: str - le document à vectoriser
        all_documents: list of str - tous les documents (pour calculer IDF)
    
    Retour:
        dict - {mot: tfidf_score}
    """
    text_tfidf = {}
    text_tf = compute_tf(document)
    texts_idf = compute_idf(all_documents)
    for x in text_tf:
        text_tfidf[x] = text_tf[x] * texts_idf[x]
    return text_tfidf
    
