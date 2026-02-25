from similarity import build_similarity_matrix
import numpy as np

def detect_plagiarism(documents, threshold=0.7):
    """
    Identifie les paires de documents suspects (similarité > seuil)
    
    Paramètres:
        documents: list of str - tous les documents
        threshold: float - seuil de détection (défaut 0.7 = 70%)
    
    Retour:
        list of tuples - [(doc_i, doc_j, similarity_score), ...]
        Trié par similarité décroissante
    
    Exemple:
        [
            (0, 3, 0.94),  # Doc 0 et 3 sont 94% similaires
            (1, 5, 0.82),  # Doc 1 et 5 sont 82% similaires
            (2, 7, 0.71)   # Doc 2 et 7 sont 71% similaires
        ]
    """
    similars = build_similarity_matrix(documents)
    similars = np.triu(similars, k=1)
    similarities = []
    for x in similars:
        for y in x:
            if y > threshold:
                similarities.append((similars.index(x), similars.index(y), y))
    similarities.sort(key=lambda x: x[2], reverse=True)
    return similarities