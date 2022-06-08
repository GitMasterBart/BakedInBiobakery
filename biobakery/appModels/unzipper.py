#!/env/bin/python3
"""
This class switches between different bio-bakery tools, it
will make sure that the right tool is used.

"""
import zipfile
import Pathways
# from biobakery.appModels.file_scraper import FileScraper
from biobakery.appModels.start_processes import ProcessesStarter
from biobakery.appModels.checker import Checker
from biobakery.appModels.file_scraper import FileScraper


class Unzipper:
    """
    this Unzipper has 2 switches. one that switch between the tools and one
    that switch between multi and single uploads
    """

    def __init__(self, tool, input_file, variables):
        self.tool = tool
        self.variables = variables
        self.input_file = input_file
        self.output_location = variables
        self.prefix = str(self.input_file).split('.')[-1]

    def control_unzip_switch(self):
        """
        unzips the uploaded zip file.
        :return: void
        """

        if Checker(self.input_file).check_zip():
            with zipfile.ZipFile(Pathways.INPUTFILESLOCATION + self.input_file, 'r') as zip_ref:
                zip_ref.extractall(Pathways.INPUTFILESLOCATION)
            self.input_file = str(self.input_file).split('.')[0]