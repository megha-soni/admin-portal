from django.shortcuts import render,HttpResponseRedirect
#import all the models from our models.py file 
from .models import Organization,Department,Designation,GroupMaster,Modules,Permission
# import dateTime to show the correct date when data has been created
from django.utils.timezone import datetime


#-------------------------this view function is for Organization--------------------

# created 'OrganizationView' function just to display the Organization's UI where we will perform our CRUD operation
def OrganizationView(request):
    organization_data=Organization.objects.all()    
    return render(request,"app/organization.html",{"organization_data":organization_data})

# created 'Organization_entry' function that is used to create the fields/data to save in database 
def Organization_entry(request):
    if request.method=="POST":
        organization_name=request.POST.get("organization-name")
        organization_description=request.POST.get("organization-description")
        organization_email=request.POST.get("organization-email")
        organization_phoneNo=request.POST.get("organization-phone-number")
        organization_website=request.POST.get("organization-website")
        current_date=datetime.now()  
        organization_data=Organization(organization_name=organization_name,organization_description=organization_description,organization_email=organization_email,organization_phoneNo=organization_phoneNo,organization_website=organization_website,created=current_date)
        organization_data.save()
    organization_data=Organization.objects.all()    
    return render(request,"app/organization.html",{"organization_data":organization_data})

#  created 'Organization_update' function to update or edit that particular field/data through its respected id
def Organization_update(request,id):
    if request.method=="POST":
        organization_name=request.POST.get("organization-name")
        organization_description=request.POST.get("organization-description")
        organization_email=request.POST.get("organization-email")
        organization_phoneNo=request.POST.get("organization-phone-number")
        organization_website=request.POST.get("organization-website")
        current_date=datetime.now()  
        organization_data=Organization(id=id,organization_name=organization_name,organization_description=organization_description,organization_email=organization_email,organization_phoneNo=organization_phoneNo,organization_website=organization_website,created=current_date)
        organization_data.save()
        return HttpResponseRedirect("/")
    organization_data=Organization.objects.get(id=id)
    return render(request,'app/organization_update.html',{'organization_data':organization_data})

#  created 'Organization_delete' function to delete or remove that particular data through its respected id
def Organization_delete(request,id):
    organization_data_deleted=Organization.objects.get(id=id)
    organization_data_deleted.delete()
    return HttpResponseRedirect("/")


#-------------------------this view function is for Department--------------------

# created 'DepartmentView' function just to display the Department's UI where we will perform our CRUD operation
def DepartmentView(request):
    department_data=Department.objects.all()    
    return render(request,"app/department.html",{"department_data":department_data})

# created 'Department_entry' function that is used to create the fields/data to save in database 
def Department_entry(request):
    if request.method=="POST":
        department_name=request.POST.get("department-name")
        department_description=request.POST.get("description")
        current_date=datetime.now()
        if 'checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"    
        department_data=Department(department_name=department_name,department_description=department_description,status=status,created=current_date)
        department_data.save()
    department_data=Department.objects.all()    
    return render(request,"app/department.html",{"department_data":department_data})

#  created 'Department_update' function to update or edit that particular field/data through its respected id
def Department_update(request,id):
    if request.method=="POST":
        department_name=request.POST.get("department-name")
        department_description=request.POST.get("description")
        created_date=datetime.now()
        if 'checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"  
        department_data=Department(id=id,department_name=department_name,department_description=department_description,status=status,created=created_date)
        department_data.save()
        return HttpResponseRedirect("/department")
    department_data=Department.objects.get(id=id)
    return render(request,'app/department_update.html',{'department_data':department_data})

#  created 'Department_delete' function to delete or remove that particular data through its respected id
def Department_delete(request,id):
    deleted_data=Department.objects.get(id=id)
    deleted_data.delete()
    return HttpResponseRedirect("/department")


#---------------------this view function is for Designation-----------------

# created 'DesignationView' function just to display the Designation's UI where we will perform our CRUD operation
def DesignationView(request):
    designation_data=Designation.objects.all()    
    return render(request,"app/designation.html",{"designation_data":designation_data})


# created 'Designation_entry' function that is used to create the fields/data to save in database 
def Designation_entry(request):
    if request.method=="POST":
        designation_name=request.POST.get("designation-name")
        designation_description=request.POST.get("designation-description")
        current_date=datetime.now()
        if 'designation_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"    
        designation_data=Designation(designation_name=designation_name,designation_description=designation_description,designation_status=status,created=current_date)
        designation_data.save()
    designation_data=Designation.objects.all()    
    return render(request,"app/designation.html",{"designation_data":designation_data})


#  created 'Designation_update' function to update or edit that particular field/data through its respected id
def Designation_update(request,id):
    if request.method=="POST":
        designation_name=request.POST.get("designation-name")
        designation_description=request.POST.get("designation-description")
        current_date=datetime.now()
        if 'designation_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"  
        designation_data=Designation(id=id,designation_name=designation_name,designation_description=designation_description,designation_status=status,created=current_date)
        designation_data.save()
        return HttpResponseRedirect("/designation/")
    designation_data=Designation.objects.get(id=id)
    return render(request,'app/designation_update.html',{'designation_data':designation_data})

