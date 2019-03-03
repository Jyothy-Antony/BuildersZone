from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.utils.formats import get_format
from django.utils.dateformat import DateFormat

def userindex(request):
    id=request.session["userid"]
    data=tbl_userreg.objects.get(id=id)
    return render(request,'userapp/userindex.html',{'data':data})
def userprofileedit(request,id):
    detail=tbl_userreg.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        pas=request.POST.get('pass')
        phone=request.POST.get('phone')
        place=request.POST.get('place')
        det=request.POST.get('img')
        if tbl_login.objects.filter(log_user=detail.add_email,log_pass=detail.add_pas):
            data1=tbl_login.objects.get(log_user=detail.add_email,log_pass=detail.add_pas)
            data1.log_user=email
            data1.log_pass=pas
            data1.save()
        if det=="on":
            image=request.FILES['image']
            detail.add_image=image    
        detail.add_name=name
        detail.add_address=address
        detail.add_email=email
        detail.add_pas=pas
        detail.add_phone=phone
        detail.add_place=place
        detail.save()
        return HttpResponseRedirect(reverse('userindex'))
    return render(request,'userapp/userprofileedit.html',{'detail':detail})

# def requirment(request):
#     msg=''
#     if request.method=='POST':
#         userid=request.session["userid"]
#         location=request.POST.get('location')
#         floor=request.POST.get('floor')
#         sqrft=request.POST.get('sqrft')
#         bedrooms=request.POST.get('bedroom')
#         bath=request.POST.get('bath')
#         kitchen=request.POST.get('kitchen')
#         staircase=request.POST.get('stair')
#         des=request.POST.get('des')
#         plot=request.FILES['plott']
#         plan=request.FILES['plann']
#         msg="Successfully added"
#         data=tbl_requirment.objects.create(des=des,location=location,floor=floor,sqrft=sqrft,bedrooms=bedrooms,baths=bath,kitchen=kitchen,staircase=staircase,plot=plot,plan=plan,userid=userid)
#     return render(request,'userapp/requirment.html',{'msg':msg})
def feedback(request):
    msg=''
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        data=tbl_feedback.objects.create(name=name,email=email,feedback=feedback)
        msg='Successfully Added'
    return render(request,'userapp/feedback.html',{'msg':msg})
# Create your views here.
def gardenrequirment(request,id):
    try:
        userid=request.session["userid"]
        if userid:
            compdata=tbl_userreg.objects.get(id=id)
            msg=''
            if request.method=='POST':
                
                userid=request.session["userid"]
                location=request.POST.get('location')
                des=request.POST.get('des')
                plot=request.FILES['plott']
                msg="Successfully added"   
                                           
                data=tbl_garden.objects.create(companyid=id,des=des,location=location,img=plot,userid=userid,status="waiting")
            return render(request,'userapp/gardenrequirment.html',{'msg':msg,'compdata':compdata})
    except:
        return HttpResponseRedirect(reverse('login'))


def comreplay(request):
    id=request.session["userid"]   
    if tbl_garden.objects.filter(userid=id):
        data=tbl_garden.objects.filter(userid=id)
        compdata=tbl_userreg.objects.all()
    return render(request, "userapp/comreplay.html", {'data':data,'compdata':compdata})

def comapprove(request,id):
    tb=tbl_garden.objects.get(id=id)
    tb.status="Accepted"
    tb.save()
    return HttpResponseRedirect(reverse('comreplay'))


def adreplay(request):
    id=request.session["userid"]   
    if tbl_requirment.objects.filter(userid=id):
        data=tbl_requirment.objects.filter(userid=id)
        archdata=tbl_addbuilder.objects.all()
    return render(request, "userapp/adreplay.html", {'data':data,'archdata':archdata})

def booking(request,id): 
    try:
        userid=request.session["userid"]
    except:
        return HttpResponseRedirect(reverse('login'))
    if userid:
        userdata=tbl_userreg.objects.get(id=userid)
        workdata=tbl_addwork.objects.get(id=id)
        msg=''
        if request.method=='POST':
            userid=request.session["userid"]
            date=request.POST.get("date")
            msg="Successfully added,Our team will contacts you"                                       
            data=tbl_booking.objects.create(workid=id,dateofbookng=date,userid=userid)
        return render(request,'userapp/booking.html',{'msg':msg,'userdata':userdata,'workdata':workdata})


def payment(request):
    try:
        myid=request.session['userid']
    except:
        return HttpResponseRedirect(reverse('login'))
    if myid:
        # item=tbshoping.objects.get(id=id)
        userdata=tbl_userreg.objects.get(id=myid)
        
        if request.method=="POST":
            # qty=request.POST.get('qty')
            cvv=request.POST.get('cvv')
            cardno=request.POST.get('cardNumber')
            if tbatm.objects.filter(cvv=cvv,Atmno=cardno):
                atmdetails=tbatm.objects.get(cvv=cvv,Atmno=cardno)
                # actaddress=request.POST.get('actaddress')
                month=request.POST.get('month')
                year1=request.POST.get('year')
                year=int(year1)
                price=int(1000)
                
                # total=request.POST.get('price')
                amt=atmdetails.amt
                yr=atmdetails.expy
                if int(atmdetails.amt)< int(price):
                    err="sorry...pls check your act balance"
                    return render(request,'userapp/payment.html',{'userdata':userdata,'err':err})
                dt = datetime.now()
                df = DateFormat(dt)
                date=df.format('d-m-Y')
                yo=df.format('Y')
                mo=df.format('m')
                y=int(yo)
                # quty=int(item.quty)-int(qty)
                # if quty<0:
                #     err="We have only " + item.quty + "left....sorry"
                #     return render(request,'app/buy.html',{'item':item,'userdata':userdata,'err':err})
                if year > int(yr):
                    err="Card Expired"
                    return render(request,'userapp/payment.html',{'userdata':userdata,'err':err})
                else:
                    pay=tbl_payment.objects.create(userid=myid,date=date,price=price,payment='done',status="Work Assignmnet")
                    atmdetails.amt=int(amt)-int(price)
                    atmdetails.save()
                    succ="Payment Successfully completed"
                    return render(request,'userapp/payment.html',{'succ':succ})
            else:
                err="Not a valid card number"
                return render(request,'userapp/payment.html',{'userdata':userdata,'err':err})
    return render(request,'userapp/payment.html',{'userdata':userdata})
def noti(request):
    id=request.session["userid"] 
    if tbl_wrkassgn.objects.filter(userid=id):
        data=tbl_wrkassgn.objects.get(userid=id)
        data1=data.archid
        archdata=tbl_addbuilder.objects.get(id=data1)
    return render(request, "userapp/noti.html", {'data':data,'archdata':archdata}) 

def suggestions(request):
    id=request.session["userid"] 
    userdata=tbl_userreg.objects.get(id=id)
    data1=tbl_addbuilder.objects.all()
    if request.method=='POST': 
        name=userdata.add_name
        sugg=request.POST.get('sugg')
        arch=request.POST.get('arch')
        data1.archid=arch
        data2=tbl_sugg.objects.create(userid=id,workid=arch,sugg=sugg)
    return render(request,'userapp/suggestions.html',{'userdata':userdata,'data1':data1})

def replay(request):
    id=request.session["userid"]   
    if tbl_sugg.objects.filter(userid=id):
        data=tbl_sugg.objects.filter(userid=id)
    return render(request, "userapp/replay.html", {'data':data})