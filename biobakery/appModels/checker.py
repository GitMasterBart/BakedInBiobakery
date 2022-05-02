#!/env/bin/python3
"""
This class contains all the checks that are made regards the file prefixes
"""
class Checker:

    """
    This class hase 3 methods that check the prefix of a file.
    They return a boolean.
    """

    def __init__(self, input_file):
        self.input_file = input_file
        self.prefix = str(self.input_file).split('.')[-1]

    def check_gz_zip(self):
        """
        check if prefix equals gz of zip
        :return: boolean
        """
        return bool(self.prefix in ("gz", "zip"))

    def check_gz(self):
        """
        checks if prefix equals gz
        :return: boolean
        """
        return bool(self.prefix == "gz")

    def check_zip(self):
        """
        checks if prefix equals zip
        :return: boolean
        """
        return bool(self.prefix == "zip")
