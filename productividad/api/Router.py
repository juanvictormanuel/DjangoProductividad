from django.urls import path
from .views_model.Autenticacion import AutenticationView 
from .views_model.usuarios import UsuariosView 
from .views_model.procedimientos import ProcedimientosView
from .views_model.actividades import ActividadesView


urlpatterns = [
    path('auth/',AutenticationView.as_view(),name="categorias_list"),
    path('usuarios/',UsuariosView.as_view(),name="usuarios_list"),
    path('usuarios/<int:id>',UsuariosView.as_view(),name="usuarios_process"),
    path('procedimientos/',ProcedimientosView.as_view(),name="procedimientos_list"),
    path('procedimientos/<int:id>',ProcedimientosView.as_view(),name="procedimientos_process"),
    path('procedimientos/getbyid/<int:id>',ProcedimientosView.getbyid,name="procedimientos_func"),
    path('actividades/',ActividadesView.as_view(),name="actividades_list"),
    path('actividades/<int:id>',ActividadesView.as_view(),name="actividades_process"),
    path('actividades/getbyid/<int:id>',ActividadesView.getbyid,name="actividades_func"),
    path('actividades/getbyon/<int:id>',ActividadesView.getbyon,name="actividades_func_on"),
    path('actividades/getbyon2/<int:id>',ActividadesView.getbyon2,name="actividades_func_on2"),
    path('actividades/completar/<int:id>',ActividadesView.completar,name="actividades_func_comple"),
    ]