from django.urls import path
from . import views #YA EXPORTO TODAS LAS VIEWS
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('alta_curso/<nombre>', views.alta_curso),
    path ('',views.inicio, name ="HOME"),
    path ("ver_cursos", views.ver_cursos, name="CURSOS"),
    path ("alumnos", views.alumnos, name="ALUMNOS"),
    path ("profesores", views.profesores, name="PROFESORES"),
    path('alta_curso', views.curso_formulario),
    path('buscar', views.buscar),
    path('buscar_curso', views.buscar_curso),
    path ('eliminar_curso/<int:id>', views.eliminar_curso, name= "eliminar_curso"),
    path ('editar_curso/<int:id>',views.editar_curso, name="editar_curso"),
    path('login', views.login_request, name="Login"),
    path("register", views.register , name="Register"),
    #
    path('alta_alumno/<nombre>', views.alta_alumno),
    path ("ver_alumno", views.ver_alumno, name="ALUMNOS"),
    path ('alta_alumno', views.alumno_formulario),
    path('buscar_alumno', views.buscar_alumno),
    path('buscar', views.buscar),
    path ('eliminar_alumno/<int:id>', views.eliminar_alumno, name= "eliminar_alumno"),
    path ('editar_alumno/<int:id>',views.editar_alumno, name="editar_alumno"),
    #
    path('alta_profesor/<nombre>', views.alta_profesor),
    path ("ver_profesor", views.ver_profesor, name="PROFESORES"),
    path('alta_profesor', views.profesores_formulario),
    path('buscar_profesores', views.buscar_profesores),  
    path ('buscar', views.buscar),
    path ('eliminar_profesor/<int:id>', views.eliminar_profesor, name= "eliminar_profesor"),
    path ('editar_profesor/<int:id>',views.editar_profesor, name="editar_profesor"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")
]
