from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class MyAuthentication(TokenAuthentication):
    
    def validarToken(self,token):
        timeDif=timezone.now()-token.created
        leftTime = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - timeDif
        isExpire = leftTime < timedelta(seconds=0)

        return isExpire


    def Autenticar(self,key):
        message,token,user,status = None,None,None,None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user
            message = 'Contraseña actualizada'
            
            status = True
        except self.get_model().DoesNotExist:
            # raise AuthenticationFailed('Token invalido.')
            print("Token Invalido")
            message = 'Datos Incorrectos'
            return (user,token,message,status)
            

        if not token.user.is_active:
            # raise AuthenticationFailed('Usuario no activo o eliminado')
            message = 'Usuario no activo o eliminado'
            user = None
            status = False
           

        isExpired = self.validarToken(token)

        if isExpired:
            # raise AuthenticationFailed('Su token ha expirado')
            message = 'Su token ha expirado'
            user = None
            status = False
           

        return (user,token,message,status)
