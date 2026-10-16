from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page request")
    friends = ['ankit', 'ravi', 'gautam']
    return JsonResponse(friends, safe=False)


