from django.contrib import admin
#import the models from models.py from the application
from .models import Organization,Department,Designation,GroupMaster,Modules,Permission


#  registered all the models that have been imported from models file with the help of admin decorator
# specify the fields that I wanted to be displayed in the database table with the help of list_display 
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display=['id','organization_name','organization_description','organization_email','organization_phoneNo','organization_website','created','updated']  


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','department_name','department_description','status','created','updated']  


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display=['id','designation_name','designation_description','designation_status','created','updated'] 


@admin.register(GroupMaster)
class GroupMasterAdmin(admin.ModelAdmin):
    list_display=['id','group_name','group_description','group_status','created','updated'] 


@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    list_display=['id','module_name','module_description','module_status','created','updated'] 


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display=['id','permission_name','permission_description','permission_status','created','updated']    