from django.http import HttpResponse

def homePage(request):
    return HttpResponse("<h1>My Home Page</h1>")