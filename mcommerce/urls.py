"""mcommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path
from adminapp.views import *
from publicapp.views import *
from userapp.views import *
from companyapp.views import *
from architectapp.views import *
from django.conf.urls import url 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^index/$',index,name='index'),
    url(r'^login/$',login,name='login'),
    url(r'^addworks/$',addworks,name='addworks'),
    url(r'^addbuliders/$',addbuliders,name='addbuliders'),
    url(r'^bldrdelete/(?P<id>\d+)',bldrdelete,name='bldrdelete'),
    url(r'^bldredit/(?P<id>[0-9]+)',bldredit,name='bldredit'),
    url(r'^viewusers/$',viewusers,name='viewusers'),
    url(r'^userdelete/(?P<id>\d+)',userdelete,name='userdelete'),
    url(r'^workdelete/(?P<id>\d+)',workdelete,name='workdelete'),
    url(r'^workedit/(?P<id>[0-9]+)',workedit,name='workedit'),
    url(r'^contactview/$',contactview,name='contactview'),
    url(r'^userapprove/(?P<id>\d+)',userapprove,name='userapprove'),
    url(r'^builderapprove/(?P<id>\d+)',builderapprove,name='builderapprove'),
     url(r'^viewfeedback/$',viewfeedback,name='viewfeedback'),
    url(r'^viewreqrmnt/',viewreqrmnt,name='viewreqrmnt'),
    url(r'^indview/(?P<id>[0-9]+)',indview,name='indview'),
    url(r'^archreplay/$',archreplay,name='archreplay'),
url(r'^companyreplay/$',companyreplay,name='companyreplay'),
url(r'^addcommision/(?P<id>[0-9]+)',addcommision,name='addcommision'),
url(r'^addcommision1/(?P<id>[0-9]+)',addcommision1,name='addcommision1'),
url(r'^viewreq/$',viewreq,name='viewreq'),
url(r'^viewpayment/$',viewpayment,name='viewpayment'),
url(r'^workasgnmnt/(?P<id>[0-9]+)',workasgnmnt,name='workasgnmnt'),

    url(r'^aboutus/$',aboutus,name='aboutus'),
    url(r'^$',publicindex,name='publicindex'),
    url(r'^register/$',register,name='register'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^comregister/$',comregister,name='comregister'),
    url(r'^homegallery/$',homegallery,name='homegallery'),
    url(r'^flatgallery/$',flatgallery,name='flatgallery'),
    url(r'^companygallery/$',companygallery,name='companygallery'),
    url(r'^grdnreqview/$',grdnreqview,name='grdnreqview'),
    
    url(r'^userindex/$',userindex,name='userindex'),
    url(r'^userprofileedit/(?P<id>[0-9]+)',userprofileedit,name='userprofileedit'),
    # url(r'^requirment/$',requirment,name='requirment'),
    url(r'^requirment1/$',requirment1,name='requirment1'),
     url(r'^feedback/$',feedback,name='feedback'),
     url(r'^gardenrequirment/(?P<id>[0-9]+)',gardenrequirment,name='gardenrequirment'),
     url(r'^comreplay/$',comreplay,name='comreplay'),
     url(r'^adreplay/$',adreplay,name='adreplay'),
url(r'^comapprove/(?P<id>\d+)',comapprove,name='comapprove'),
url(r'^booking/(?P<id>[0-9]+)',booking,name='booking'),
     url(r'^payment/',payment,name='payment'),
     url(r'^noti/$',noti,name='noti'),
     url(r'^suggestions/$',suggestions,name='suggestions'),
     url(r'^replay/$',replay,name='replay'),
url(r'^logout/$',logout,name='logout'),


    url(r'^architectindex/$',architectindex,name='architectindex'),
    url(r'^architectedit/(?P<id>[0-9]+)',architectedit,name='architectedit'),
    url(r'^planrequest/(?P<id>[0-9]+)',Replay,name='Replay'),
    url(r'^Replay/(?P<id>[0-9]+)',planrequest,name='planrequest'),
    url(r'^indgallery/(?P<id>[0-9]+)',indgallery,name='indgallery'),
    url(r'^indhomegallery/(?P<id>[0-9]+)',indhomegallery,name='indhomegallery'),
    #url(r'^upload',upload,name='upload'),
    url(r'^form/$',form,name='form'),
    url(r'^requestview/$',requestview,name='requestview'),
    url(r'^suggview/$',suggview,name='suggview'),
    url(r'^wrkasgn/$',wrkasgn,name='wrkasgn'),
    url(r'^indwrkasgn/(?P<id>[0-9]+)',indwrkasgn,name='indwrkasgn'),

    url(r'^compindex/$',compindex,name='compindex'),
    url(r'^companyedit/(?P<id>[0-9]+)',companyedit,name='companyedit'),
    url(r'^addprofile/$',addprofile,name='addprofile'),
    url(r'^reqindview/(?P<id>[0-9]+)',reqindview,name='reqindview'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
