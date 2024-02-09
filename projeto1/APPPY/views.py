from django.shortcuts import render

# Create your views here.

def nomedafuncaoview (request):
    return render(
        request,
        'PYT/index.html'
    )