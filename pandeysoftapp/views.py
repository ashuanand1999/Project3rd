from django.shortcuts import render
from .models import ContactData,FeedbackData
from .forms import ContactForm,FeddbackForm
from django.http.response import HttpResponse

def home(request):
    return render(request,'home.html')

def our_services(request):
    return render(request,'our_services.html')

def contact(request):
    if request.method=="POST":
        cform = ContactForm(request.POST)
        if cform.is_valid():
            fname = request.POST.get('firstname', '')
            lanme = request.POST.get('lastname', '')
            email = request.POST.get('email', '')
            mob = request.POST.get('mobile', '')
            cname = request.POST.get('cname', '')
            data = ContactData(
                firstname=fname,
                lastname=lanme,
                email=email,
                mobile=mob,
                cname=cname
            )
            data.save()
            cform = ContactForm()
            return render(request,'contact.html'),{'cform': cform}
        else:
            return HttpResponse('Invalid Form Please Fill All Data')

    else:
        cform = ContactForm()
        return render(request, 'contact.html'), {'cform': cform}

import datetime
Time = datetime.datetime.now()

def feedback(request):
    if request.method =="POST":
        ffrom = FeddbackForm(request.POST)
        if ffrom.is_valid():
            name = request.POST.get('name', '')
            rate = request.POST.get('rating', '')
            feedback = request.POST.get('feedback', '')

            name = name.capitalize()
            data = FeedbackData(
                name=name,
                rating=rate,
                feedback=feedback,
                time=Time
            )
            data.save()
            ffrom= FeedbackData()
            return render(request,'feedback.html', ''),{'fform': ffrom}
        else:
            return HttpResponse('Invalid Form Please Fill All Data')

    else:
        ffrom=FeedbackData()
        return render(request,'feedback.html',''),{'fform': ffrom}

def gallery(request):
    return render(request,'gallery.html',)




