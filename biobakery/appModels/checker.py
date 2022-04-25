#!/env/bin/python3

class Checker:

    def __init__(self, input_file):
        self.input_file = input_file
        self.prefix = str(self.input_file).split('.')[-1]

    def check_gz_zip(self):
        return True if self.prefix == "gz" or self.prefix == "zip" else False

    def check_gz(self):
        return True if self.prefix == "gz" else False

    def check_zip(self):
        return True if self.prefix == "zip" else False
