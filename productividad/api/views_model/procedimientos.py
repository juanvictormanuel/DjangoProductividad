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

class ProcedimientosView(Authentication,View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
            jd = json.loads(request.body)
         
            try:
                fecha,nombre,totalActividades,idUsuario = jd

                
            
            except:
                  resp ={'status':False,'message':"Peticion Invalida"}
                  return JsonResponse(resp)
            
            #print(jd)
            result = DataAcess.Excute("call stp_procedimientos_add(%s,%s,%s,%s)",(jd['fecha'],jd['nombre'],jd['totalActividades'],jd['idUsuario']))
            

            if result:
               
                resp ={'status':True,'message':"Proyecto creado",'idProcedimiento':result}
            else:
              
                resp ={'status':False,'message':"Error al agregar"}

            return JsonResponse(resp)



    def get(self, request,id=0):

            if id >0:

                result = DataAcess.Query("CALL stp_procedimientos_getall(%s)",(id,))
                if result:
                 resp ={'status':True,'message':"Consulta exitosa",'procedimientos':result}
                else:
                    resp ={'status':False,'message':"Error al consultar",'procedimientos':[]}
              
            else:
                 resp ={'status':False,'message':"Ingrese un id",'procedimientos':[]}
            

            return JsonResponse(resp)


    def put(self,request,id):
        jd = json.loads(request.body)
      
    
        try:
            nombre,totalActividades,idUsuario = jd

                
            
        except:
            resp ={'status':False,'message':"Peticion Invalida"}
            return JsonResponse(resp)



        result = DataAcess.Excute("call stp_procedimientos_update(%s,%s,%s,%s)",(id,jd['nombre'],jd['totalActividades'],jd['idUsuario']))
            
        if result:

            list =  DataAcess.QuerySingle("call stp_procedimientos_getbyid(%s)",(id,))
            resp ={'status':True,'message':"Actualizado",'procedimiento':list}
        else:
            list =  DataAcess.QuerySingle("call stp_procedimientos_getbyid(%s)",(id,))
            resp ={'status':False,'message':"Error al actualizar",'procedimiento':list}

        return JsonResponse(resp)


    def delete(self,request,id):
        
        result = DataAcess.Excute("call stp_procedimientos_delete(%s)",(id,))
            
        if result>0:

          
            resp ={'status':True,'message':"Eliminado"}
        else:
           
            resp ={'status':False,'message':"Error al eliminar"}

        return JsonResponse(resp)


    @method_decorator(csrf_exempt)
    def getbyid(request,id):

        token = get_authorization_header(request).split()

        if token:
            try:
                token = token[1].decode()
              
                # print(token)

            except:
                resp ={'message':"Vuelva iniciar sesión"}
                return JsonResponse(resp)
            
            token_expire =  MyAuthentication()
            user,token,message = token_expire.Autenticar(token)
            # print("",message)


            if user!= None and token != None:
                if request.method == 'POST':
                    jd = json.loads(request.body)

                    try:
                         nombre,codigo,cantidad,recio,color,material = jd
                        
                    except:
                        resp ={'status':False,'message':"Peticion Invalida"}
                        return JsonResponse(resp)

                
                    result =DataAcess.QueryPandasNoParams("call stp_hormas_getall()")
                   
                    

                    if not result.empty:

                        if jd['nombre']:
                            search = jd['nombre'].split(",")
                            result =result[result["Nombre"].str.contains('|'.join(search))]

                        if jd['codigo']:
                            search = jd['codigo'].split(",")
                            result =result[result["Codigo"].str.contains('|'.join(search))]

                        if jd['cantidad']:
                            result = result.astype({'Cantidad':str})
                            search = jd['cantidad'].split(",")
                            result =result[result["Cantidad"].isin(search)]
                            result = result.astype({'Cantidad':int})
                        
                        if jd['recio']:
                            search = jd['recio'].split(",")
                            result =result[result["Recio"].str.contains('|'.join(search))]

                        if jd['color']:
                            search = jd['color'].split(",")
                            result =result[result["Color"].str.contains('|'.join(search))]

                        if jd['material']:
                            search = jd['material'].split(",")
                            result =result[result["Material"].str.contains('|'.join(search))]


                        jsonResult = json.loads(result.to_json(orient="records"))

                        resp ={'status':True,'message':"Consulta exitosa",'marcas':jsonResult}
                        return JsonResponse(resp)

                    else:
                        resp ={'status':False,'message':"Error al consultar",'marcas':[]}

                        return JsonResponse(resp)
        else:
            resp ={'message':"Vuelva iniciar sesión"}
            return JsonResponse(resp) 

      

        
                    


                # dfFilter= result[result["Nombre"].isin(nombres)]
                
                # dfFilter =result[result.stack().str.contains('|'.join(nombres)).any(level=0)]

        
      