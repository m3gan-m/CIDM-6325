from django.contrib import admin

# Register your models here.
class ProjectAdmin(admin.AdminSite):
    site_header = "WT Administration"
    admin_site = ProjectAdmin(name='project_admin')