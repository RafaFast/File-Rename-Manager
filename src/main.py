import os
from pathlib import Path

class File:
    def __init__(self, dir, sentence, replaced):
        self.dir = Path(dir)
        self.sentence = sentence
        self.replaced = replaced
        self.files = []
        self.set_files_path()
        self.renamed_files = [file.replace(self.sentence, self.replaced) for file in self.files]
        self.rename_files()

    def set_files_path(self):
        for file in os.listdir(self.dir):
            self.files.append(os.path.join(self.dir, file))

    def rename_files(self):
        for old, new in zip(self.files, self.renamed_files):
            os.rename(old, new)

def main():
    path = input('Path: ')
    sentence = input('Sentence to change: ')
    rename = input('Rename to: ')
    pasta = File(path, sentence, rename)
    print(os.listdir(pasta.dir))

main()