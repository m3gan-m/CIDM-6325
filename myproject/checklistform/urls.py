from django.urls import path
from . import views

urlpatterns = [
    path('studentform2/', views.checklistform, name='checklistform'),
    path('welcome/', views.checklistform, name='checklistform'),
    path('', views.welcome_view, name='welcome_view'),
    #path('form-example/', views.studentform, name='studentform'),
    #path("form-example/", form_example.views.form_example),
    #path('studentform/', studentform.views.studentform)
]