from django.shortcuts import redirect, render

import json
import requests
from api.helpers.Auth import MyAuthentication
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login

from django.conf import settings


# Create your views here.
def Login(request):
    if request.session.get('TOKEN'):
        user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))
    else:
        message = str

    if request.user.is_authenticated:
        
        if status:
            return redirect("home")
    else:
        if request.method == "POST":
            usuario = request.POST.get('usuario')
            password = request.POST.get('password')

            res = json.loads(requests.post(settings.DIRECCION_SERVER + 'api/auth/', json={'username': usuario, 'password': password})._content)
            status = res.get('status')
            mensaje = res.get('message')
            user = res.get('username')
            TOKEN = res.get('token')
            
            request.session['TOKEN'] = TOKEN
            
            

            if status:
                user = authenticate(username=usuario, password=password)
                do_login(request, user)

                if request.user.is_authenticated:
                    request.session['idUsuario'] = request.user.id
                    
                    return redirect("home")
            else:
                return render(request, 'login/login.html', {"mensaje": "Datos Incorrectos"})
        else:
            return render(request, 'login/login.html', {"mensaje": message})