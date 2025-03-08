from django.shortcuts import render, redirect
import requests
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def homepage(request):
    return render(request, 'homepage.html')

def search(request):
    return render(request, 'weather_search.html')

API_KEY = "266eb785a61dca80a994eb215d98dff9"

def fetching(latitude, longitude):
    FORECAST_API_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    CURRENT_API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    try:
        response1 = requests.get(FORECAST_API_URL)
        response2 = requests.get(CURRENT_API_URL)
        response1.raise_for_status() 
        response2.raise_for_status() 
        return {
            'forecast': response1.json(),
            'current': response2.json()
        }
    except requests.exceptions.RequestException:
        return None

def weather_data(request):
    city = request.GET.get('city')
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')
    date = request.GET.get('date')
    if city and latitude and longitude:
        data = fetching(latitude, longitude)
        if data:
            uniquedates = set()
            array = []
            today = datetime.now().strftime('%Y-%m-%d')
            weather_today = None
            for forecast in data['forecast']['list']:
                date_str = forecast['dt_txt'].split(' ')[0]
                if date and date_str == date and weather_today is None:
                    weather_today = forecast
                    weather_today['date'] = date_str
                elif date_str == today and weather_today is None:
                    weather_today = forecast
                    weather_today['date'] = date_str
                elif date_str != today and date_str not in uniquedates:
                    uniquedates.add(date_str)
                    forecast['date'] = date_str
                    array.append(forecast)
                    if len(array) == 5:
                        break
            current_data = data['current']
            sunrise = datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M')
            sunset = datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M')
            return render(request, 'weather_display.html', {'city': city,'latitude': latitude,'longitude': longitude,'today_forecast': weather_today,'weather_data': array,'sunrise': sunrise,'sunset': sunset})
        return redirect('search')
    return redirect('search')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('search')
        messages.error(request,'Invalid Credentials')
        return redirect('signin')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('homepage')

def signup(request):
    if request.method == "POST":
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        mail = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        data = User.objects.filter(username=username)
        if data:
            messages.error(request, "Please use a different User Name")
            context = {"fname":fname, "lname":lname, "email":mail, "username":username}
            return render(request,'signup.html',context)
        if password == cpassword:
            User.objects.create_superuser(first_name=fname,last_name=lname,email=mail,username=username,password=password)
            messages.success(request,"The Record Added Successfully")
            return redirect('signin')
        messages.error(request,"Password doesn't match with Confirm Password")
        context = {"fname":fname, "lname":lname, "email":mail, "username":username}
        return render(request,'signup.html',context)
    return render(request,'signup.html')
