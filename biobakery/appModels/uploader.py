#!/env/bin/python3

"""
Upload a file to a directory of choice
parameters: file of interested
"""
import Pathways


class Uploader:
    """
    Upload a file to a directory of choice:
    can be used as: Uploader([Direcotry]).handle_uploaded_file
    """
    def __init__(self, file):
        self.file = file


    def handle_uploaded_file(self):
        """
        handles upload, and writes it to the directory of choice
        :return: void
        """
        with open(Pathways.LOCATIONUPLOADEDFILES + str(self.file), 'wb+') as destination:
            for chunk in self.file.chunks():
                destination.write(chunk)
