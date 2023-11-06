# defining all the models that has been used in my application
from django.db import models


# this model field defines the structure of Organization table in the database
class Organization(models.Model):
    organization_name=models.CharField(max_length=100)
    organization_description=models.CharField(max_length=1000)
    organization_email=models.EmailField(max_length=100)
    organization_phoneNo=models.IntegerField()
    organization_website=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

# this model field defines the structure of Department table in the database
class Department(models.Model):
    department_name=models.CharField(max_length=100)
    department_description=models.CharField(max_length=1000)
    status=models.CharField(max_length=20,default=True)
    created=models.DateTimeField(auto_now_add=True)  # it will help to set the exact time in which the record has been created
    updated=models.DateTimeField(auto_now=True)    # it will automatically update the date and time whenever record modified     

# this model field defines the structure of Designation table in the database
class Designation(models.Model):
    designation_name=models.CharField(max_length=100)
    designation_description=models.CharField(max_length=1000)
    designation_status=models.CharField(max_length=20,default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

# this model field defines the structure of GroupMaster table in the database
class GroupMaster(models.Model):
    group_name=models.CharField(max_length=100)
    group_description=models.CharField(max_length=1000)
    group_status=models.CharField(max_length=20,default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


# this model field defines the structure of Modules table in the database    
class Modules(models.Model):
    module_name=models.CharField(max_length=100)
    module_description=models.CharField(max_length=1000)
    module_status=models.CharField(max_length=20,default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

# this model field defines the structure of Permission table in the database
class Permission(models.Model):
    permission_name=models.CharField(max_length=100)
    permission_description=models.CharField(max_length=1000)
    permission_status=models.CharField(max_length=20,default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)