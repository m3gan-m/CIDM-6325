from django.urls import path
from . import views

urlpatterns = [
    path('studentform1/', views.studentform, name='studentform'),
    #path('form-example/', views.studentform, name='studentform'),
    #path("form-example/", form_example.views.form_example),
    #path('studentform/', studentform.views.studentform)
]