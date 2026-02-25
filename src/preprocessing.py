import re
import string

def preprocess_text(text: str) -> str:
    """
    Nettoie et prépare le texte pour la vectorisation
    
    Étapes :
    1. Convertir en minuscules
    2. Supprimer la ponctuation
    3. Supprimer les chiffres (optionnel)
    4. Supprimer les espaces multiples
    
    Paramètres:
        text: str - texte brut
    
    Retour:
        str - texte nettoyé
    """
    text_clean = text.lower()
    text_clean = re.sub(r"([,;.\"()!<>:?«»=]+)|'|[ \t]{2,}", lambda m : "" if m.group(1) else " " , text_clean)
    text_clean = re.sub(r"\d+", "", text_clean)
    return text_clean

def tokenize(text: str) -> list:
    """
    Découpe le texte en mots individuels
    
    Paramètres:
        text: str - texte nettoyé
    
    Retour:
        list - liste de mots
    """
    return text.split()

def build_vocabulary(documents: list[str]) -> dict:
    """
    Construit le vocabulaire complet à partir de tous les documents
    
    Paramètres:
        documents: list of str - liste de textes
    
    Retour:
        dict - {mot: index} pour chaque mot unique
    
    Exemple:
        docs = ["le chat mange", "le chien mange"]
        vocab = {"le": 0, "chat": 1, "chien": 2, "mange": 3}
    """
    documents_cleaned = [tokenize(preprocess_text(doc)) for doc in documents]
    
    uniques = set()
    vocabulary = {}
    for value in documents_cleaned:
        for x in value:
            uniques.add(x)
    for value, index in enumerate(uniques):
        vocabulary.update({value: index})
    return vocabulary


# text = "L'Intelligence Artificielle (IA) est fascinante! Elle transforme notre monde."
# onetext = """L'intelligence artificielle transforme notre société de manière profonde. Les algorithmes 
# """
# twotext = """Les algorithmes d'apprentissage automatique permettent désormais de résoudre des problèmes complexes dans 
# des domaines variés. La médecine bénéficie de diagnostics plus précis grâce aux réseaux 
# de neurones. Les véhicules autonomes promettent de révolutionner le transport. Cependant, 
# ces avancées soulèvent des questions éthiques importantes concernant la vie privée et 
# l'emploi. Il est                 crucial de développer ces technologies de façon responsable."""
# docs = [text, onetext, twotext]
# red = tokenize(preprocess_text(text))
# print(build_vocabulary(docs)) 

















# import re
# import os
# import nltk

# class Text:
#     noise_words = {"de", "des", "les", "le", "dans", "la", "ces", "ce", "et", "une", "est", "que", "qui", "pour", "aux", "il", "l'", "d'", "\n", "cet", "aux", "ils", "vous", "nous", "en", "notre", "plus"}
#     def __init__(self, file_path: str):
#         self.content = ""
#         self.vocabulary = {}
#         try:
#             with open(file_path) as f:
#                 self.content = f.read()
#         except FileNotFoundError:
#             print(f"File not found: {file_path}")
#             raise FileNotFoundError

#     def preprocess_text(self):
#         self.content = self.content.lower()
#         self.content = re.sub(r"\d+", "", self.content)
#         self.content = re.sub(r"\b(" + "|".join(self.noise_words) + r")\b", "", self.content)
#         self.content = re.sub(r"([,;.\"<>:?«»=]+)|[ \t]{2,}", lambda m: "" if m.group(1) else " ", self.content)
#         print(self.content)

#     def tokenize(self):
#         self.content = nltk.word_tokenize(self.content)

#     def build_vocabulary(self):

#         self.vocabulary = {x : i for x, i in enumerate(self.content)}
        
# ecolo = Text("documents/student_01.txt")
# ecolo.preprocess_text()
# ecolo.tokenize()

    
