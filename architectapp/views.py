from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse



def architectindex(request):
    id=request.session["arhitectid"]
    data=tbl_addbuilder.objects.get(id=id)
    return render(request,'architectapp/architectindex.html',{"data":data})
def architectedit(request,id):
    detail=tbl_addbuilder.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        quali=request.POST.get('quali')
        exp=request.POST.get('exp')
        det=request.POST.get('img')
        pas=request.POST.get('pass')
        if tbl_login.objects.filter(log_user=detail.add_email,log_pass=detail.add_pass):
            data1=tbl_login.objects.get(log_user=detail.add_email,log_pass=detail.add_pass)
            data1.log_user=email
            data1.log_pass=pas
            data1.save()
        if det=="on":
            image=request.FILES['image']
            detail.add_image=image
        detail.add_pass=pas    
        detail.add_name=name
        detail.add_address=address
        
        detail.add_email=email
        detail.add_phone=phone
        detail.add_quali=quali
        detail.add_exp=exp

        detail.save()
        return HttpResponseRedirect(reverse('architectindex'))
    return render(request,'architectapp/architectedit.html',{'detail':detail})


# Create your views here.
def planrequest(request,id):
    data=tbl_requirment.objects.get(id=id)
    userid=data.userid
    data1=tbl_userreg.objects.get(id=userid)
    if request.method=='POST':
        cost=request.POST.get('cost')
        img=request.FILES["files"]
        # for count, x in enumerate(request.FILES.getlist("files")):
        data.archcost=cost
        data.archplan=img
        data.save()
    return render(request,'architectapp/planrequest.html',{'data':data,'data1':data1})

def form(request):
    return render(request, "architectapp/form.html", {})

#def upload(request):
    #if request.method=="POST":
        #for count, x in enumerate(request.FILES.getlist("files")):
            #data=imagesupload.objects.create(imag=x)
        #return HttpResponse("File(s) uploaded!")
def requestview(request):
    id=request.session["arhitectid"]
    if tbl_requirment.objects.filter(archid=id):
        data=tbl_requirment.objects.filter(archid=id)
        
    return render(request, "architectapp/requestview.html", {'data':data})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('publicindex'))

def requestgardenview(request,id):
    data=tbl_garden.objects.filter(id=id)
    return render(request,'requestgardenview.html',{'data':data})

def wrkasgn(request):
    id=request.session["arhitectid"]
    if tbl_wrkassgn.objects.filter(archid=id):
        data=tbl_wrkassgn.objects.filter(archid=id)
    return render(request,'architectapp/wrkasgn.html',{'data':data})

def indwrkasgn(request,id):
    data=tbl_wrkassgn.objects.get(id=id)
    userid=data.userid
    data1=tbl_userreg.objects.get(id=userid)
    return render(request,'architectapp/indwrkasgn.html',{'data':data,'data1':data1})


def suggview(request):
    id=request.session["arhitectid"]
    if tbl_sugg.objects.filter(workid=id):
        data=tbl_sugg.objects.filter(workid=id)
        data1=tbl_userreg.objects.all()
    return render(request, "architectapp/suggview.html", {'data':data,'data1':data1})

def Replay(request,id):
    data=tbl_sugg.objects.get(id=id)
    userid=data.userid
    data1=tbl_userreg.objects.get(id=userid)
    if request.method=='POST':
        replay=request.POST.get('rply')
        # img=request.FILES["files"]
        # for count, x in enumerate(request.FILES.getlist("files")):
        data.rply=replay
        # data.archplan=img
        data.save()
    return render(request,'architectapp/Replay.html',{'data':data,'data1':data1})