from django.urls import path
from . import views

urlpatterns = [
    path('studentform/', views.studentform, name='studentform'),
    path('studentform/', views.studentform, name='form-example'),
    #path("form-example/", form_example.views.form_example),
    #path('studentform/', studentform.views.studentform)
]