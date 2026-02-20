import re
import os
import nltk

class Text:
    noise_words = {"de", "des", "les", "le", "dans", "la", "ces", "ce", "et", "une", "est", "que", "qui", "pour", "aux", "il", "l'", "d'", "\n", "cet", "aux", "ils", "vous", "nous", "en", "notre", "plus"}
    def __init__(self, file_path: str):
        self.content = ""
        try:
            with open(file_path) as f:
                self.content = f.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise FileNotFoundError

    def preprocess_text(self):
        self.content = self.content.lower()
        self.content = re.sub(r"\d+", "", self.content)
        self.content = re.sub(r"\b(" + "|".join(self.noise_words) + r")\b", "", self.content)
        self.content = re.sub(r"([,;.\"<>:?«»=]+)|[ \t]{2,}", lambda m: "" if m.group(1) else " ", self.content)
        print(self.content)

    def tokenize(self):
        self.content = nltk.word_tokenize(self.content)
        
ecolo = Text("documents/student_01.txt")
ecolo.preprocess_text()
ecolo.tokenize()

    
