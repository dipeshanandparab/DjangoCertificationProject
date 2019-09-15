from django.http import HttpResponse

def blogPage(request):
    return HttpResponse("Blog Home Page")