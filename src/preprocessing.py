import re
import string

def preprocess_text(text):
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

def tokenize(text):
    """
    Découpe le texte en mots individuels
    
    Paramètres:
        text: str - texte nettoyé
    
    Retour:
        list - liste de mots
    """
    return text.split()


text = "L'Intelligence Artificielle (IA) est fascinante! Elle transforme notre monde."
red = tokenize(preprocess_text(text))
print(red) 

















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

    
