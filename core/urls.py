from django.urls import path
from core import views
urlpatterns = [
    path("",views.Home , name='home' ),
    path("add_student",views.Add_Student ,name="add_student"),
    path("delete_student/<int:id>" ,views.Delete_Student, name="delete_student" ),
    path("edit_student/<int:id>" , views.Edit_Student,name="edit_student"),
    path("register",views.Register,name="register"),
    path("login",views.Login,name="login"),
    path("logout" ,views.Logout , name="logout")
]