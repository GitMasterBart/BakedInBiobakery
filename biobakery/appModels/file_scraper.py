#!/env/bin/python3

"""
This class is used for scraping files form the filepath that is given.
a list is created this can be done for a list of directory's and files
it hase a get method for both of these options.
"""

import os

class FileScraper:
    """
    This class is used for scraping files form the filepath that is given.
    It has 2 options and a required method to function.
    required:
    find_files_in_directories: searches for files or directory in the given directory.
    optional:
    get_directory_list: returns a list with directory names
    get_fileset: returns a list with filenames
    """

    def __init__(self, file_pathway):
        self.file_path = file_pathway
        self.list_files = []
        self.listdir = []
        self.pngreadylist = []

    def find_files_in_directories(self):
        """
        Scrapes the directory that is given as variable file_pathway
        :return: void
        """
        for file in os.listdir(self.file_path):
            objects_in_directory = os.path.join(self.file_path, file)
            # checking if it is a file
            if os.path.isfile(objects_in_directory):
                self.list_files.append(objects_in_directory)
            elif os.path.isdir(objects_in_directory):
                self.listdir.append(objects_in_directory)

    def get_directory_list(self):
        """
        :return: List: self.listdir
        """
        return self.listdir

    def get_fileset(self):
        """
        :return: list: list_files
        """
        return self.list_files

    def get_pngreadyfiles(self):
        """
        Really specific and not used in the software atm. maybe later
        :return: list: pngreadylist
        """
        for files in self.list_files:
            files = files.split('/')
            self.pngreadylist.append("../" + "/".join((files[6],files[7] ,files[8],files[9])))
        return self.pngreadylist


def main():
    """
    main function pylint vault. Will be deleted when unnecessary
    :return:
    """
    search_directory =  FileScraper("/static/fastqcfiles/images")
    search_directory.find_files_in_directories()
    search_directory.get_fileset()
    print(search_directory.get_pngreadyfiles())


if __name__ == '__main__':
    main()
