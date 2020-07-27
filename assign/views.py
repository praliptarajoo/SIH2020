from django.shortcuts import render,HttpResponse,redirect
from backend.models import newcontract
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail 
from django.conf import settings
from account.models import Dashboard 
from assign.models import assignwork


from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.
def assignment(request,getdata_id):
    #contrecord=newcontract.objects.filter(id=1)
    contrecord=newcontract.objects.all()
    count=len(contrecord)
    newrecord=Dashboard.objects.filter(id=getdata_id)
    for i in range(count):
        assignrecord=assignwork(cemail=contrecord[i].cemail,
            adate=newrecord[0].date,
            alat=newrecord[0].lat,
            alon=newrecord[0].lon,
            anear=newrecord[0].near,
            aurl=newrecord[0].url,
            alod=3,
            aoption=1,
            astatus=1)
        assignrecord.save()
    return render(request,"message.html") 

def interest(request):
    record=assignwork.objects.filter(aoption=0)
    record.delete()
    result=assignwork.objects.all()
    return render(request,"show_int.html",{'assignwork':result})
   



    