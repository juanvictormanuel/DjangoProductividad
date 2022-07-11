import json
import requests
from django.shortcuts import redirect, render, HttpResponse

from api.helpers.Auth import MyAuthentication
# from django.contrib import messages
from django.conf import settings
from datetime import datetime
import pandas as pd
# Create your views here.




def home(request):
    
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))

    
   
    if status:
   
        if request.user.is_authenticated:
            res = json.loads(
                requests.get(settings.DIRECCION_SERVER + 'api/actividades/getbyon/%s'% request.user.id, headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content
            )

            res2 = json.loads(
                requests.get(settings.DIRECCION_SERVER + 'api/actividades/getbyon2/%s'% request.user.id, headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content
            )
            
            # status = res.get('status')
            mensaje = res.get('message')
            actividades = res.get('actividades')
            actividades2 = res2.get('actividades')

            if actividades:
                frame = pd.DataFrame.from_records(actividades)
                frame2 = pd.DataFrame.from_records(actividades2)
                # print('AAAAAAAAA', frame['Porcentaje'].sum())
                # frame['Porcentaje'] = (frame['Porcentaje'].sum() / 100) * frame['Jerarquia']

            
                frameTitle = frame.columns[:]
                frameTitle = list(tuple(frameTitle.to_numpy()))


                frameTitle2 = frame2.columns[:]
                frameTitle2 = list(tuple(frameTitle2.to_numpy()))

                
            else:
                frameTitle = [""]
                frame = [] 

                frameTitle2 = [""]
                frame2 = [] 

            mensaje = request.session.get('mensaje')

            if mensaje:
                request.session.pop('mensaje', "")


            
            return render(request, "core/home.html", {"username": "Bienvenido " + str(request.user.first_name),"frameTitle": frameTitle, 'frame': frame,"frameTitle2": frameTitle2, 'frame2': frame2, "mensaje":mensaje, "ruta":settings.DIRECCION_SERVER + 'api/actividades/completar/', "token": request.session.get('TOKEN')})
        else:
            return redirect("logout")
    
    else:

        return redirect("logout")


def task_add(request):
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))

    if status:
   
        if request.user.is_authenticated:
            if request.method == "POST":
                nombre = request.POST.get('txtNombre')
                actividades = request.POST.get('txtActividades')
                
                res = json.loads(requests.post(settings.DIRECCION_SERVER + 'api/procedimientos/', json={"fecha": str(datetime.now()),"nombre": nombre,"totalActividades" : actividades,"idUsuario": request.user.id}, headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content)
                
                status = res.get('status')
                mensaje = res.get('message')

                
                if status:
                    return render(request, "core/task_add.html", {"mensaje": mensaje, "status": 'success'} )
                else:
                    return render(request, "core/task_add.html", {"mensaje": mensaje, "status": 'error'} )
            else:
                return render(request, "core/task_add.html" )
        else:
            return redirect("logout")
    else:

        return redirect("logout")


def task_list(request):

    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))

    if status:
        if request.user.is_authenticated:

            res = json.loads(
                requests.get(settings.DIRECCION_SERVER + 'api/procedimientos/'+ str(request.user.id), headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content
            )

            
            status = res.get('status')
            # mensaje = res.get('message')
            procedimientos = res.get('procedimientos')
        
            if procedimientos:
                frame = pd.DataFrame.from_records(procedimientos)
                frameTitle = frame.columns[:]
                frameTitle = list(tuple(frameTitle.to_numpy()))

                
            else:
                frameTitle = ["No hay datos para mostrar"]
                frame = [] 

            mensaje = request.session.get('mensaje')
            

            if mensaje:
                request.session.pop('mensaje', "")

            return render(request,"core/task_list.html", {"frameTitle": frameTitle, 'frame': frame, "mensaje":mensaje, "status": "success"})
        else:
            return redirect("login")
    else:
            return redirect("login")

def task_update(request, id, nombre, actividades):
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))
    

    if status:
        if request.user.is_authenticated:
            return render(request, "core/task_update.html", {"id": id, "nombre": nombre, "actividades": actividades})

        else:
            return redirect("logout")
    else:
            return redirect("logout")

