class Text:
    def __init__(self, file_path: str):
        self.content = ""
        with open(file_path) as f:
            self.content = f.read()


