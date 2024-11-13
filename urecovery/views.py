from django.shortcuts import redirect

def redirect_to_swagger(request):
    return redirect('/swagger/')