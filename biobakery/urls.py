from urllib import request

from django.urls import path

# from polls.views import Myviews
from biobakery.views import *
from . import views

urlpatterns = [
    # path('', Myviews.geeks_view, name='base'),
    path('Home', HomeViews.as_view()),
    path('Upload', Uploadfiles.as_view() ),
    path('succes', SuccesVieuws.as_view())
]
