from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def index_view(request):
    return render(request, 'bookingapp/homepage.html')

def booking_view(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        uname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        adhar = request.POST.get('adhar')
        date = request.POST.get('date')
        days = request.POST.get('days')
        status = request.POST.get('status')
        persons =request.POST.get('persons')
        rtype = request.POST.get('rtype')

        booking = Bookings(Name=uname,email_id=email,mobile=mobile,days=days,adhar_no=adhar,booking_date=date,status=status,no_of_persons=persons,room_type=rtype)
        booking.save()
        return redirect('/bookingsapp/display/')


    return render(request, 'bookingapp/bookingpage.html')


def display_view(request):
    data = Bookings.objects.all()
    context = {'data': data}
    return render(request, 'bookingapp/display.html', context)
    

def update_view(request, id):

    data = Bookings.objects.get(pk=id)
    context = {'data': data}

    if request.method == 'POST':
        uname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        adhar = request.POST.get('adhar')
        date = request.POST.get('date')
        days = request.POST.get('days')
        status = request.POST.get('status')
        persons =request.POST.get('persons')
        rtype = request.POST.get('rtype')

        # booking = Bookings(Name=uname,email_id=email,mobile=mobile,days=days,adhar_no=adhar,booking_date=date,status=status,no_of_persons=persons,room_type=rtype)
        
        data.Name = uname
        data.email_id = email
        data.mobile = mobile
        data.adhar_no = adhar
        data.booking_date = date
        data.status = status
        data.no_of_persons = persons
        data.days = days
        data.room_type = rtype
        data.save()

        return redirect('/bookingsapp/display/')


    return render(request, 'bookingapp/update.html', context)


def delete_view(request, id):
    data = Bookings.objects.get(pk=id)
    data.delete()
    return redirect('/bookingsapp/display/')
