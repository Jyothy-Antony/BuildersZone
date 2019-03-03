from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def publicindex(request):
    data=tbl_addwork.objects.filter(add_typ='house')
    flat=tbl_addwork.objects.filter(add_typ='flat')
    companydata=tbl_userreg.objects.filter(add_type='company')
    return render(request,'publicapp/publicindex.html',{'data':data,'flat':flat,'companydata':companydata})
def about(request):
    return render(request,'publicapp/about.html',{})
def register(request):  
    msg=""
    if request.method == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        if tbl_login.objects.filter(log_user=email):
            error="Please choose another emailid"
            return render(request,'publicapp/register.html',{'error':error})
        phone=request.POST.get('phone')
        place=request.POST.get('place')
        image=request.FILES['image']
        pas=request.POST.get('pas')
        msg="Please Check your Email & Confirm your registration!"
        data=tbl_userreg.objects.create(add_name=name,add_address=address,add_email=email,add_phone=phone,add_image=image,add_place=place,add_pas=pas,add_approve="approve",add_type="user")
        data1=tbl_login.objects.create(log_user=email,log_pass=pas,log_type='user')   
    return render(request,'publicapp/register.html',{'msg':msg})
def comregister(request):  
    msg=""
    if request.method == 'POST':
        com_name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        if tbl_login.objects.filter(log_user=email):
            error="Please choose another emailid"
            return render(request,'publicapp/register.html',{'error':error})
        phone=request.POST.get('phone')
        place=request.POST.get('place')
        image=request.FILES['image']
        desc=request.POST.get('desc')
        pas=request.POST.get('pas')
        com_lic=request.POST.get('lic')
        msg="Please Check your Email & Confirm your registration!"
        data=tbl_userreg.objects.create(add_name=com_name,add_address=address,add_email=email,add_phone=phone,add_image=image,add_place=place,add_pas=pas,add_approve="approve",add_lic=com_lic,add_type="company",add_desc=desc)
        data1=tbl_login.objects.create(log_user=email,log_pass=pas,log_type='company')   
    return render(request,'publicapp/comregister.html',{'msg': msg})
def contact(request):
    msge=""
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        msg=request.POST.get('msg')
        data=tbl_contact.objects.create(conName=name,conemail=email,conSub=subject,conmsg=msg)
        msge="Successfully Added"
    return render(request,'publicapp/contact.html',{'msge':msge})
def aboutus(request):
    return render(request,'publicapp/aboutus.html',{})

def indgallery(request,id):
    inddata=tbl_userreg.objects.get(id=id)
    profiledata=""
    
    if tbl_addprofile.objects.filter(companyid=id):
        profiledata=tbl_addprofile.objects.filter(companyid=id)
    #if request.session["userid"]:
        #return HttpResponseRedirect(reverse('gardenrequirment'))
    #else:
        #return HttpResponseRedirect(reverse('login'))
    return render(request,'publicapp/indgallery.html',{'inddata':inddata,'profiledata':profiledata})

def homegallery(request):
    home=tbl_addwork.objects.filter(add_typ='house')
    return render(request,'publicapp/homegallery.html',{'home':home})

def flatgallery(request):
    flat=tbl_addwork.objects.filter(add_typ='shope')
    return render(request,'publicapp/flatgallery.html',{'flat':flat})

def companygallery(request):
    companydata=tbl_userreg.objects.filter(add_type='company')
    
    return render(request,'publicapp/companygallery.html',{'companydata':companydata})
def indhomegallery(request,id):
    gallerydata=tbl_addwork.objects.get(id=id)
    return render(request,'publicapp/indhomegallery.html',{'gallerydata':gallerydata})



def requirment1(request):
    try:
        userid=request.session["userid"]
    except:
        return HttpResponseRedirect(reverse('login'))
    if userid:
        msg=''
        if request.method=='POST':
            userid=request.session["userid"]
            location=request.POST.get('location')
            floor=request.POST.get('floor')
            sqrft=request.POST.get('sqrft')
            bedrooms=request.POST.get('bedroom')
            bath=request.POST.get('bath')
            kitchen=request.POST.get('kitchen')
            staircase=request.POST.get('stair')
            des=request.POST.get('des')
            plot=request.FILES['plott']
            plan=request.FILES['plann']
            msg="Successfully added"
            data=tbl_requirment.objects.create(des=des,location=location,floor=floor,sqrft=sqrft,bedrooms=bedrooms,baths=bath,kitchen=kitchen,staircase=staircase,plot=plot,plan=plan,userid=userid)
    return render(request,'publicapp/requirment1.html',{'msg':msg})

