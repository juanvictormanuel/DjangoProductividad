from django.http import JsonResponse
from django.views import View
from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from ..helpers.TokenAuth import Authentication

import json

class AutenticationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
            jd = json.loads(request.body)
            # print(jd)
    
            login_serializer = ObtainAuthToken.serializer_class(data=jd,context={'request':request})        
            if login_serializer.is_valid():
                user=login_serializer.validated_data['user']
                if user.is_active:
                    token,created = Token.objects.get_or_create(user = user)
                    # print(user)
                    if created:
                        resp={'status':True,'message':"Accesso correcto",'token':token.key}
                        return JsonResponse(resp)

                    else:
                        token.delete()
                        token = Token.objects.create(user=user)
                        resp={'status':True,'message':"Accesso correcto",'token':token.key,'username':user.username}
                        return JsonResponse(resp)
                else:
                    resp={'status':False,'message':"Usuario no activo",'token':None,'username':None}
                    return JsonResponse(resp)

            else:
                resp={'status':False,'message':"Usuario no valido",'token':None,'username':None}
                return JsonResponse(resp)