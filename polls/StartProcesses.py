#!/env/bin/python3

import os

class activateHumaNn:

    def __init__(self, filename, input_file, threads):
        self.input_file = "~/Desktop/StageWetsus2022/BakedInBiobakery/BakedInBiobakery/" + input_file
        self.output_file = "./Demodatafiles"
        self.bashscript = "~/Desktop/StageWetsus2022/BakedInBiobakery/BakedInBiobakery/media/" + filename
        self.threads = threads


    def startHumaNn(self):
        Qeary = "source " + self.bashscript + " " + self.input_file + " " + self.output_file + " " + str(self.threads)
        print(Qeary)
        os.system(Qeary)

def main():
    Newactivatie = activateHumaNn("HumanBashScript.sh", "media/DemoData.fastq.gz", 16)
    Newactivatie.startHumaNn()

if __name__ == '__main__':
    main()