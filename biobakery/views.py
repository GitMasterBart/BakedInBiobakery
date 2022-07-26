#!/env/bin/python3
"""
The view class is the response handler from the application,
it handles the responses that are sent by URLS
"""

__author__ = "Bart Engels"
__date__ = "28-07-2022"
__version__ = "v1"


from zipfile import BadZipFile
import os
from django.shortcuts import render, redirect
from django.views import View

import Pathways
import Error_messages

from .appModels.start_processes import ProcessesStarter

from .appModels.unzipper import Unzipper
from .appModels.uploader import Uploader

from .models import Users, Researches

from biobakery.appModels.write_to_database import WriteToDb
from biobakery.forms import ApplicatonForm, NewUserForm
from biobakery.appModels.checker import Checker


class HomeViews(View):
    """
    Response handler for URL: Biobakery/Home
    """

    def get(self, request):
        """
        Fetch users initials from database
        :param request: urls
        :return: Home.html + list with initials
        """
        os.system("python manage.py runserver")
        intitals = Users.objects.all()
        print(intitals)
        return render(request, "v2/Home.html", {'intials': intitals})

    def post(self, request):
        """
        Send new reqeust and saves user initials in session
        :param request: urls
        :return: request biobakery/Upload
        """
        intitals = Users.objects.all()
        if request.method == "POST":
            request.session['username'] = request.POST.get("initials_user")
        return redirect("/biobakery/Upload")


class UploadViews(View):
    """
    Response handler for URL: Biobakery/Upload
    """
    def get(self, request):
        """
        Renders the upload page with the initials in session
        :param request: urls
        :return: upload_form.hlml + upload form +  initials
        """
        form = ApplicatonForm()
        initials = request.session.get('username')
        return render(request, "v2/Upload_form.html", {'form': form, "username": initials})

    def post(self, request):
        """
        Starts the workflow and sends a reqeust to the fastaqc_check or the succes_page
        :param request: urls
        :return: succes_page.html or fastqc_check.html + folder with fatqc files
        """
        form = ApplicatonForm(request.POST)
        newpage = ""
        input_file = request.FILES.get('input_file')
        used_tool = "compleet"
        request.session["input_file"] = str(input_file).split(".")[0]
        if request.method == 'POST' and input_file:
            if Checker(input_file).check_zip():
                uploaded = Uploader(input_file)
                # adding research to db
                initials = request.session.get('username')
                research_name = request.POST.get("project") + "_" + \
                                request.POST.get("date") + "_" + str(initials)
                request.session['research_name'] = research_name
                createdb = WriteToDb(initials, "Microbiologie", research_name)
                createdb.add_research_to_db()

                try:
                    uploaded.handle_uploaded_file()
                except (BadZipFile , IsADirectoryError):
                    error_massage = Error_messages.WRONGEXTENTIONERROR
                    return render(request, 'v2/error_page.html', {'error_massage': error_massage})

                newpage = render(request, 'v2/succes_page.html')

                try:
                    switch = Unzipper(str(request.FILES.get('input_file')))
                    switch.unzip_zip_folder()
                    switch.unzip_gz_files()
                except (BadZipFile, FileNotFoundError):
                    error_massage = Error_messages.WRONGEXTENTIONERROR
                    return render(request, 'v2/error_page.html', {'error_massage': error_massage})

                user_id = Users.objects.filter(initials=initials) \
                    .values_list('User_id', flat=True).first()
                research_id = Researches.objects.filter(name=research_name) \
                    .values_list('researches_id', flat=True).first()
                USEDOPTIONSKNEADDATA = request.POST.getlist('tool_optons_kneaddata')
                USEDOPTIONSHUMANTOOL = request.POST.getlist('tool_optons_humann')
                total_list_variables = USEDOPTIONSHUMANTOOL + USEDOPTIONSKNEADDATA
                request.session['options_human'] = USEDOPTIONSHUMANTOOL
                POSSILBLEOPTIONSKNEADDATA = form.fields['tool_optons_kneaddata'].choices
                POSSILBLEOPTIONSHUMANTOOL = form.fields['tool_optons_humann'].choices
                total_list_options = POSSILBLEOPTIONSHUMANTOOL + POSSILBLEOPTIONSKNEADDATA

                request.session['possible_options_human'] = POSSILBLEOPTIONSHUMANTOOL

                try:
                    checking = Checker(Pathways.INPUTFILESLOCATION + str(input_file))
                    if checking.check_if_sample_same_as_folder():
                        error_massage = Error_messages.FIlESINZIPNOTCORRECT
                        return render(request, 'v2/error_page.html',
                                      {'error_massage': error_massage})
                    if checking.check_if_contains_hypend():
                        error_massage = Error_messages.FIlESHASEHYPENDERROR
                        return render(request, 'v2/error_page.html',
                                      {'error_massage': error_massage})
                    if "--run-fastqc-start" in USEDOPTIONSKNEADDATA \
                            and "--run-fastqc-end" in USEDOPTIONSKNEADDATA:
                        used_tool = "kneaddata"
                        newpage = redirect("/biobakery/fastqcCheck")
                    if checking.checks_fastq():
                        error_massage = Error_messages.FILENOTFASTQERROR
                        return render(request, 'v2/error_page.html',
                                      {'error_massage': error_massage})
                    newactivatie = ProcessesStarter(used_tool, str(input_file).split(".")[0],
                                                        research_name, user_id,
                                                    research_id, total_list_variables,
                                                        total_list_options)
                    newactivatie.start_humann_multi()

                except FileNotFoundError:
                    error_massage = Error_messages.FILENOTFOUNDERROR
                    return render(request, 'v2/error_page.html',
                                  {'error_massage': error_massage})
            else:
                newpage = render(request, 'v2/Upload_form.html',
                                 {'form': form, "error_message":
                                     Error_messages.WRONGEXTENTIONERROR})
        return newpage


