from django.db import models

class tbl_login(models.Model):          
    log_user=models.CharField(max_length=100)
    log_pass=models.CharField(max_length=100)
    log_type=models.CharField(max_length=100)
   
class tbl_addwork(models.Model):
    add_name=models.CharField(max_length=100)
    add_place=models.CharField(max_length=100)
    add_prize=models.CharField(max_length=100)
    add_sqrft=models.CharField(max_length=100)
    add_typ=models.CharField(max_length=100)
    add_image=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True)
    add_nearby=models.CharField(max_length=100)
    add_des=models.CharField(max_length=10000)
    add_bedrooms=models.CharField(max_length=100)
    add_toilet=models.CharField(max_length=100)
    add_floor=models.CharField(max_length=100)

class tbl_userreg(models.Model):
    add_name=models.CharField(max_length=100)
    add_address=models.CharField(max_length=100)
    add_email=models.CharField(max_length=100)
    add_phone=models.CharField(max_length=100)
    add_place=models.CharField(max_length=100)
    add_approve=models.CharField(max_length=100)
    add_pas=models.CharField(max_length=100)
    add_lic=models.CharField(max_length=100)
    add_image=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True)
    add_type=models.CharField(max_length=100)
    add_desc=models.CharField(max_length=10000)

# Create your models here.
class tbl_addbuilder(models.Model):
    add_name=models.CharField(max_length=100)
    add_address=models.CharField(max_length=100)
    add_email=models.CharField(max_length=100)
    add_phone=models.CharField(max_length=100)
    add_exp=models.CharField(max_length=100)
    add_quali=models.CharField(max_length=100)
    add_pass=models.CharField(max_length=100)
    add_image=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True)
    add_approve=models.CharField(max_length=100)


class tbl_contact(models.Model):
    conSub=models.CharField(max_length=100)
    conName=models.CharField(max_length=100)
    conemail=models.CharField(max_length=100)
    conmsg=models.CharField(max_length=1000)


class tbl_feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    feedback=models.CharField(max_length=1000)

class tbl_addprofile(models.Model):
    companyid=models.IntegerField()
    features=models.CharField(max_length=10000)
    works=models.CharField(max_length=100)
    wrkimg=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True) 


class imagesupload(models.Model):
    reqid=models.IntegerField()
    imag=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True) 
    cost=models.CharField(max_length=100)


class tbl_garden(models.Model):
    des=models.CharField(max_length=1000)
    location=models.CharField(max_length=100)
    img=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True)
    userid=models.IntegerField()
    companyid=models.IntegerField() 
    companyimage=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True)
    companycost=models.CharField(max_length=100)
    msg=models.CharField(max_length=1000)
    status=models.CharField(max_length=100)

class tbl_requirment(models.Model):
    userid=models.IntegerField()
    location=models.CharField(max_length=100)
    floor=models.CharField(max_length=100)
    sqrft=models.CharField(max_length=100)
    bedrooms=models.CharField(max_length=100)
    baths=models.CharField(max_length=100)
    staircase=models.CharField(max_length=100)
    kitchen=models.CharField(max_length=100)
    plot=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True)
    plan=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True)
    des=models.CharField(max_length=100)
    archid=models.IntegerField()
    archplan=models.ImageField(upload_to='images/',verbose_name="file",null=True,blank=True) 
    archcost=models.CharField(max_length=100)
    status=models.CharField(max_length=100)



class tbl_booking(models.Model):
    userid=models.IntegerField()
    workid=models.IntegerField()
    dateofbookng=models.CharField(max_length=100)



class tbatm(models.Model):
    Atmno=models.CharField(max_length=14)
    amt=models.CharField(max_length=15)
    expm=models.CharField(max_length=2)
    expy=models.CharField(max_length=100)
    cvv=models.CharField(max_length=3)
    date=models.DateField()
    

class tbl_payment(models.Model):
    userid=models.IntegerField()
    workid=models.IntegerField()
    price=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    payment=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class tbl_sugg(models.Model):
    userid=models.IntegerField()
    workid=models.IntegerField()
    name=models.CharField(max_length=100)
    sugg=models.CharField(max_length=100)
    rply=models.CharField(max_length=100)

class tbl_wrkassgn(models.Model):
    userid=models.IntegerField()
    reqid=models.IntegerField()
    archid=models.IntegerField()
    startdate=models.CharField(max_length=100)
    enddate=models.CharField(max_length=100)