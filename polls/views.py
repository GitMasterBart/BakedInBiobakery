from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views import View
from polls.StartProcesses import activateHumaNn
import Pathways




class Myviews(View):
    template_name = Pathways.HumanPage_html

    def geeks_view(self, request):
        return render(request, Pathways.base_html)

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name)

    def post(self, request):

        if request.method == 'POST' and request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            request.session['filePath'] = fs.url(filename)

            return render(request, Pathways.HumanPage_html, {
                'uploaded_file_url': request.session.get('filePath')
            })

        elif 'run_script' in request.POST:
            if request.method == 'POST' and 'run_script' in request.POST:
                print(request.POST.get('threads'))
                Newactivatie = activateHumaNn(Pathways.bashscript, request.session.get('filePath'), request.POST.get('threads'))
                Newactivatie.startHumaNn()

        return render(request, Pathways.HumanPage_html)

