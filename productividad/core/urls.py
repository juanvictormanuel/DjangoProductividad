
from unicodedata import name
from django.urls import path

from core import views as vcore


urlpatterns = [
    path('', vcore.home, name="home"),
    path('task_add/', vcore.task_add, name="task_add"),
    path('task_list/', vcore.task_list, name="task_list"),
    path('task_list/<int:id>/<str:nombre>/<int:actividades>', vcore.task_update ,name="task_update"),
    path('task_update/<int:id>', vcore.task_update_2 ,name="task_update_2"),
    path('task_delete/<int:id>', vcore.task_delete ,name="task_delete"),

    path('activity_add/', vcore.activity_add, name="activity_add"),
    path('activity_list/', vcore.activity_list, name="activity_list"),
    path('activity_list/<int:id>/', vcore.activity_getbyid, name="activity_getbyid"),
    path('activity_update/<int:id>/', vcore.activity_update, name="activity_update"),
    path('activity_delete/<int:id>/', vcore.activity_delete, name="activity_delete"),

    path('configuration/', vcore.configuration, name="configuration"),
]