from django.shortcuts import render
from django.http import HttpResponse
from.models import  SportsData,CustomerData
from .forms import CustomerForm


def sportsview(request):
    sdata=SportsData.objects.all()
    return render(request, 'sports.html',{'sdata':sdata})


def apply_form(request):
    if request.method == 'POST':
        aform = CustomerForm(request.POST)
        if aform.is_valid():
            name = request.POST.get('name')
            adress = request.POST.get('adress')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            gender = request.POST.get('gender')
            sports = aform.cleaned_data.get('sports')
            data_of_joining = aform.cleaned_data.get('data_of_joining')

            data = CustomerData(
                name = name,
                adress = adress,
                mobile = mobile,
                email = email,
                gender = gender,
                sports = sports,
                data_of_joining = data_of_joining

            )
            data.save()

            aform = CustomerForm()
            return render(request,'apply.html',{'aform':aform})
        else:
            return HttpResponse('User invalid Data')
    else:
        aform = CustomerForm()
        return render(request,'apply.html',{'aform':aform})
