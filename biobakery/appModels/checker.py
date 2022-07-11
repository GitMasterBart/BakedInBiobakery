#!/env/bin/python3
"""
This class contains all the checks that are made regards the file extension
"""

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
        :return: booleany
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


    def checks_fastq(self):
        """
        checks if a fastq extension is present in all the sample files
        :return: boolean
        """
        head_dir = FileScraper(self.input_file_without_extention)
        head_dir.find_files_in_directories()
        head_dir.remove_snakemake_file()
        inner_directorys = head_dir.get_directory_list_onlynames()
        for directory in inner_directorys:
            inner_files = FileScraper(self.input_file_without_extention + "/" + directory)
            inner_files.find_files_in_directories()
            filelist = inner_files.get_fileset()
            if ".DS_Store" in filelist:
                filelist.remove(".DS_Store")
            for file in filelist:
                if not "fastq" in file:
                    return True

    def check_if_sample_same_as_folder(self):
        """
        checks if files are there
        :return: boolean
        """
        file = FileScraper(self.input_file_without_extention)
        file.find_files_in_directories()
        file.remove_snakemake_file()
        inner_directorys = file.get_directory_list_onlynames()
        for directory in inner_directorys:
            inner_files = FileScraper(self.input_file_without_extention  + "/" + directory)
            inner_files.find_files_in_directories()
            filelist = inner_files.get_fileset()
            if ".DS_Store" in filelist:
                filelist.remove(".DS_Store")
            for file in filelist:
                if not directory in file:
                    return True

    def check_if_contains_hypend(self):
        """
        checks if hypends "-" are present in the
        file or directory names.
        :return: boolean
        """
        if "-" in self.input_file:
            return True
