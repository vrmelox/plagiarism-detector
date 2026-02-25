"""
Détecteur de plagiat basé sur TF-IDF et similarité cosinus
"""
import os
from detector import detect_plagiarism, generate_report
from utils import get_content

def load_documents(folder_path):
    """Charge tous les fichiers .txt d'un dossier"""
    return os.listdir(folder_path)

def main():
    docs_path = "documents/"
    filenames = load_documents(docs_path)
    
    print(f"{len(filenames)} documents chargés\n")
    
    documents = [get_content(docs_path + doc) for doc in filenames]
    # Détecter les plagiats
    print("🔍 Analyse en cours...")
    
    pairs = detect_plagiarism(documents, threshold=0.7)
    
    # Générer et afficher le rapport
    report = generate_report(documents, pairs)
    print(report)
    
    # Sauvegarder le rapport
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("\n✅ Rapport sauvegardé dans results.txt")

if __name__ == "__main__":
    main()