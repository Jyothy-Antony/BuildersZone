from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import smtplib
from django.conf import settings
# Create your views here.
def compindex(request):
    id=request.session["compid"]
    data=tbl_userreg.objects.get(id=id)
    return render(request,'companyapp/compindex.html',{'data':data})

def companyedit(request,id):
    detail=tbl_userreg.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        pas=request.POST.get('pass')
        if tbl_login.objects.filter(log_user=detail.add_email,log_pass=detail.add_pass):
            data1=tbl_login.objects.get(log_user=detail.add_email,log_pass=detail.add_pass)
            data1.log_user=email
            data1.log_pass=pas
            data1.save()
        lic=request.POST.get('lic')
        det=request.POST.get('img')
        if det=="on":
            image=request.FILES['image']
            detail.add_image=image
        detail.add_pas=pas
        detail.add_name=name
        detail.add_address=address
        detail.add_email=email
        detail.add_phone=phone
        detail.add_lic=lic

        detail.save()
        return HttpResponseRedirect(reverse('compindex'))
    return render(request,'companyapp/companyedit.html',{'detail':detail})

def addprofile(request):
    msg=""
    id=request.session["compid"]
    if request.method=='POST':
        features=request.POST.get('features')
        works=request.POST.get('works')
        
        image=request.FILES['image']
        data=tbl_addprofile.objects.create(features=features,works=works,wrkimg=image,companyid=id)
        msg="Successfully Added"
    return render(request,'companyapp/addprofile.html',{'msg':msg})

def grdnreqview(request):
    id=request.session["compid"]   
    if tbl_garden.objects.filter(companyid=id):
        data=tbl_garden.objects.filter(companyid=id)
        userdata=tbl_userreg.objects.all()
    return render(request, "companyapp/grdnreqview.html", {'data':data,'userdata':userdata})

def reqindview(request,id):
    inddata=tbl_garden.objects.get(id=id)
    userid=inddata.userid
    data=tbl_userreg.objects.get(id=userid)
    if request.method=='POST':
        
        msg=request.POST.get('msg')
        img=request.FILES['image']
        cost=request.POST.get('cost')
        inddata.msg=msg
        inddata.companyimage=img
        inddata.companycost=cost
        inddata.save()
        return HttpResponseRedirect(reverse('grdnreqview'))
    return render(request,'companyapp/reqindview.html',{'inddata':inddata,'data':data})




