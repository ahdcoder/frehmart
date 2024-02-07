from django.shortcuts import render,redirect

def simple_middleware(get_response):

    def middleware(request):
        if '/adminpanel/' in request.path:
            if not request.path == '/adminpanel/auth_admin/auth_login/':
                if not request.user.is_staff or (not request.user.is_superuser and not request.user.is_staff):
                    return redirect('/adminpanel/auth_admin/auth_login/')
                
        if not('/' in request.path):
            if not request.user.is_authenticated:
                return redirect('/')

        if request.user.is_authenticated and (not request.user.is_superuser or not request.user.is_staff):
            if not (request.path == '/logout/' or request.path == '/confirm_acc/'):
                if request.user.is_authenticated:
                    if (hasattr(request.user, 'confirmcode')) and not request.user.confirmcode.status:
                        return redirect("/confirm_acc/")

        response = get_response(request)

        return response
    
    return middleware