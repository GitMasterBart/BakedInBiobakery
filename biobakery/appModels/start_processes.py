#!/env/bin/python3

import os
import Pathways
from biobakery.appModels.file_scraper import FileScraper
from biobakery.appModels.checker import Checker

class StartProcesses:

    def __init__(self, input_files, output_location):
        self.input_files = input_files
        self.output_file = output_location
        self.prefix = str(self.input_files).split('.')[-1]
        # self.output_file_fastqc = Pathways.virtual_envPathwayfastqc + self.input_file.split('.')[0] + "_fastqc.zip"

        # self.threads = threads

    def start_humann_single(self):
        Query = "source " + Pathways.BashScriptHuman + " " + Pathways.input_file_Location + str(self.input_files) + " " + \
                Pathways.output_file_Location + " " + "fastq.gz" + " " + Pathways.UniprotDatabase
        print(Query)
        os.system(Query)

    def start_humann_multi(self):
        Query = "source " + Pathways.BashScriptHumanMulti + " " + Pathways.input_file_Location + str(self.input_files) + " " + \
                Pathways.output_file_Location + " " + "fastq" + " " + Pathways.UniprotDatabase
        print(Query)
        os.system(Query)


def main():
    Newactivatie = StartProcesses("demofile_wetsusR1.fastq.gz", "~/Desktop/output_data")
    Newactivatie.start_humann_single()

if __name__ == '__main__':
    main()