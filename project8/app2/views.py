from django.shortcuts import render

# Create your views here.
def jinja_print2 (request):
    return render(request, 'jinja_print2.html')
