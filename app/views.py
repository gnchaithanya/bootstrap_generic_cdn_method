from django.shortcuts import render

# Create your views here.
def cdn_bootstrap(request):
    return render(request,'cdn_bootstrap.html')

def first(request):
    return render(request,'first.html')
def second(request):
    return render(request,'second.html')
def buttons(request):
    return render(request,'buttons.html')
def button_group(request):
    return render(request,'button_group.html')
def card(request):
    return render(request,'card.html')
def Carousel(request):
    return render(request,'Carousel.html')
