import numpy as np
from collections import Counter
from preprocessing import tokenize

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
