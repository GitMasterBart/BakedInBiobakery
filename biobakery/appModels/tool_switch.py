#!/env/bin/python3
import zipfile

import Pathways
from biobakery.appModels.file_scraper import FileScraper
from biobakery.appModels.start_processes import StartProcesses
from biobakery.appModels.checker import Checker

class Switcher:

    def __init__(self, tool, input_file, output_location):
        self.tool = tool
        self.input_file = input_file
        self.output_location = output_location
        self.prefix = str(self.input_file).split('.')[-1]

    def control_unzip_switch(self):
        if Checker(self.input_file).check_zip():
            with zipfile.ZipFile(Pathways.input_file_Location + self.input_file, 'r') as zip_ref:
                zip_ref.extractall(Pathways.input_file_Location)
            self.input_file = str(self.input_file).split('.')[0]

    def tool_switch(self):
        if self.tool == "human" and Checker(self.input_file).check_gz():
            print(self.input_file)
            StartProcesses(self.input_file, self.output_location).start_humann_single()
        elif self.tool == "human":
            print("hierbenik")
            print(self.input_file)
            StartProcesses(self.input_file, self.output_location).start_humann_multi()

