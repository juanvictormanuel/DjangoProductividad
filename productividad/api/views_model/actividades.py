import imp
from unittest import result
from django.http import JsonResponse
from django.views import View
from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from ..helpers.TokenAuth import Authentication
from ..dal.data_access import DataAcess
from ..helpers.Auth import MyAuthentication
from rest_framework.authentication import get_authorization_header

import json

class ActividadesView(Authentication,View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
            jd = json.loads(request.body)
         
            try:
                nombre,descripcion,fechaInicio,dias,fechaFin,jerarquia,valor,idProcedimiento = jd

                
            
            except:
                  resp ={'status':False,'message':"Peticion Invalida"}
                  return JsonResponse(resp)
            
            #print(jd)
            result = DataAcess.Excute("call stp_actividades_add(%s,%s,%s,%s,%s,%s,%s,%s)",(jd['nombre'],jd['descripcion'],jd['fechaInicio'],jd['dias'],jd['fechaFin'],jd['jerarquia'],jd['valor'],jd['idProcedimiento']))
            

            if result:
               
                resp ={'status':True,'message':"Actividad almacenada"}
            else:
              
                resp ={'status':False,'message':"Error al agregar"}

            return JsonResponse(resp)



    def get(self, request,id=0):

            if id >0:

                result = DataAcess.Query("CALL stp_actividades_getall(%s)",(id,))
                if result:
                 resp ={'status':True,'message':"Consulta exitosa",'actividades':result}
                else:
                    resp ={'status':False,'message':"Error al consultar",'actividades':[]}
              
            else:
                 resp ={'status':False,'message':"Ingrese un id",'actividades':[]}
            

            return JsonResponse(resp)



    def put(self,request,id):
        jd = json.loads(request.body)
      
    
        try:
            nombre,descripcion,fechaInicio,dias,fechaFin,jerarquia,valor,idProcedimiento = jd

                
            
        except:
            resp ={'status':False,'message':"Peticion Invalida"}
            return JsonResponse(resp)



        result = DataAcess.Excute("call stp_actividades_update(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,jd['nombre'],jd['descripcion'],jd['fechaInicio'],jd['dias'],jd['fechaFin'],jd['jerarquia'],jd['valor'],jd['idProcedimiento']))
            
        if result:

            list =  DataAcess.QuerySingle("call stp_actividades_getbyid(%s)",(id,))
            resp ={'status':True,'message':"Actualizado",'actividad':list}
        else:
            list =  DataAcess.QuerySingle("call stp_actividades_getbyid(%s)",(id,))
            resp ={'status':False,'message':"Error al actualizar",'actividad':list}

        return JsonResponse(resp)


    def delete(self,request,id):

        result = DataAcess.Excute("call stp_actividades_delete(%s)",(id,))
            
        if result>0:

          
            resp ={'status':True,'message':"Eliminado"}
        else:
           
            resp ={'status':False,'message':"Error al eliminar"}

        return JsonResponse(resp)


    @method_decorator(csrf_exempt)
    def getbyid(request,id=0):

        token = get_authorization_header(request).split()

        if token:
            try:
                token = token[1].decode()
              
                # print(token)

            except:
                resp ={'message':"Vuelva iniciar sesión"}
                return JsonResponse(resp)
            
            token_expire =  MyAuthentication()
            user,token,message,status = token_expire.Autenticar(token)
            # print("",message)


            if user!= None and token != None:
                if request.method == 'GET':

                    if id==0:
                    
                        resp ={'status':False,'message':"Peticion Invalida"}
                        return JsonResponse(resp)

                
                    list =  DataAcess.QuerySingle("call stp_actividades_getbyid(%s)",(id,))

                    if(list):
                        resp ={'status':True,'message':"Consulta exitosa",'actividad':list}
                        return JsonResponse(resp)
                    
                    else:
                        resp ={'status':False,'message':"Sin registro",'actividad':None}
                        return JsonResponse(resp)
                    
            else:
                    resp ={'message':"Vuelva iniciar sesión"}
                    return JsonResponse(resp) 
                    

                   
        else:
            resp ={'message':"Vuelva iniciar sesión"}
            return JsonResponse(resp) 


    @method_decorator(csrf_exempt)
    def completar(request,id=0):
       
        token = get_authorization_header(request).split()

        if token:
            try:
                token = token[1].decode()
              
                

            except:
                resp ={'message':"Vuelva iniciar sesión"}
                return JsonResponse(resp)
            
            token_expire =  MyAuthentication()
            user,token,message,status = token_expire.Autenticar(token)
            


            if user!= None and token != None:
                if request.method == 'GET':

                    if id==0:
                    
                        resp ={'status':False,'message':"Peticion Invalida"}
                        return JsonResponse(resp)

                
                    list =  DataAcess.Excute("call stp_actividades_completar(%s)",(id,))

                    if(list==1):
                        resp ={'status':True,'message':"Actualización exitosa"}
                        return JsonResponse(resp)
                    
                    else:
                        resp ={'status':False,'message':"Error al actualizar"}
                        return JsonResponse(resp)
                    

                    
            else:
                    resp ={'message':"Vuelva iniciar sesión"}
                    return JsonResponse(resp) 

                   
        else:
            resp ={'message':"Vuelva iniciar sesión"}
            return JsonResponse(resp) 


      
    @method_decorator(csrf_exempt)
    def getbyon(request,id=0):

        token = get_authorization_header(request).split()

        if token:
            try:
                token = token[1].decode()
              
                # print(token)

            except:
                resp ={'message':"Vuelva iniciar sesión"}
                return JsonResponse(resp)
            
            token_expire =  MyAuthentication()
            user,token,message,status = token_expire.Autenticar(token)
            # print("",message)


            if user!= None and token != None:
                if request.method == 'GET':

                    if id==0:
                    
                        resp ={'status':False,'message':"Peticion Invalida"}
                        return JsonResponse(resp)

                
                    list =  DataAcess.Query("call stp_actividades_getbyon(%s)",(id,))

                    if(list):
                        resp ={'status':True,'message':"Consulta exitosa",'actividades':list}
                        return JsonResponse(resp)
                    
                    else:
                        resp ={'status':False,'message':"Sin registro",'actividades':None}
                        return JsonResponse(resp)
                    

            else:
                    resp ={'message':"Vuelva iniciar sesión"}
                    return JsonResponse(resp)        

                   
        else:
            resp ={'message':"Vuelva iniciar sesión"}
            return JsonResponse(resp) 

        
    @method_decorator(csrf_exempt)
    def getbyon2(request,id=0):

        token = get_authorization_header(request).split()

        if token:
            try:
                token = token[1].decode()
              
                # print(token)

            except:
                resp ={'message':"Vuelva iniciar sesión"}
                return JsonResponse(resp)
            
            token_expire =  MyAuthentication()
            user,token,message,status = token_expire.Autenticar(token)
            # print("",message)


            if user!= None and token != None:
                if request.method == 'GET':

                    if id==0:
                    
                        resp ={'status':False,'message':"Peticion Invalida"}
                        return JsonResponse(resp)

                
                    list =  DataAcess.Query("call stp_actividades_getbyon2(%s)",(id,))

                    if(list):
                        resp ={'status':True,'message':"Consulta exitosa",'actividades':list}
                        return JsonResponse(resp)
                    
                    else:
                        resp ={'status':False,'message':"Sin registro",'actividades':None}
                        return JsonResponse(resp)
                    

            else:
                    resp ={'message':"Vuelva iniciar sesión"}
                    return JsonResponse(resp)        

                   
        else:
            resp ={'message':"Vuelva iniciar sesión"}
            return JsonResponse(resp) 

                        


                # dfFilter= result[result["Nombre"].isin(nombres)]
                
                # dfFilter =result[result.stack().str.contains('|'.join(nombres)).any(level=0)]

        
      