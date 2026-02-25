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
    indices = np.where(similars > threshold)
    similarities = [
        (i, j, similars[i, j])
        for i, j, in zip(indices[0], indices[1])
    ]
    similarities.sort(key=lambda x: x[2], reverse=True)
    return similarities

def generate_report(filenames, plagiarism_pairs):
    """
    Génère un rapport lisible des plagiats détectés
    
    Paramètres:
        filenames: list of str - noms des fichiers
        plagiarism_pairs: list of tuples - résultat de detect_plagiarism()
    
    Retour:
        str - rapport formaté
    """
    matrix = detect_plagiarism(filenames)
    report = ""
    for i, j, similarity in matrix:
        report += f"⚠️  PLAGIAT DÉTECTÉ ⚠️\n\n"
        report += f"Paire {i}: {filenames[i]} ↔ {filenames[j]}\n"
        report += f"Similarité: {similarity*100}%\n"
        report += f"Niveau: {'Plagiat quasi-certain (copie massive)' if similarity > 0.9 else 'Plagiat probable (investigation nécessaire)' if similarity > 0.7 else 'Similarité suspecte (vérification manuelle)' if similarity > 0.5 else 'Probablement distinct'}\n\n"
    return report