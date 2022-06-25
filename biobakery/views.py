from zipfile import BadZipFile

from django.shortcuts import render, redirect

import Pathways
from .appModels.start_processes import ProcessesStarter
from .models import Users, Researches
from .appModels.unzipper import Unzipper
from biobakery.appModels.checker import Checker

# Create your views here.
import os
import Error_messages
from django.views import View
from biobakery.appModels.write_to_database import WriteToDb
from biobakery.forms import ApplicatonForm, NewUserForm
from .appModels.uploader import Uploader


class HomeViews(View):

    def get(self, request):
        os.system("python manage.py runserver")
        intitals = Users.objects.all()
        print(intitals)
        return render(request, "v2/Home.html", {'intials': intitals})

    def post(self, request):
        intitals = Users.objects.all()
        if request.method == "POST":
            request.session['username'] = request.POST.get("initials_user")
        return redirect("/biobakery/Upload")


class Uploadfiles(View):
    def get(self, request):
        form = ApplicatonForm()
        initials = request.session.get('username')
        return render(request, "v2/Upload_form.html", {'form': form, "username": initials})

    def post(self, request):
        form = ApplicatonForm(request.POST)
        newpage = ""
        # print(form.fields['tool_optons_humann'].choices)
        # print(request.POST.getlist('tool_optons_humann'))
        ## tool data
        input_file = request.FILES.get('input_file')
        used_tool = "compleet"
        request.session["input_file"] = str(input_file).split(".")[0]

        if request.method == 'POST' and input_file:
            print(type(input_file))
            uploaded = Uploader(input_file)
            if uploaded.check_file():
                # adding research to db
                initials = request.session.get('username')
                research_name = request.POST.get("project") + "_" + request.POST.get("date") + "_" + str(initials)
                request.session['research_name'] = research_name
                createdb = WriteToDb(initials, "Microbiologie", research_name)
                createdb.add_research_to_db()

                try:
                    uploaded.handle_uploaded_file()
                except BadZipFile:
                    error_massage = Error_messages.WRONGEXTENTIONERROR
                    newpage = render(request, 'v2/error_page.html', {'error_massage': error_massage})

                newpage = render(request, 'v2/succes_page.html')

                try:
                    switch = Unzipper(str(request.FILES.get('input_file')))
                    switch.control_unzip_switch()
                    switch.contorl_gzip_switch()
                except BadZipFile:
                    error_massage = Error_messages.WRONGEXTENTIONERROR
                    newpage = render(request, 'v2/error_page.html', {'error_massage': error_massage})


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
                    if checking.check_if_not_exist() or checking.check_if_it_contains_hypend():
                        error_massage = Error_messages.FIlESINZIPNOTCORRECT
                        newpage = render(request, 'v2/error_page.html', {'error_massage': error_massage})
                    if len(USEDOPTIONSKNEADDATA) > 3:
                        used_tool = "kneaddata"
                        newpage = redirect("/biobakery/fastqcCheck")

                    newactivatie = ProcessesStarter(used_tool, str(input_file).split(".")[0],
                                                    research_name, user_id, research_id, total_list_variables,
                                                    total_list_options)
                    newactivatie.start_humann_multi()

                except FileNotFoundError:
                    error_massage = Error_messages.FILENOTFOUNDERROR
                    newpage = render(request, 'v2/error_page.html', {'error_massage': error_massage})

            else:

                newpage = render(request, 'v2/Upload_form.html',
                                 {'form': form, "error_message": Error_messages.WRONGEXTENTIONERROR})
        return newpage


class SuccesVieuws(View):
    def get(self, request):
        return render(request, "v2/succes_page.html")


class AddUser(View):
    def get(self, request):
        add_user_form = NewUserForm()
        return render(request, "v2/new_user.html", {'form': add_user_form})

    def post(selfs, request):
        if request.method == 'POST':
            initials = request.POST.get("initials")
            # needs to be made dynamic
            createdb = WriteToDb(initials, "Microbiologie", "placeholder")
            createdb.add_users_to_db()
            os.system("python manage.py runserver")
        return redirect("/biobakery/Home")


class Information(View):
    def get(self, request):
        add_user_form = NewUserForm()
        return render(request, "v2/info_page.html", {'form': add_user_form})

    def post(selfs, request):
        return redirect("/biobakery/Home")


class FastqcCheck(View):
    def get(self, request):
        png = os.listdir(Pathways.FASTQCIMGFOLDER)
        return render(request, "v2/fastqc_check_page.html", {"png": png})

    def post(selfs, request):
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
                                            research_name, user_id, research_id, total_list_variables,
                                            total_list_options)
            newactivatie.start_humann_multi()
            new_page = render(request, "v2/succes_page.html")

        return new_page
