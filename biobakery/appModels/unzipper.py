#!/env/bin/python3
"""
This class switches between different bio-bakery tools, it
will make sure that the right tool is used.

"""
import zipfile
import Pathways
import gzip
# from biobakery.appModels.file_scraper import FileScraper
from biobakery.appModels.start_processes import ProcessesStarter
from biobakery.appModels.checker import Checker
from biobakery.appModels.file_scraper import FileScraper


class Unzipper:
    """
    this Unzipper has 2 switches. one that switch between the tools and one
    that switch between multi and single uploads
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.prefix = str(self.input_file).split('.')[-1]

    def control_unzip_switch(self):
        """
        unzips the uploaded zip file.
        :return: void
        """

        if Checker(self.input_file).check_zip():
            print(self.input_file)
            with zipfile.ZipFile(Pathways.INPUTFILESLOCATION + self.input_file, 'r') as zip_ref:
                print("unzipping")
                zip_ref.extractall(Pathways.INPUTFILESLOCATION)
                print(Pathways.INPUTFILESLOCATION + self.input_file)
            self.input_file = str(self.input_file).split('.')[0]

    def contorl_gzip_switch(self):
        """
                unzips the uploaded gz files.
                :return: void
        """

        parentmap = FileScraper(Pathways.INPUTFILESLOCATION + str(self.input_file).split(".")[0])
        parentmap.find_files_in_directories()
        parentmap.remove_snakemake_file()
        for sample_direcotrys in parentmap.get_directory_list():
            files = FileScraper(sample_direcotrys)
            files.find_files_in_directories()
            files.remove_snakemake_file()
            checked_files = list(filter(lambda i: Checker(i).check_gz(), files.get_fileset_full_path()))
            if not checked_files == []:
                for file in checked_files:
                    fp = open(file.split(".")[0] + ".fastq", "wb")
                    with gzip.open(file, "rb") as f:
                        bindata = f.read()
                        fp.write(bindata)
                        fp.close()


# Unzipper("Fullsamples_dummy.zip").control_unzip_switch()
#
# with zipfile.ZipFile( "/Users/bengels/Desktop/Uploaded_files/Fullsamples_dummy_3.zip", 'r') as zip_ref:
#
#     zip_ref.extractall("/Users/bengels/Desktop/Uploaded_files/")