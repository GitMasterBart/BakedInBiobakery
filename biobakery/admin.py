from django.contrib import admin

from .models import Department
from .models import Researches
from .models import Users

admin.site.register(Department)
admin.site.register(Researches)
admin.site.register(Users)



