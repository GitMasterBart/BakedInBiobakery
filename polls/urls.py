from urllib import request

from django.urls import path

# from polls.views import Myviews
from polls.views import *
# from .views

urlpatterns = [
    # path('', Myviews.geeks_view, name='base'),
    path('HUMAnN', Myviews.as_view(), name='uplaoding'),
    path('create/', create_session),
    path('access', access_session)
    # path('HUMAnN/start', views.run_scripts)
]
