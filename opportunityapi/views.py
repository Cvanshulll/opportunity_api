from django.http import HttpResponse

def home_page(request):
    print("home page requested")
    return HttpResponse("Hello, world. You're at the opportunityapi index.")