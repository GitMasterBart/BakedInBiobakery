#!/env/bin/python3
"""
This file looks add the requests and redirects it to the
correct view class
"""

__author__ = "Bart Engels"
__date__ = "28-07-2022"
__version__ = "v1"

from django.urls import path

# from polls.views import Myviews
from biobakery.views import *

urlpatterns = [
    path('Home', HomeViews.as_view()),
    path('Upload', UploadViews.as_view()),
    path('succes', SuccesViews.as_view()),
    path('addUser', AddUser.as_view()),
    path('information', Information.as_view()),
    path('fastqcCheck', FastqcCheckViews.as_view()),

]
