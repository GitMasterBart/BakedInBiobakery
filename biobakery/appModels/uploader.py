
from biobakery.appModels.checker import Checker

class Uploader:



    def __init__(self, file):
        self.file = file

    def check_file(self):
        return Checker(self.file).check_gz_zip()

    def handle_uploaded_file(self):
        with open('/Users/bengels/Desktop/Uploaded_files/' + str(self.file), 'wb+') as destination:
            for chunk in self.file.chunks():
                destination.write(chunk)


def main():
    u = Uploader("txt.sh")
    print(u.check_file() == 1)
    print(str(u.check_file()))
    if str(u.check_file) == "False":
        print("prefix wrong")

    ut = Uploader("txt.gz")
    ut.check_file()
    if ut.check_file == "True":
        print("prefix gz")

if __name__ == '__main__':
    main()