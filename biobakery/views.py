from django.shortcuts import render, redirect

import Pathways
from .appModels.start_processes import ProcessesStarter
from .models import Users, Researches
# from .appModels.start_processes import ProcessesStarter
from .appModels.tool_switch import Switcher
from biobakery.appModels.checker import Checker
from django.core.exceptions import *

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
        return render(request, "v2/Home.html", {'intials' : intitals})

    def post(self, request):
        intitals = Users.objects.all()
        if request.method == "POST":
            request.session['username'] = request.POST.get("initials_user")
        return redirect("/biobakery/Upload")

class Uploadfiles(View):
    def get(self, request):
        form = ApplicatonForm()
        initials = request.session.get('username')
        return render(request, "v2/Upload_form.html", {'form': form, "username" : initials})

    def post(self, request):
        form = ApplicatonForm(request.POST)
        newpage = ""
        # print(form.fields['tool_optons_humann'].choices)
        # print(request.POST.getlist('tool_optons_humann'))
            ## tool data
        input_file = request.FILES.get('input_file')

        if request.method == 'POST' and input_file:
            uploaded = Uploader(input_file)
            if uploaded.check_file():
                # adding research to db
                initials = request.session.get('username')
                research_name = request.POST.get("project") + "_" + request.POST.get("date") + "_" + str(initials)
                createdb = WriteToDb(initials, "Microbiologie", research_name)
                createdb.add_research_to_db()

                try:
                    uploaded.handle_uploaded_file()
                except: #nee to be added:
                    error_massage = " "
                    newpage = render(request, 'v2/error_page.html', {'error_massage': error_massage})

                newpage = render(request, 'v2/succes_page.html')
                # print(str(request.FILES.get('input_file')))
                switch = Switcher(request.POST.get("BiobakeryTool"), str(request.FILES.get('input_file')), request.POST.getlist('tool_optons_humann'))
                switch.control_unzip_switch()
                # switch.tool_switch()
                # print(str(request.FILES.get('input_file')).split(".")[0])

                user_id = Users.objects.filter(initials=initials) \
                    .values_list('User_id', flat=True).first()
                research_id = Researches.objects.filter(name=research_name) \
                    .values_list('researches_id', flat=True).first()

                total_list_variables = request.POST.getlist('tool_optons_humann') + request.POST.getlist('tool_optons_kneaddata')
                total_list_options = form.fields['tool_optons_humann'].choices + form.fields['tool_optons_kneaddata'].choices



                try:
                    if Checker(Pathways.INPUTFILESLOCATION + str(input_file)).check_if_exist():
                        error_massage = Error_messages.FIlESINZIPNOTCORRECT
                        newpage = render(request, 'v2/error_page.html', {'error_massage': error_massage})
                    newactivatie = ProcessesStarter(str(input_file).split(".")[0],
                                                            research_name, user_id, research_id, total_list_variables, total_list_options)
                    newactivatie.start_humann_multi()
                except FileNotFoundError:
                    error_massage = Error_messages.FILENOTFOUNDERROR
                    newpage = render(request, 'v2/error_page.html', {'error_massage': error_massage})

            else:

                newpage = render(request, 'v2/Upload_form.html', {'form': form, "error_message": Error_messages.WRONGEXTENTIONERROR})
            # print(str(request.FILES.get('input_file')) + " "  + str(request.POST.get('project'))
            #       + " "  + str(request.POST.get('date')))
        return newpage

class SuccesVieuws(View):
    def get(self, request):
        return render(request, "v2/succes_page.html")

class AddUser(View):
    def get(self, request):
        add_user_form = NewUserForm()
        return render(request, "v2/new_user.html", {'form': add_user_form})

    def post(selfs, request):
        add_user_form = NewUserForm()
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





