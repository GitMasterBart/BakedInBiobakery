#!/env/bin/python3

import os
import Pathways

class ActivateProcesses:

    def __init__(self, filename, input_file, threads):
        self.input_file = Pathways.virtual_envPathway + input_file
        self.output_file = Pathways.output_file_Location
        self.output_file_fastqc = self.input_file.split('.')[0] + "_fastqc.zip"
        self.bashscript = Pathways.input_file_Location_sh + filename
        self.threads = threads

    def check(self):
        print(self.input_file)


    def startHumaNn(self):
        Query = "source " + self.bashscript + " " + self.input_file + " " + self.output_file + " " + str(self.threads)
        print(Query)
        os.system(Query)


    def startFastqc(self):
        Query = "source " + self.bashscript + " " + self.input_file + " "  + self.output_file_fastqc
        print(Query)
        os.system(Query)


def main():
    Newactivatie = ActivateProcesses("fastqcStarter.sh", "media/temp/DemoData.fastq.gz",  "media/DemoData_fastqc.zip")
    Newactivatie.startFastqc()
    Newactivatie.check()
if __name__ == '__main__':
    main()