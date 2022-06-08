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
        self.list_files_full_path = []
        self.listdir_full_path = []
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
                self.list_files_full_path.append(objects_in_directory)
                self.list_files.append(file)
            elif os.path.isdir(objects_in_directory):
                self.listdir_full_path.append(objects_in_directory)
                self.listdir.append(file)

    def get_directory_list(self):
        """
        :return: List: self.listdir_full_path
        """
        return self.listdir_full_path

    def get_directory_list_onlynames(self):
        return self.listdir

    def get_fileset(self):
        """
        :return: list: list_files
        """
        return self.list_files

    def get_fileset_full_path(self):
        """
        :return: list: list_files
        """
        return self.list_files_full_path