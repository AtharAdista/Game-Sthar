from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Shaquille Athar Adista',
        'class' : 'PBP A',

    }

    return render(request, "main.html", context)