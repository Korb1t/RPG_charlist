from django.shortcuts import render
from main.models import Char


# Create your views here.


def char_list(request):
    chars = Char.objects.all()

    ctx = {
        'chars': chars
    }

    return render(request, 'charlists.html', ctx)


def stat_table(request, id):
    char = Char.objects.filter(pk=id)[0]

    ctx = {
        'char': char
    }

    return render(request, 'stats.html', ctx)
