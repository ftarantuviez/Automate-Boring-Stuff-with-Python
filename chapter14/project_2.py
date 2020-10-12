'''  

Checking the weather seems fairly trivial: Open your web browser, click the
address bar, type the URL to a weather website (or search for one and then
click the link), wait for the page to load, look past all the ads, and so on.
Actually, there are a lot of boring steps you could skip if you had a program that downloaded the weather forecast for the next few days and printed
it as plaintext. This program uses the requests module from Chapter 11 to
download data from the Web.
Overall, the program does the following:
•	 Reads the requested location from the command line.
•	 Downloads JSON weather data from OpenWeatherMap.org.
•	 Converts the string of JSON data to a Python data structure.
•	 Prints the weather for today and the next two days.
So the code will need to do the following:
•	 Join strings in sys.argv to get the location.
•	 Call requests.get() to download the weather data.
•	 Call json.loads() to convert the JSON data to a Python data structure.
•	 Print the weather forecast.

'''

#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json, requests, sys

def check_weather(location):
  # Download the JSON data from OpenWeatherMap.org's API.
  url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
  response = requests.get(url)
  response.raise_for_status()

  # Load JSON data into a Python variable.
  weatherData = json.loads(response.text)

  # Print weather description
  w = weatherData['list']
  print('Current weather in %s:' % (location))
  print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
  print()
  print('Tomorrow:')
  print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
  print()
  print('Day after tomorrow:')
  print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

if __name__ == "__main__":  
  if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
  location = ' '.join(sys.argv[1:])
  check_weather(location)