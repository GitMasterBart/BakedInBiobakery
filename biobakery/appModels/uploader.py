#!/env/bin/python3

"""
Upload a file to a directory of choice
"""

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
        return Checker(self.file).check_gz_zip()

    def handle_uploaded_file(self):
        """
        handles upload, and writes it to the directory of choice
        :return: void
        """
        with open('/Users/bengels/Desktop/Uploaded_files/' + str(self.file), 'wb+') as destination:
            for chunk in self.file.chunks():
                destination.write(chunk)


def main():
    """
    test the uploader.
    :return:
    """
    # u = Uploader("txt.sh")
    # print(u.check_file() == 1)
    # print(str(u.check_file()))
    # if str(u.check_file) == "False":
    #     print("prefix wrong")
    #
    # ut = Uploader("txt.gz")
    # ut.check_file()
    # if ut.check_file == "True":
    #     print("prefix gz")

if __name__ == '__main__':
    main()
