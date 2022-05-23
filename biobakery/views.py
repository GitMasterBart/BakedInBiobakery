from django.shortcuts import render, redirect

from .appModels.start_processes import ProcessesStarter
from .models import Users
# from .appModels.start_processes import ProcessesStarter
from .appModels.tool_switch import Switcher


# Create your views here.
import os
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
        username = request.session.get('username')
        return render(request, "v2/Upload_form.html", {'form': form, "username" : username})

    def post(self, request):
        form = ApplicatonForm(request.POST)
        newpage = ""
        # print(form.fields['tool_optons_humann'].choices)
        # print(request.POST.getlist('tool_optons_humann'))
            ## tool data

        if request.method == 'POST' and request.FILES.get('input_file'):
            uploaded = Uploader(request.FILES.get('input_file'))
            if uploaded.check_file():
                uploaded.handle_uploaded_file()
                newpage = render(request, 'v2/succes_page.html')
                # print(str(request.FILES.get('input_file')))
                switch = Switcher(request.POST.get("BiobakeryTool"), str(request.FILES.get('input_file')), request.POST.getlist('tool_optons_humann'))
                switch.control_unzip_switch()
                # switch.tool_switch()
                # print(str(request.FILES.get('input_file')).split(".")[0])

                total_list_variables = request.POST.getlist('tool_optons_humann') + request.POST.getlist('tool_optons_kneaddata')
                total_list_options = form.fields['tool_optons_humann'].choices + form.fields['tool_optons_kneaddata'].choices
                print(total_list_variables)
                newactivatie = ProcessesStarter(str(request.FILES.get('input_file')).split(".")[0], total_list_variables, total_list_options)
                newactivatie.start_humann_multi()
            else:
                print("wrong prefix")
                newpage = render(request, 'v2/Upload_form.html', {'form': form, "errormessage": "Your file does not "
                                                                                                 "have te right "
                                                                                                 "prefix"})
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
            createdb = WriteToDb("/Users/bengels/Desktop/output_data/output_gentable.tsv", initials,
                                         "Microbiologie",
                                         "2022-05-03", "FirstTestOnderzoek")
            createdb.add_users_to_db()
            os.system("python manage.py runserver")
        return redirect("/biobakery/Home")





