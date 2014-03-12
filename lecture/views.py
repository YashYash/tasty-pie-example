from django.shortcuts import render


def presentation(request):
    return render(request, "presentation.html")

def angular(request):
    return render(request, "angular.html")