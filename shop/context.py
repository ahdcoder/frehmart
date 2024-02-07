from .models import *
def include(request):

    if request.user.is_authenticated:
        cart,created = Cart.objects.get_or_create(user=request.user,status=False)
        wishlist,created = Wishlist.objects.get_or_create(user=request.user)
    else:
        cart = None
        wishlist = None

    return {
        'cart':cart,
        'wishlist':wishlist,
    }