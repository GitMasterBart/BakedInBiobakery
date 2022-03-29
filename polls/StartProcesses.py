#!/env/bin/python3

import os
import Pathways

class activateHumaNn:

    def __init__(self, filename, input_file, threads):
        self.input_file = Pathways.virtual_envPathway + input_file
        self.output_file = Pathways.output_file_Location
        self.bashscript = Pathways.input_file_Location + filename
        self.threads = threads

    def check(self):
        print(self.input_file)

    def startHumaNn(self):
        Qeary = "source " + self.bashscript + " " + self.input_file + " " + self.output_file + " " + str(self.threads)
        print(Qeary)
        os.system(Qeary)

def main():
    Newactivatie = activateHumaNn("HumanBashScript.sh", "media/DemoData.fastq.gz", 16)
    # Newactivatie.startHumaNn()
    Newactivatie.check()
if __name__ == '__main__':
    main()