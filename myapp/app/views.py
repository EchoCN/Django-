from django.shortcuts import render

# Create your views here.
def query(request):
    return render(request,'search/query.html')