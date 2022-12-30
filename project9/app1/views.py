from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d={'name':'Suraj', 'mobile':123}
    return render(request,'jinja_print.html',context=d)
