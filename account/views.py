from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.view
from account.models import Dashboard
from django.contrib import messages

# Create your views here.
#def login_view(request,*args, **kwargs):


#def dashboard(request):
 #   context = {}
  #  return render(request, "dashboard.html", context)
@login_required
def show(request): 
  if request.method=="POST":
    fromdate = request.POST.get('fromdate')
    todate = request.POST.get('todate')
    searchresult = Dashboard.objects.raw('select * from collect where date between "'+fromdate+'" and "'+todate+'"')
    return render(request,"dashboard.html",{'Dashboard':searchresult})
  else:
    #if request.method=="POST"
    resultsdisplay=Dashboard.objects.order_by("-id")
    return render(request,"dashboard.html",{'Dashboard':resultsdisplay})

def map(request):
  return render(request,"new3.html")

def sort(request,val):
  if val==1:
    resultsdisplay=Dashboard.objects.order_by("-lod")
    return render(request,"dashboard.html",{'Dashboard':resultsdisplay})
  elif val==2:
    resultsdisplay=Dashboard.objects.order_by("-date")
    return render(request,"dashboard.html",{'Dashboard':resultsdisplay})
  else:
    resultsdisplay=Dashboard.objects.order_by("-id")
    return render(request,"dashboard.html",{'Dashboard':resultsdisplay})

def filter(request):
  result=Dashboard.objects.filter(status="accepted")
  return render(request,"dashboard.html",{'Dashboard':result})








