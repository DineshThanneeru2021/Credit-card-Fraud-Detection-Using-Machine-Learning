from django.shortcuts import render,redirect

# Create your views here.
from .credit_card import credit_card
#from .sms import send_sms
def login(request):
    if request.method=="POST":
        return redirect("input/")
    return render(request,"login.html")

def Input(request):
    if request.method=="POST":
        amount=int(request.POST["amount"])
        city=request.POST["city"]
        limit=100000
        p=credit_card(amount)
        if p[0]==0 and city=="Mylavaram" and amount<=limit and amount>0:
            #print(send_sms("The Transaction Amount of "+str(amount)+" is Successfull,"+city))
            return render(request,'success.html')
        else:
            #print(send_sms("The Transaction is Failed ,due to fraud "+" at city,"+city))
            return render(request,'fail.html')
    return render(request,"input.html")
