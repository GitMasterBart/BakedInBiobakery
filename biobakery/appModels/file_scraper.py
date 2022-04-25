import os

class FileScraper:

    def __init__(self, file_pathway):
        self.file_path = file_pathway
        self.listfiles = []
        self.listdir = []
        self.pngreadylist = []

    def find_files_in_directories(self):
        for file in os.listdir(self.file_path):
            f = os.path.join(self.file_path, file)
            # checking if it is a file
            if os.path.isfile(f):
                self.listfiles.append(f)
            elif os.path.isdir(f):
                self.listdir.append(f)

    def get_dircotrylist(self):
         return self.listdir

    def get_fileslist(self):
        return self.listfiles

    def get_pngreadyfiles(self):
        for files in self.listfiles:
            files = files.split('/')
            # print("/".join((files[6],files[7] ,files[8])))
            self.pngreadylist.append("../" + "/".join((files[6],files[7] ,files[8],files[9])))
        return self.pngreadylist

def main():
   Files =  FileScraper("/static/fastqcfiles/images")
   Files.find_files_directories()
   Files.get_fileslist()
   print(Files.get_pngreadyfiles())


if __name__ == '__main__':
    main()