def task_update_2(request, id):
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))

    if status:
        if request.user.is_authenticated:
            if request.method == "POST":
                nombre = request.POST.get('txtNombre')
                actividades = request.POST.get('txtActividades')
                
                res = json.loads(requests.put(settings.DIRECCION_SERVER + 'api/procedimientos/%s' % id , json={"nombre": nombre,"totalActividades" : actividades,"idUsuario": request.user.id}, headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content)
                status = res.get('status')
                mensaje = res.get('message')

                request.session['mensaje'] = mensaje

                if status:
                    return redirect("task_list")
                else:
                    return render(request, "core/task_update.html", {"id": id, "nombre": nombre, "actividades": actividades, "mensaje": mensaje})
        else:
            return redirect("logout")
    else:
            return redirect("logout")


def task_delete(request, id):
    
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))
    if status:
        if request.user.is_authenticated:

            res = json.loads(requests.delete(settings.DIRECCION_SERVER + 'api/procedimientos/%s' % id , headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content)
            status = res.get('status')
            mensaje = res.get('message')

            request.session['mensaje'] = mensaje

            return redirect("task_list")
            
        else:
            return redirect("logout")
    else:
            return redirect("logout")


def activity_add(request):
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))
    if status:
        if request.user.is_authenticated:

            res = json.loads(
                    requests.get(settings.DIRECCION_SERVER + 'api/procedimientos/'+ str(request.user.id), headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content
            )

            
            status = res.get('status')
            mensaje_ = res.get('message')
            procedimientos = res.get('procedimientos')

            if procedimientos:
                frame = pd.DataFrame.from_records(procedimientos)
                frameTitle = frame.columns[:]
                frameTitle = list(tuple(frameTitle.to_numpy()))

            else:
                frameTitle = ["No hay datos para mostrar"]
                frame = [] 

            if request.method == "POST":
                nombre = request.POST.get('txtNombre')
                descripcion = request.POST.get('txtDescripcion')
                fechaIn = request.POST.get('txtFechaIn')
                dias = request.POST.get('txtDias')
                fechaFin = request.POST.get('txtFechaFin')
                jerarquia = request.POST.get('txtJerarquia')
                task = request.POST.get('cmbTask_list')
                
                res = json.loads(requests.post(settings.DIRECCION_SERVER + 'api/actividades/', json={"nombre": nombre, "descripcion": descripcion, "fechaInicio": fechaIn, "dias": dias,"fechaFin":fechaFin, "jerarquia": jerarquia, "valor": 0, "idProcedimiento": task}, headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content)
            
                status = res.get('status')
                mensaje = res.get('message')

                

                if status:
                    return render(request, "core/activity_add.html", {'frameTareas': frame, "mensaje": mensaje, "status": 'success', "fechaIn": datetime.now().strftime("%Y-%m-%d")} )
                else:
                    return render(request, "core/activity_add.html", {'frameTareas': frame, "mensaje": mensaje, "status": 'error', "fechaIn": datetime.now().strftime("%Y-%m-%d")} )
            else:


                return render(request, "core/activity_add.html", {'frameTareas': frame, "fechaIn": datetime.now().strftime("%Y-%m-%d")})
        else:
            return redirect("logout")
    else:
            return redirect("logout")

def activity_list(request):
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))

    if status:
        if request.user.is_authenticated:

            res = json.loads(
                requests.get(settings.DIRECCION_SERVER + 'api/actividades/'+ str(request.user.id), headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content
            )

            
            status = res.get('status')
            mensaje = res.get('message')
            actividades = res.get('actividades')
        
            if actividades:
                frame = pd.DataFrame.from_records(actividades)
                frameTitle = frame.columns[:]
                frameTitle = list(tuple(frameTitle.to_numpy()))

                
            else:
                frameTitle = ["No hay datos para mostrar"]
                frame = [] 

            mensaje = request.session.get('mensaje')

            if mensaje:
                request.session.pop('mensaje', "")

            return render(request,"core/activity_list.html", {"frameTitle": frameTitle, 'frame': frame, "mensaje":mensaje, "ruta":settings.DIRECCION_SERVER + 'api/actividades/completar/', "token": request.session.get('TOKEN')})
        else:
            return redirect("login")
    else:
            return redirect("login")

def activity_getbyid(request, id):
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))

    if status:
        if request.user.is_authenticated:
            res = json.loads(
                requests.get(settings.DIRECCION_SERVER + 'api/actividades/getbyid/%s' % id, headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content
            )

            status = res.get('status')
            mensaje = res.get('message')
            actividad = res.get('actividad')

            res = json.loads(
                requests.get(settings.DIRECCION_SERVER + 'api/procedimientos/'+ str(request.user.id), headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content
            )

            procedimientos = res.get("procedimientos")

            if procedimientos:
                frame = pd.DataFrame.from_records(procedimientos)
                frameTitle = frame.columns[:]
                frameTitle = list(tuple(frameTitle.to_numpy()))

                actividad['frameActividades'] = frame

            else:
                frameTitle = ["No hay datos para mostrar"]
                frame = [] 
            
            return render(request, "core/activity_update.html", actividad)

        else:
            return redirect("login")
    else:
            return redirect("login")

def activity_update(request, id):
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))
    if status:
        if request.user.is_authenticated:

            if request.method == "POST":
                nombre = request.POST.get('txtNombre')
                descripcion = request.POST.get('txtDescripcion')
                fechaIn = request.POST.get('txtFechaIn')
                dias = request.POST.get('txtDias')
                fechaFin = request.POST.get('txtFechaFin')
                jerarquia = request.POST.get('txtJerarquia')
                task = request.POST.get('cmbTask_list')
                
                res = json.loads(requests.put(settings.DIRECCION_SERVER + 'api/actividades/%s'% id, json={"nombre": nombre, "descripcion": descripcion, "fechaInicio": fechaIn, "dias": dias,"fechaFin":fechaFin, "jerarquia": jerarquia, "valor": 0, "idProcedimiento": task}, headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content)
            
                status = res.get('status')
                mensaje = res.get('message')
                request.session['mensaje'] = mensaje

                return redirect("activity_list")
                
            
        else:
            return redirect("logout")
    else:
            return redirect("logout")


def activity_delete(request, id):
    
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))
    if status:
        if request.user.is_authenticated:

            res = json.loads(requests.delete(settings.DIRECCION_SERVER + 'api/actividades/%s' % id , headers={'Authorization': "Token %s" % request.session.get('TOKEN')})._content)
            status = res.get('status')
            mensaje = res.get('message')

            request.session['mensaje'] = mensaje

            return redirect("activity_list")
            
        else:
            return redirect("logout")
    else:
            return redirect("logout")


def configuration(request):
    
    user,token,message,status = MyAuthentication().Autenticar(request.session.get('TOKEN'))
    if status:
        if request.user.is_authenticated:
            if request.method == "POST":

                password = request.POST.get('password')
                newPassword = request.POST.get('newPassword')

                res = json.loads(requests.put(settings.DIRECCION_SERVER + 'api/usuarios/'+ str(request.user.id ), json={"password": password ,"newPassword": newPassword}, headers={"Authorization": "Token %s" % request.session.get('TOKEN')})._content)
                
                status = res.get('status')
                mensaje = res.get('message')
                request.session['mensaje'] = mensaje

                if status:
                    return redirect("login")
                else:
                    return redirect("configuration")
            else:
                
                mensaje = request.session.get('mensaje')
                if mensaje:
                    request.session.pop('mensaje', "")

                return render(request, 'core/configuration.html', {'Nombre': request.user.first_name, 'Apellido': request.user.last_name, 'mensaje': mensaje})
        
        else:
            return redirect("logout")
    else:
            return redirect("logout")



    