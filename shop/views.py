from django.shortcuts import render


# @login_required
def shop(request):
    return render(request, 'shop.html', {})