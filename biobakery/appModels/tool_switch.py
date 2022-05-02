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

class Switcher:
    """
    this Switcher has 2 switches. one that switch between the tools and one
    that switch between multi and single uploads
    """

    def __init__(self, tool, input_file, output_location):
        self.tool = tool
        self.input_file = input_file
        self.output_location = output_location
        self.prefix = str(self.input_file).split('.')[-1]

    def control_unzip_switch(self):
        """
        unzips the uploaded zip file.
        :return: void
        """
        if Checker(self.input_file).check_zip():
            with zipfile.ZipFile(Pathways.input_file_Location + self.input_file, 'r') as zip_ref:
                zip_ref.extractall(Pathways.input_file_Location)
            self.input_file = str(self.input_file).split('.')[0]

    def tool_switch(self):
        """
        Switches between the tools and start the right process (single, multi)
        :starts: process
        """
        if self.tool == "human" and Checker(self.input_file).check_gz():
            ProcessesStarter(self.input_file, self.output_location).start_humann_single()
        elif self.tool == "human":
            ProcessesStarter(self.input_file, self.output_location).start_humann_multi()

