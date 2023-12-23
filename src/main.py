import os

class File:
    def __init__(self, dir, old, new):
        self.dir = dir
        self.old = old
        self.new = new
        self.files = []
        self.set_files_path()
        self.set_new_name()
        self.reset_files()

    def set_files_path(self):
        for file in os.listdir(self.dir):
            self.files.append(self.dir + f'\{file}')

    def set_new_name(self):
        for file in self.files:
            if self.old in file:
                renamed_file = file.replace(self.old, self.new)
                yield renamed_file

    def reset_files(self):
        self.files.clear()
        self.newfiles = self.set_new_name()

    def rename_files(self):
        for file in self.files:
            os.rename(file, self.newfiles)