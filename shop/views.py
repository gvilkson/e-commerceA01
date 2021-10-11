from django.shortcuts import render


# @login_required
def shop(request):
    return render(request, 'shop.html', {})

def cart(request):
    return render(request, 'cart.html', {})