from rest_framework.authentication import get_authorization_header
from .Auth import MyAuthentication
from django.http import JsonResponse


class Authentication(object):

    def get_user(self,request):
        token = get_authorization_header(request).split()

        if token:
            try:
                token = token[1].decode()
              
                # print(token)

            except:
                return None
            
            token_expire =  MyAuthentication()
            user,token,message,status = token_expire.Autenticar(token)
            # print("",message)
            if user!= None and token != None:
                return user
            
        return None

    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)
        if user is None:
            resp ={'message':"Vuelva iniciar sesión"}
            return JsonResponse(resp)
        return super().dispatch(request, *args, **kwargs)