from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def result(request):
    name=request.POST['yourname']
    location=request.POST['selections']
    languages=request.POST['selection-languages']
    comment=request.POST['comment']
    context={
        'posted_name':name,
        'posted_location':location,
        'posted_lan':languages,
        'posted_comment':comment
    }
    return render(request,"index2.html",context)

