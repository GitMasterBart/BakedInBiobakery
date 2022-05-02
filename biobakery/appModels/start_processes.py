#!/env/bin/python3

"""
This process start of different processes and starts them. It has methods that describe
what happens when called
"""
import os
import Pathways
# from biobakery.appModels.file_scraper import FileScraper
# from biobakery.appModels.checker import Checker


class ProcessesStarter:
    """
    This class handels the start of different biobakery tools.
    Each tool hase its own methode with a single and
    a multi option. This makes it possible to upload one file or multiple files.
    """

    def __init__(self, input_files, output_location):
        self.input_files = input_files
        self.output_file = output_location
        self.prefix = str(self.input_files).split('.')[-1]
        # self.output_file_fastqc = Pathways.virtual_envPathwayfastqc +
        # self.input_file.split('.')[0] + "_fastqc.zip"
        # self.threads = threads

    def start_humann_single(self):
        """
        Starts The humann tool single, this means that it wil start a
        bash script that handels only one file.
        :return: void
        """
        query = "source " + Pathways.BashScriptHuman + " " + \
                Pathways.input_file_Location + str(self.input_files) + " " + \
                Pathways.output_file_Location + " " + "fastq.gz" + " " + Pathways.UniprotDatabase
        print(query)
        os.system(query)

    def start_humann_multi(self):
        """
        Starts the HumaNn3.0 tool multi, this means that it wil start a bahs
        file that handles multiple unziped files.
        :return: void
        """
        query = "source " + Pathways.BashScriptHumanMulti + " " + \
                Pathways.input_file_Location + str(self.input_files) + " " + \
                Pathways.output_file_Location + " " + "fastq" + " " + Pathways.UniprotDatabase
        print(query)
        os.system(query)


def main():
    """
    test startswitches
    :return: void
    """
    newactivatie = ProcessesStarter("demofiles_wetsus4000/demofile_wetsus4000R1.fastq",
                                  "~/Desktop/output_data")
    newactivatie.start_humann_single()


if __name__ == '__main__':
    main()
