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
    stats = [['Melee Skill', char.Melee, char.Melee_bonus],
             ['Balistic', char.Range, char.Range_bonus],
             ['Will Power', char.WillPower, char.WillPower_bonus],
             ['Strength', char.Strength, char.Strength_bonus],
             ['Agility', char.Agility, char.Agility_bonus],
             ['Intelligence', char.Intelligence, char.Intelligence_bonus],
             ['Perception', char.Perception, char.Perception_bonus],
             ['Toughness', char.Toughness, char.Toughness_bonus],
             ['Fellowship', char.Fellowship, char.Fellowship_bonus]]

    ctx = {
        'char': char,
        'stats': stats,
    }

    return render(request, 'stats.html', ctx)

