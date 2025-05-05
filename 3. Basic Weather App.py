import requests
API_KEY="d67dc4ab9ae35592afaf4aad2771c576"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"
city=input("Enter city name: ")
params={'q':city,'appid':API_KEY,'units':'metric'}
try:
    response=requests.get(BASE_URL,params=params)
    response.raise_for_status()
    data=response.json()
    if data.get("cod")!=200:
        print("City not found.")
    else:
        temp=data['main']['temp']
        humidity=data['main']['humidity']
        description=data['weather'][0]['description']
        wind_speed=data['wind']['speed']
        print(f"Temperature: {temp}C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.title()}")
        print(f"Wind Speed: {wind_speed} m/s")
except requests.exceptions.RequestException as e:
    print("error fetching weather data: ",e)
