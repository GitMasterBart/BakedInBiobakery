from django.test import TestCase

from biobakery.appModels.uploader import Uploader
from biobakery.appModels.file_scraper import FileScraper
from biobakery.appModels.start_processes import ProcessesStarter
from biobakery.appModels.checker import Checker
import Pathways


class URLTest(TestCase):
    """
    test for URLs
    """
    def test_testhomepage(self):
        """
        tests if URL homepage is correct
         :return: boolean
        """
        response = self.client.get("/biobakery/Home")
        self.assertEquals(response.status_code, 200)

    def test_testuploadpage(self):
        """
        tests if URL upload page is correct
         :return: boolean
        """
        response = self.client.get("/biobakery/Upload")
        self.assertEquals(response.status_code, 200)

    def test_testfastqc_chekpag(self):
        """
        tests if URL fastqc check page is correct
         :return: boolean
        """
        response = self.client.get("/biobakery/fastqcCheck")
        self.assertEquals(response.status_code, 200)

    def test_testinfopage(self):
        """
        tests if URL information page is correct
         :return: boolean
        """
        response = self.client.get("/biobakery/information")
        self.assertEquals(response.status_code, 200)

    def test_testnewuserpage(self):
        """
        tests if URL new user page is correct
         :return: boolean
        """
        response = self.client.get("/biobakery/addUser")
        self.assertEquals(response.status_code, 200)

    def test_testsuccespage(self):
        """
        tests if URL succes page is correct
         :return: boolean
        """
        response = self.client.get("/biobakery/succes")
        self.assertEquals(response.status_code, 200)


class UploaderCheckTest(TestCase):
    """
    test that check if the uploader works.
    """
    def test_testuploader_zipcheck_sunnycase(self):
        """
        sunny case of zip checker. it hase a zip extension
         :return: boolean
        """
        uploaded = Uploader('file.zip')
        uploaded.check_file()
        self.assertEquals(uploaded.check_file(), True)

    def test_testuploader_zipcheck_worstcase(self):
        """
        worst case of zip checker. it does not have a txt extension
        :return: boolean
        """
        uploaded = Uploader('file.txt')
        uploaded.check_file()
        self.assertEquals(uploaded.check_file(), False)

class FilescrapperTest(TestCase):
    """
    test if filescraper works as designed
    """
    def test_filescrapper_find_files_in_directories(self):
        """
        check if find_files_in_directories works
        :return:boolean
        """
        search_directory = FileScraper(Pathways.LOCATIONOFYOURPROJECT + "djangoProject/")
        search_directory.find_files_in_directories()

    def test_filescrapper_get_directory_list(self):
        """
        check if get_directory_list works
        :return:boolean
        """
        search_directory = FileScraper(Pathways.LOCATIONOFYOURPROJECT + "djangoProject/")
        search_directory.find_files_in_directories()
        self.assertEquals(search_directory.get_fileset(), ['asgi.py', '__init__.py', 'settings.py', 'urls.py', 'wsgi.py'])

    def test_filescrapper_get_directory_list_onlynames(self):
        """
        check if get_directory_list_onlynames works
        :return: boolean
        """
        search_directory = FileScraper(Pathways.LOCATIONOFYOURPROJECT + "djangoProject/")
        search_directory.find_files_in_directories()
        self.assertEquals(search_directory.get_directory_list_onlynames(), ['__pycache__', '.idea'])

    def test_filescrapper_get_fileset_full_path(self):
        """
        check if get_fileset_full_paht works
        :return: boolean
        """
        search_directory = FileScraper(Pathways.LOCATIONOFYOURPROJECT + "djangoProject/")
        search_directory.find_files_in_directories()
        shouldbe = search_directory.get_fileset_full_path()
        self.assertEquals(search_directory.get_fileset_full_path(), shouldbe)

    def test_filescrapper_get_fileset(self):
        """
        check if get fileset works
        :return: boolean
        """
        search_directory = FileScraper(Pathways.LOCATIONOFYOURPROJECT + "djangoProject/")
        search_directory.find_files_in_directories()
        shouldbe = search_directory.get_fileset()
        self.assertEquals(search_directory.get_fileset(), shouldbe)

class write_to_data(TestCase):
    """
    checks if the write to database class works for each method this is
    namely the to test if the workflow works properly
    """
    def test_start_humann_multi(self):
        """
        check if the method start_humann_multi works
        :return: boolean
        """
        start = ProcessesStarter("compleet", "poging2_v1" , "d_2022-06-24_beng", 1, 48,
                                 ['--bypass-nucleotide-search', '--remove-temp-output',
                                  '--verbose', '/Users/bengels/Desktop/Uploaded_files/humann_dbs/unireffull/',
                                  '/Users/bengels/Desktop/Uploaded_files/humann_dbs/silvadb',
                                  '~/Desktop/kneaddataMap/Trimmomatic-0.36/',
                                  '--bypass-trf', '--run-fastqc-start',
                                  '--run-fastqc-end'],
                                 [('--bypass-nucleotide-search', 'bypass_n_search'),
                                ('--remove-temp-output', 'remove_temp_output'),
                                  ('--verbose', 'verbose'),
                                  ('/Users/bengels/Desktop/Uploaded_files/humann_dbs/unireffull/', 'protein_db'),
                                  ('/Users/bengels/Desktop/Uploaded_files/humann_dbs/chocophlan', 'nucleotide_db'),
                                  ('/Users/bengels/Desktop/Uploaded_files/humann_dbs/silvadb', 'silvadatabase'),
                                  ('~/Desktop/kneaddataMap/Trimmomatic-0.36/', 'trimmomatic'),
                                  ('--bypass-trf', 'bypass_trf'),
                                  ('--run-fastqc-start', 'fastqc_start'),
                                  ('--run-fastqc-end', 'fastqc_end')])
        self.assertEquals(start.start_humann_multi(), 0)


class ViewTest(TestCase):
    """
    test the views (request handlers)
    """
    def test_testhomeview(self):
        """
        does it return the correct url
        :return: boolean
        """
        response = self.client.post('/biobakery/Home', follow=True)
        self.assertRedirects(response, '/biobakery/Upload')

    def test_testuploadview(self):
        """
        check if upload view returns the correct url
        :return: boolean
        """
        response = self.client.post('/biobakery/Upload', follow=True)
        self.assertRedirects(response, '/biobakery/Upload')

class CheckerTest(TestCase):
    """
    test if the checks work
    """
    def test_check_if_it_contains_hypend(self):
        """
        checks if the check if contain_hypend_class_works
        :return: boolean
        """
        checkerclass = Checker("Sed_ut-perspiciatis")
        response = checkerclass.check_if_contains_hypend()
        self.assertEquals(response, True)




