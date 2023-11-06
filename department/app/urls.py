from django.urls import path
from app import views

urlpatterns=[
     # Organization section's urls
    path('',views.OrganizationView,name="organization"),
    path('organization_entry/',views.Organization_entry,name="organization_entry"),
    path('organization_update/<int:id>/',views.Organization_update,name="organization_update"),
    path('organization_delete/<int:id>/',views.Organization_delete,name="organization_delete"),

    # department section's urls
    path('department/',views.DepartmentView,name="department"),
    path('department_entry/',views.Department_entry,name="department_entry"),
    path('department_update/<int:id>/',views.Department_update,name="department_update"),
    path('department_delete/<int:id>/',views.Department_delete,name="department_delete"),


    # designation section's urls
    path('designation/',views.DesignationView,name="designation"),
    path('designation_entry/',views.Designation_entry,name="designation_entry"),
    path('designation_update/<int:id>/',views.Designation_update,name="designation_update"),
    path('designation_delete/<int:id>/',views.Designation_delete,name="designation_delete"),


    # GroupMaster section's urls
    path('groupmaster/',views.GroupMasterView,name="group_master"),
    path('group_entry/',views.GroupMaster_entry,name="group_entry"),
    path('groupmaster_update/<int:id>/',views.Group_update,name="groupmaster_update"),
    path('group_delete/<int:id>/',views.GroupMaster_delete,name="group_delete"),


    # Module section's urls
    path('module/',views.ModuleView,name="module"),
    path('module_entry/',views.Module_entry,name="module_entry"),
    path('module_update/<int:id>/',views.Modules_update,name="module_update"),
    path('module_delete/<int:id>/',views.Modules_delete,name="module_delete"),


    # Permission section's urls
    path('permission/',views.PermissionView,name="permission"),
    path('permission_entry/',views.Permission_entry,name="permission_entry"),
    path('permission_update/<int:id>/',views.Permission_update,name="permission_update"),
    path('permission_delete/<int:id>/',views.Permission_delete,name="permission_delete"),



]