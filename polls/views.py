from urllib import request

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views import View
from polls.StartProcesses import ActivateProcesses
import Pathways
from polls.fileScraper import FileScraper
import os
import zipfile


class Myviews(View):
    template_name = Pathways.HumanPage_html


    def geeks_view(self, request):
        return render(request, Pathways.base_html)

    def get(self, request, *args, **kwargs):

        fileScraper = FileScraper(Pathways.imgFasqc_folder)
        fileScraper.find_files()
        img_files = fileScraper.get_pngreadyfiles()

        print(img_files)


        # form = self.form_class(initial=self.initial)
        return render(request, self.template_name, { 'uploaded_file_url': request.session.get('filePath'), "img_files": img_files})

    def post(self, request):
        request.session['filePath'] = ""
        fileScraper = FileScraper(Pathways.imgFasqc_folder)
        fileScraper.find_files()
        img_files = fileScraper.get_pngreadyfiles()

        if request.method == 'POST' and request.FILES.get('myfile'):
            myfile = request.FILES.get('myfile')
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            request.session['filePath'] = fs.url(filename)
            startFastqc = ActivateProcesses("fastqcStarter.sh", request.session['filePath'], str(request.session['filePath']).split(".")[0] + "_fastqc.zip")
            startFastqc.startFastqc()
            print(request.session['filePath'].split(".")[0])
            os.replace("/Users/bengels/Desktop/StageWetsus2022/BakedInBiobakery" + str(request.session['filePath']).split(".")[0] + "_fastqc" + "/images",
                           "/Users/bengels/Desktop/StageWetsus2022/BakedInBiobakery/static/fastqcfiles/images/")
            return render(request, Pathways.HumanPage_html, {
                    'uploaded_file_url': request.session.get('filePath'), "img_files": img_files
            })

        elif 'run_script' in request.POST:
            if request.method == 'POST' and 'run_script' in request.POST:
                print(request.POST.get('threads'))
                Newactivatie = ActivateProcesses(Pathways.bashscript, request.session.get('filePath'), request.POST.get('threads'))
                Newactivatie.startHumaNn()

        elif 'run_fastqct' in request.POST:
            if request.method == 'POST' and 'run_fastqct' in request.POST:
               return render(request, Pathways.HumanPage_html, {'uploaded_file_url': request.session.get('filePath'),  "img_files": img_files})
                # img_files = fileScraper.get_pngreadyfiles()
        print(img_files)


        return render(request, Pathways.HumanPage_html, {
                    'uploaded_file_url': request.session.get('filePath'), "img_files": img_files
            })


