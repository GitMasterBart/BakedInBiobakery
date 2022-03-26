from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views import View
from polls.StartProcesses import activateHumaNn

globals()


class Myviews(View):
    uploaded_file_url = ""
    template_name = 'uploading.html'

    def geeks_view(self, request):
        return render(request, "base.html")

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name)

    def post(self, request):

        if request.method == 'POST' and request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            request.session['filePath'] = fs.url(filename)

            return render(request, 'uploading.html', {
                'uploaded_file_url': request.session.get('filePath')
            })

        elif 'run_script' in request.POST:
            if request.method == 'POST' and 'run_script' in request.POST:
                print(request.POST.get('threads'))
                Newactivatie = activateHumaNn("HumanBashScript.sh",request.session.get('filePath'), request.POST.get('threads'))
                Newactivatie.startHumaNn()

        return render(request, 'uploading.html')


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")


def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')

