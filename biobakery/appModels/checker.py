#!/env/bin/python3
"""
This class contains all the checks that are made regards the file prefixes
"""
import Pathways
from biobakery.appModels.file_scraper import FileScraper

class Checker:

    """
    This class hase 3 methods that check the prefix of a file.
    They return a boolean.
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.input_file_without_extention = str(self.input_file).split(".")[0]
        self.extention = str(self.input_file).split('.')[-1]

    def check_gz_zip(self):
        """
        check if prefix equals gz of zip
        :return: boolean
        """
        return bool(self.extention in ("gz", "zip"))

    def check_gz(self):
        """
        checks if prefix equals gz
        :return: boolean
        """
        return bool(self.extention == "gz")

    def check_zip(self):
        """
        checks if prefix equals zip
        :return: boolean
        """
        return bool(self.extention == "zip")

    def check_if_exist(self):
        # print(self.input_file_without_extention)
        file = FileScraper(self.input_file_without_extention)
        file.find_files_in_directories()
        inner_directorys = file.get_directory_list_onlynames()
        if ".snakemake" in inner_directorys:
            inner_directorys.remove(".snakemake")
        print(inner_directorys)
        for dir in inner_directorys:
            inner_files = FileScraper(self.input_file_without_extention  + "/" + dir)
            inner_files.find_files_in_directories()
            filelist = inner_files.get_fileset()
            if ".DS_Store" in filelist:
                filelist.remove(".DS_Store")
            for file in filelist:
                if not dir in file:
                    return True




