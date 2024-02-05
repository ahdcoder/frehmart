from .models import *
def include(request):

    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
    else:
        cart = None

    return {
        'cart':cart,
    }