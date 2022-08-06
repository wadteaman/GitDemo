from django.shortcuts import render


# Create your views here.
def pythonfile(request):
    return render(request, 'pythoncourse.html')
