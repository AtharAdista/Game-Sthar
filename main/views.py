from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Shaquille Athar Adista',
        'class' : 'PBP A',
        'game' : 'EA SPORTS™ FIFA 23 ',
        'category' : 'Sport',
        'amount' : 20,
        'price' : 400000,
        'platform' : 'PC, Nintendo Switch, Xbox X|S, Xbox One, playStation 4',
        'description' : ' FIFA 23 provides an authentic soccer simulation, making it a must-play for soccer enthusiasts worldwide. Enjoy dynamic stadium atmospheres and cross-platform play, making it a thrilling and immersive gaming experience.'


    }

    return render(request, "main.html", context)