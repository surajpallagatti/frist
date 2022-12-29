from django.urls import path
from app1.views import *
app_name='any1'

urlpatterns = [
    
    path('jinja_print/', jinja_print, name='jinja_print'),
]
