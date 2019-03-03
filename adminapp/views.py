from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import smtplib
from django.conf import settings

# Create your views here.
def addbuliders(request):
    msg=""
    if request.method  == 'POST':
        name=request.POST.get('name')
        address=request.POST.get('address')   
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        quali=request.POST.get('quali')
        exp=request.POST.get('exp')
        image=request.FILES['image']
        pas=request.POST.get('pass')
        data=tbl_addbuilder.objects.create(add_name=name,add_address=address,add_email=email,add_phone=phone,add_image=image,add_exp=exp,add_quali=quali,add_pass=pas,add_approve='approve')
        data1=tbl_login.objects.create(log_user=email,log_pass=pas,log_type='architect')
        msg='Successfully Added'
    bldrdata=tbl_addbuilder.objects.all()
    return render(request,'adminapp/addbuliders.html',{'bldrdata':bldrdata,'msg':msg})
def bldrdelete(request,id):
    tb=tbl_addbuilder.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('addbuliders'))

def bldredit(request,id):
    
    detail=tbl_addbuilder.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        quali=request.POST.get('quali')
        exp=request.POST.get('exp')
        det=request.POST.get('img')
        if det=="on":
            image=request.FILES['image']
            detail.add_image=image
        detail.add_name=name
        detail.add_address=address
        detail.add_email=email
        detail.add_exp=exp
        detail.add_phone=phone
        detail.add_quali=quali
        detail.save()
        return HttpResponseRedirect(reverse('addbuliders'))
    return render(request,'adminapp/bldredit.html',{'detail':detail})



def index(request):
    return render(request,'adminapp/index.html',{})
def login(request):
    if request.method=='POST':
        username=request.POST.get('name')
        password=request.POST.get('pass')
        if tbl_login.objects.filter(log_user=username,log_pass=password):
            data=tbl_login.objects.get(log_user=username,log_pass=password)
            if data.log_type=="admin":
                request.session['adminid']=data.id
                return HttpResponseRedirect(reverse('index'))
            if data.log_type=="user":
                user=data.log_user
                upass=data.log_pass
                data2=tbl_userreg.objects.get(add_email=user,add_pas=upass)
                request.session['userid']=data2.id
                return HttpResponseRedirect(reverse('userindex'))
            if data.log_type=="architect":
                user=data.log_user
                upass=data.log_pass
                data2=tbl_addbuilder.objects.get(add_email=user,add_pass=upass)
                request.session['arhitectid']=data2.id
                return HttpResponseRedirect(reverse('architectindex'))
            if data.log_type=="company":
                user=data.log_user
                upass=data.log_pass
                data2=tbl_userreg.objects.get(add_email=user,add_pas=upass)
                request.session['compid']=data2.id
                return HttpResponseRedirect(reverse('compindex'))
        data="Invalid Username & Password"
        return render(request,'adminapp/login.html',{'data':data})
    return render(request,'adminapp/login.html',{})

                               
def addworks(request):
    msg=""
    if request.method == 'POST':
        name=request.POST.get('name')
        place=request.POST.get('place')
        prize=request.POST.get('prize')
        nearby=request.POST.get('nearby')
        sqrft=request.POST.get('sqrft')
        image=request.FILES['image']
        typ=request.POST.get('typ')
        des=request.POST.get('des')
        bedrooms=request.POST.get('bedrooms')
        toilet=request.POST.get('toilet')
        floor=request.POST.get('floor')
        data=tbl_addwork.objects.create(add_name=name,add_place=place,add_prize=prize,add_sqrft=sqrft,add_nearby=nearby,add_image=image,add_typ=typ,add_des=des,add_bedrooms=bedrooms,add_toilet=toilet,add_floor=floor)
        msg='Successfully Added'
    prprtdata=tbl_addwork.objects.all()
    return render(request,'adminapp/addworks.html',{'prprtdata':prprtdata,'msg':msg})
def workdelete(request,id):
    tb=tbl_addwork.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('addworks'))

def workedit(request,id):
    detail=tbl_addwork.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        place=request.POST.get('place')
        prize=request.POST.get('prize')
        nearby=request.POST.get('nearby')
        sqrft=request.POST.get('sqrft')
        typ=request.POST.get('typ')
        des=request.POST.get('des')
        det=request.POST.get('img')
        if det=="on":
            image=request.FILES['image']
            detail.add_image=image
        detail.add_name=name
        detail.add_place=place
        detail.add_prize=prize
        detail.add_nearby=nearby
        detail.add_sqrft=sqrft
        detail.add_typ=typ
        detail.add_des=des
        detail.save()
        return HttpResponseRedirect(reverse('addworks'))
    return render(request,'adminapp/workedit.html',{'detail':detail})
