from django.shortcuts import render
from time import gmtime, strftime,localtime
    
def index(request):
    context = {
        "time": strftime("%H:%M %p", localtime()),
        "date": strftime("%d %m %Y ",localtime())
    }
    return render(request,'index.html', context)


# Create your views here.
