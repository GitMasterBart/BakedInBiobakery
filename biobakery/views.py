from django.shortcuts import render, redirect
from .models import Users
from .appModels.start_processes import ProcessesStarter
from .appModels.tool_switch import Switcher


# Create your views here.
from django.views import View

from biobakery.forms import ApplicatonForm
from .appModels.uploader import Uploader


class HomeViews(View):

    def get(self, request):
        intitals = Users.objects.all()
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
        if request.method == 'POST' and request.FILES.get('input_file'):
            uploaded = Uploader(request.FILES.get('input_file'))
            if uploaded.check_file():
                uploaded.handle_uploaded_file()
                newpage = render(request, 'v2/succes_page.html')
                switch = Switcher(request.POST.get("BiobakeryTool"),str(request.FILES.get('input_file')), "~/Desktop/output_data")
                switch.control_unzip_switch()
                switch.tool_switch()
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