def viewusers(request):
    userdata=tbl_userreg.objects.all()
    return render(request,'adminapp/viewusers.html',{'userdata':userdata})
def userapprove(request,id):
    tb=tbl_userreg.objects.get(id=id)
    if tb.add_approve=="approve":
        mail=smtplib.SMTP('smtp.mailgun.org',587)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        message =  "username="+ tb.add_email + "\n" "password=" + tb.add_pas 
        email=tb.add_email
        mail.sendmail(settings.EMAIL_HOST_USER,email,message)
        tb.add_approve="Approved"
        tb.save()
    return HttpResponseRedirect(reverse('viewusers'))
def userdelete(request,id):
    tb=tbl_userreg.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('viewusers'))
def contactview(request):
    data=tbl_contact.objects.all()
    return render(request,'adminapp/contactview.html',{'data':data})
def builderapprove(request,id):
    tb=tbl_addbuilder.objects.get(id=id)
    if tb.add_approve=="approve":
        mail=smtplib.SMTP('smtp.mailgun.org',587)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        message =  "username="+ tb.add_email + "\n" "password=" + tb.add_pass 
        email=tb.add_email
        mail.sendmail(settings.EMAIL_HOST_USER,email,message)
        tb.add_approve="Approved"
        tb.save()
    return HttpResponseRedirect(reverse('addbuliders'))
def viewfeedback(request):
    feedbackdata=tbl_feedback.objects.all()
    return render(request,'adminapp/viewfeedback.html',{'feedbackdata':feedbackdata})
def viewreqrmnt(request):
    reqrmntdata=tbl_requirment.objects.all()
    data=tbl_userreg.objects.all()
    return render(request,'adminapp/viewreqrmnt.html',{'reqrmntdata':reqrmntdata,'data':data})
def indview(request,id):
    inddata=tbl_requirment.objects.get(id=id)
    userid=inddata.userid
    data=tbl_userreg.objects.get(id=userid)
    archdata=tbl_addbuilder.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        inddata.archid=name
        inddata.save()
        return HttpResponseRedirect(reverse('viewreqrmnt'))
    return render(request,'adminapp/indview.html',{'inddata':inddata,'data':data,'archdata':archdata})



def archreplay(request):
    userdata=tbl_userreg.objects.all()
    data=tbl_requirment.objects.all()
    return render(request,'adminapp/archreplay.html',{'data':data,'userdata':userdata}) 

def companyreplay(request):
    data=tbl_garden.objects.all()
    userdata=tbl_userreg.objects.all()
    msg=""
    return render(request,'adminapp/companyreplay.html',{'data':data,'msg':msg,'userdata':userdata})

def addcommision(request,id):
    data=tbl_garden.objects.get(id=id)
    cost=data.companycost
    totalcost=(int(cost)+(int(cost)*10/100))
    data.companycost=totalcost
    status="approved"
    data.status=status
    data.save()    
    return HttpResponseRedirect(reverse('companyreplay'))
def addcommision1(request,id):
    data=tbl_requirment.objects.get(id=id)
    cost=data.archcost
    totalcost=(int(cost)+(int(cost)*10/100))
    data.archcost=totalcost
    status="Commison Added"
    data.status=status
    data.save()    
    return HttpResponseRedirect(reverse('archreplay'))

def viewreq(request):
    wrkdata=tbl_addwork.objects.all()
    bookdata=tbl_booking.objects.all()
    userdata=tbl_userreg.objects.all()
    return render(request,'adminapp/viewreq.html',{'userdata':userdata,'bookdata':bookdata,'wrkdata':wrkdata})

def viewpayment(request):
    data=tbl_payment.objects.all()
    userdata=tbl_userreg.objects.all()
    return render(request,'adminapp/viewpayment.html',{'data':data,'userdata':userdata})

def workasgnmnt(request,id):
    inddata=tbl_payment.objects.get(id=id)
    userid=inddata.userid
    data=tbl_userreg.objects.get(id=userid)
    archdata=tbl_addbuilder.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        startdate=request.POST.get('strtdate')
        enddate=request.POST.get('enddate')
        status="Suuccesfully Assigned"
        inddata.status=status
        inddata.save()
        data2=tbl_wrkassgn.objects.create(archid=name,userid=userid,startdate=startdate,enddate=enddate)
        return HttpResponseRedirect(reverse('viewpayment'))
    return render(request,'adminapp/workasgnmnt.html',{'inddata':inddata,'data':data,'archdata':archdata})



