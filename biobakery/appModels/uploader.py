#!/env/bin/python3

"""
Upload a file to a directory of choice
"""
import Pathways
from biobakery.appModels.checker import Checker

class Uploader:
    """
    Upload a file to a directory of choice:
    can be used as: Uploader([Direcotry]).handle_uploaded_file
    """
    def __init__(self, file):
        self.file = file

    def check_file(self):
        """
        This is a extra check uses the checker.py, it is only here because
        it is easier for usage in views.py.
        :return:
        """
        return Checker(self.file).check_zip()

    def handle_uploaded_file(self):
        """
        handles upload, and writes it to the directory of choice
        :return: void
        """
        with open(Pathways.LOCATIONUPLOADEDFILES + str(self.file), 'wb+') as destination:
            for chunk in self.file.chunks():
                destination.write(chunk)
