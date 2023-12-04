from django.urls import path
from . import views
from django.views.generic import TemplateView
from project_admin.admin import admin_site
from . import views, api_views

urlpatterns = [
    path('studentform2/', views.checklistform, name='checklistform'),
    path('welcome/', views.checklistform, name='checklistform'),
    path('', views.welcome_view, name='welcome_view'),
    path("", TemplateView.as_view(template_name="index.html")),
    path("WTSTaff/<int:pk>/",views.publisher_edit, name="publisher_edit"),
    path("WTStaff/new/",views.publisher_edit, name="publisher_create"),
    path('admin/', admin_site.urls),
    path('api/first_api_view/', api_views.first_api_view),
    path('api/login', api_views.Login.as_view(), name=›login›),
    #path('form-example/', views.studentform, name='studentform'),
    #path("form-example/", form_example.views.form_example),
    #path('studentform/', studentform.views.studentform)
]

