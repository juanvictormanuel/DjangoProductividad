from re import A
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..helpers.TokenAuth import Authentication
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

import json

class UsuariosView(Authentication,View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
            jd = json.loads(request.body)
         
            try:
                usuario,nombre,apellido,password,secreat = jd

                
            
            except:
                  resp ={'status':False,'message':"Peticion Invalida"}
                  return JsonResponse(resp)
            

            if jd['secret'] == "MYKQKSJRIOI1038":
                    

                #print(jd)
                instance = User()
                instance.username = jd['usuario']
                instance.first_name = jd['nombre']
                instance.last_name = jd['apellido']
                instance.set_password(jd['password'])
                #instance.is_staff = True

                instance.save()
                resp ={'status':True,'message':"Registro exitoso"}

                return JsonResponse(resp)

            else:
                resp ={'status':False,'message':"No pudes realizar esta accion"}
                return JsonResponse(resp) 



    def put(self,request,id):
        jd = json.loads(request.body)
      
    
        
         
        try:
           password,newPassword= jd

                
            
        except:
            resp ={'status':False,'message':"Peticion Invalida"}
            return JsonResponse(resp)

        



        user =User.objects.get(id=id)
        # print("usuario",user)
        # print("paaaaaaaaaaaaaas",user.password)

        if(user):

            if check_password(jd['password'],user.password):

                user.set_password(jd['newPassword'])
                user.save()
                resp ={'status':True,'message':"Contraseña Actulizada"}

                return JsonResponse(resp)


            else:
                  resp ={'status':False,'message':"Error de autenticacion"}

                  return JsonResponse(resp)


       

    
        
        resp ={'status':False,'message':"Error al actualizar"}

        return JsonResponse(resp)





        
                    


                # dfFilter= result[result["Nombre"].isin(nombres)]
                
                # dfFilter =result[result.stack().str.contains('|'.join(nombres)).any(level=0)]

        
      