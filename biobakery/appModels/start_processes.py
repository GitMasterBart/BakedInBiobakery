#!/env/bin/python3

"""
This process start of different processes and starts them. It has methods that describe
what happens when called
"""
import os
import Pathways
from biobakery.appModels.file_scraper import FileScraper

# from biobakery.appModels.file_scraper import FileScraper
# from biobakery.appModels.checker import Checker


class ProcessesStarter:
    """
    This class handels the start of different biobakery tools.
    Each tool hase its own methode with a single and
    a multi option. This makes it possible to upload one file or multiple files.
    """

    def __init__(self, input_files, variables, possibilities):
        self.input_files = input_files
        self.variables = variables
        self.possibilities = possibilities
        # self.output_file = output_location
        self.prefix = str(self.input_files).split('.')[-1]
        # self.output_file_fastqc = Pathways.virtual_envPathwayfastqc +
        # self.input_file.split('.')[0] + "_fastqc.zip"
        # self.threads = threads


    def start_humann_multi(self):
        """
        Starts the HumaNn3.0 tool multi, this means that it wil start a bahs
        file that handles multiple unziped files.
        :return: void
        """
        # print(self.variables)
        # print(type(str(' '.join(self.variables))))
        possibilties_dict = dict(self.possibilities)
        # print(possibilties_dict)

        string_ready_for_use = ""
        count = 0
        print(Pathways.uploaded_filepath)
        new_list_filse = FileScraper(Pathways.uploaded_filepath + str(self.input_files))
        new_list_filse.find_files_in_directories()

        dataset = new_list_filse.get_directory_list_onlynames()

        for keys in self.variables:
            count += 1

            # print(possibilties_dict.get(keys))
            string_ready_for_use += " " +  str(possibilties_dict.get(keys)) + "=" + str(keys)
        print(count)

        query = "source " + Pathways.BashScriptHumanMulti + " " + \
                Pathways.input_file_Location + str(self.input_files) + ' ' + str(dataset) + " " + string_ready_for_use
        # print(query)
        os.system(query)



def main():
    """
    test startswitches
    :return: void
    """
    newactivatie = ProcessesStarter("poging2_v1", ['--remove-temp-output', '--verbose',
                                                   '~/Desktop/Uploaded_files/humann_dbs/unireffull/', '--bypass-nucleotide-search'],
                                    [('--bypass-nucleotide-search', 'bypass_n_search'),
                                     ('--remove-temp-output', 'remove_temp_output'), ('--verbose', 'verbose'), (
                                     '~/Desktop/Uploaded_files/humann_dbs/unireffull/',
                                     'protein_db'), (
                                     '/Users/bengels/Desktop/Uploaded_files/humann_dbs/chocophlan',
                                     'nucleotide_db')]
                                    )
    newactivatie.start_humann_multi()


if __name__ == '__main__':
    main()