#  created 'Designation_delete' function to delete or remove that particular field/data through its respected id
def Designation_delete(request,id):
    designation_data_delete=Designation.objects.get(id=id)
    designation_data_delete.delete()
    return HttpResponseRedirect("/designation/")


#------------------------------this view function is for Group Master---------------------

# created 'GroupMasterView' function just to display the groupMaster's UI where we will perform our CRUD operation
def GroupMasterView(request):
    group_data=GroupMaster.objects.all()    
    return render(request,"app/groupMaster.html",{"group_data":group_data})

# created 'GroupMaster_entry' function that is used to create the fields/data to save in database 
def GroupMaster_entry(request):
    if request.method=="POST":
        group_name=request.POST.get("group-name")
        group_description=request.POST.get("group-description")
        current_date=datetime.now()
        if 'group_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"    
        group_data=GroupMaster(group_name=group_name,group_description=group_description,group_status=status,created=current_date)
        group_data.save()
    group_data=GroupMaster.objects.all()    
    return render(request,"app/groupMaster.html",{"group_data":group_data})


#  created 'Group_update' function to update or edit that particular field through its respected id
def Group_update(request,id):
    if request.method=="POST":
        group_name=request.POST.get("group-name")
        group_description=request.POST.get("group-description")
        current_date=datetime.now()
        if 'group_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"  
        group_data=GroupMaster(id=id,group_name=group_name,group_description=group_description,group_status=status,created=current_date)
        group_data.save()
        return HttpResponseRedirect("/groupmaster/")
    group_data=GroupMaster.objects.get(id=id)
    return render(request,'app/group_update.html',{'group_data':group_data})


#  created 'GroupMaster_delete' function to delete or remove that particular field/data through its respected id
def GroupMaster_delete(request,id):
    group_data_delete=GroupMaster.objects.get(id=id)
    group_data_delete.delete()
    return HttpResponseRedirect("/groupmaster/")



#-------------------------this view function is for Model------------------------------

# created 'ModuleView' function just to display the Model's UI where we will perform our CRUD operation
def ModuleView(request):
    module_data=Modules.objects.all()    
    return render(request,"app/module.html",{"module_data":module_data})


# created 'Module_entry' function that is used to create the fields/data to save in database 
def Module_entry(request):
    if request.method=="POST":
        module_name=request.POST.get("module-name")
        print(module_name)
        module_description=request.POST.get("module-description")
        print(module_description)
        current_date=datetime.now()
        if 'module_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"    
        module_data=Modules(module_name=module_name,module_description=module_description,module_status=status,created=current_date)
        module_data.save()
    module_data=Modules.objects.all()    
    return render(request,"app/module.html",{"module_data":module_data})

#  created 'Modules_update' function to update or edit that particular field/data through its respected id
def Modules_update(request,id):
    if request.method=="POST":
        module_name=request.POST.get("module-name")
        module_description=request.POST.get("module-description")
        current_date=datetime.now()
        if 'module_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"  
        module_data=Modules(id=id,module_name=module_name,module_description=module_description,module_status=status,created=current_date)
        module_data.save()
        return HttpResponseRedirect("/module/")
    module_data=Modules.objects.get(id=id)
    return render(request,'app/module_update.html',{'module_data':module_data})

#  created 'Modules_delete' function to delete or remove that particular data through its respected id
def Modules_delete(request,id):
    module_data_delete=Modules.objects.get(id=id)
    module_data_delete.delete()
    return HttpResponseRedirect("/module/")



#-------------------------------------this view function is for Permission----------------

# created 'PermissionView' function just to display the Permission's UI where we will perform our CRUD operation
def PermissionView(request):
    permission_data=Permission.objects.all()    
    return render(request,"app/permission.html",{"permission_data":permission_data})


# created 'Permission_entry' function that is used to create the fields/data to save in database 
def Permission_entry(request):
    if request.method=="POST":
        permission_name=request.POST.get("permission-name")
        permission_description=request.POST.get("permission-description")
        current_date=datetime.now()
        if 'permission_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"    
        permission_data=Permission(permission_name=permission_name,permission_description=permission_description,permission_status=status,created=current_date)
        permission_data.save()
    permission_data=Permission.objects.all()    
    return render(request,"app/permission.html",{"permission_data":permission_data})

#  created 'Permission_update' function to update or edit that particular field through its respected id
def Permission_update(request,id):
    if request.method=="POST":
        permission_name=request.POST.get("permission-name")
        permission_description=request.POST.get("permission-description")
        current_date=datetime.now()
        if 'permission_checkbox' in request.POST:
            status="Active"
        else:
            status="Inactive"  
        permission_data=Permission(id=id,permission_name=permission_name,permission_description=permission_description,permission_status=status,created=current_date)
        permission_data.save()
        return HttpResponseRedirect("/permission/")
    permission_data=Permission.objects.get(id=id)
    return render(request,'app/permission_update.html',{'permission_data':permission_data})

#  created 'Permission_update' function to delete or remove that particular data through its respected id
def Permission_delete(request,id):
    permission_data_deleted=Permission.objects.get(id=id)
    permission_data_deleted.delete()
    return HttpResponseRedirect("/permission/")