class SuccesViews(View):
    """
    Response handler for URL: Biobakery/succes_page
    """
    def get(self, request):
        """
         Renders the succes page
        :param request:
        :return: succes_page.html
        """
        return render(request, "v2/succes_page.html")


class AddUser(View):
    """
    Response handler for URL: Biobakery/addUser
    renders a page were the user can add initials
    """
    def get(self, request):
        """
        Renders the new_user.html
        :param request: urls
        :return: new_users.html
        """
        add_user_form = NewUserForm()
        return render(request, "v2/new_user.html", {'form': add_user_form})

    def post(selfs, request):
        """
        Saves initials in database and redirects to the home page
        :param request: urls
        :return: biobakery/Home
        """
        if request.method == 'POST':
            initials = request.POST.get("initials")
            # needs to be made dynamic
            createdb = WriteToDb(initials, "Microbiologie", "placeholder")
            createdb.add_users_to_db()
            os.system("python manage.py runserver")
        return redirect("/biobakery/Home")


class Information(View):
    """
    Request handler for URL: biobakery/information
    """
    def get(self, request):
        """
        renders info_page.html and displays infromation
        :param request:
        :return:info_page.html + users form
        """
        add_user_form = NewUserForm()
        return render(request, "v2/info_page.html", {'form': add_user_form})



class FastqcCheckViews(View):
    """
    Request handler for URL: biobakery/fastqcCheck
    """
    def get(self, request):
        """
        renders page with the png files that are present in: static/img/fastqc_results
        :param request: urls
        :return: fastqc_page.html + files from static/img/fastqc_results
        """
        png = os.listdir(Pathways.FASTQCIMGFOLDER)
        return render(request, "v2/fastqc_check_page.html", {"png": png})

    def post(selfs, request):
        """
        handles the request from the user to go back or to further with the next step.
        :param request: urls
        :return: succes_page.html
        """
        new_page = redirect("/biobakery/Upload")
        if request.method == 'POST' and "next" in request.POST:
            initials = request.session.get('username')
            research_name = request.session.get("research_name")
            print(research_name)
            input_file = request.session.get("input_file")
            used_tool = "compleet"
            user_id = Users.objects.filter(initials=initials) \
                .values_list('User_id', flat=True).first()
            research_id = Researches.objects.filter(name=research_name) \
                .values_list('researches_id', flat=True).first()
            total_list_variables = request.session.get('options_human')
            total_list_options = request.session.get('possible_options_human')
            newactivatie = ProcessesStarter(used_tool, input_file,
                                            research_name, user_id,
                                            research_id, total_list_variables,
                                            total_list_options)
            newactivatie.start_humann_multi()
            new_page = render(request, "v2/succes_page.html")

        return new_page
