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

    def __init__(self, tool, input_files, research_name, user_id, research_id, variables, possibilities):
        self.tool = tool
        self.input_files = input_files
        self.variables = variables
        self.possibilities = possibilities
        self.research_name = research_name
        self.user_id = user_id
        self.research_id = research_id
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
        bashscript = Pathways.LOCATIONBASHSCRIPTCOMPLEETPIPELINE
        new_list_filse = FileScraper(Pathways.LOCATIONUPLOADEDFILES + str(self.input_files))
        new_list_filse.find_files_in_directories()

        dataset = new_list_filse.get_directory_list_onlynames()

        if ".snakemake" in dataset:
            dataset.remove(".snakemake")


        for keys in self.variables:
            # print(possibilties_dict.get(keys))
            string_ready_for_use += " " +  str(possibilties_dict.get(keys)) + "=" + str(keys)
        count = 0
        list_without_space = "["
        for item in dataset:
            count += 1
            if len(dataset) == count:
                list_without_space += '"' + item + '"'
            else:
                list_without_space += '"' + item + '"' + ','
        list_without_space += "]"

        if self.tool == "kneaddata":
            bashscript = Pathways.LOCATIONBASHSCRIPTKNEADDATA
        elif self.tool == "human":
            bashscript = Pathways.LOCATIONBASHSCRIPTHUMAN
        print(list_without_space)
        query = "source " + bashscript + " " + Pathways.INPUTFILESLOCATION + str(self.input_files) + ' ' + str(self.research_name) + ' ' + str(self.user_id) + ' ' + str(self.research_id) + ' ' + list_without_space + " " + string_ready_for_use
        # print(query)
        return os.system(query)
