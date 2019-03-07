from django.shortcuts import render

# Create your views here.


def char_list(request):

    return render(request, 'charlists.html')
