from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    #return HttpResponse("<h1>Mi web personal</h1>")
def about(request):
    return render(request, 'core/about.html')
#gx:me llevé la vista de portfolio a su app

def contact(request):
    return render(request, 'core/contact.html')
