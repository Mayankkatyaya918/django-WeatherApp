from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=67e63e56a0fd11f1d30950dbab591d00').read()
        json_data = json.loads(res)
        data = {
            "city": city,
            "country_code": str(json_data['sys']['country']),
            "coordinates" : str(json_data['coord']['lon']) + " " + str(json_data['coord']['lat']),
            "temp": str(int(json_data['main']['temp'])-273)+" c",
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data = {}
    return render(request, 'index.html', data)