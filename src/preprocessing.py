import re
import os

class Text:
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
        self.content = re.sub(r"\bde\b|\bdes\b|\bles\b|\ble\b|\bdans\b|\bla\b|\bces\b|\bce\b {2,}", "", self.content)
        self.content = re.sub(r"(\d|l'|d'|\n|[,;.\"<>:?«»=]+)|[ \t]{2,}", lambda m: "" if m.group(1) else " ", self.content)
        print(self.content)


ecolo = Text("documents/student_01.txt")
ecolo.preprocess_text()

    
