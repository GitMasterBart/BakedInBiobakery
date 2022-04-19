from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Users


# Create your views here.
from django.views import View

from biobakery.forms import ApplicatonForm
from biobakery import Handle_upload

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
        if request.method == 'POST' and request.FILES.get('input_file'):
            Handle_upload.handle_uploaded_file(request.FILES.get('input_file'))
            # print(str(request.FILES.get('input_file')) + " "  + str(request.POST.get('project'))
            #       + " "  + str(request.POST.get('date')))
            return render(request, 'v2/succes_page.html')
        return render(request, 'v2/Upload_form.html', {'form': form })

class SuccesVieuws(View):
    def get(self, request):
        return render(request, "v2/succes_page.html")