import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# Create an object of ToastNotifier class
n = ToastNotifier()

# Define a function to fetch the data from the URL
def getdata(url):
    r = requests.get(url)
    return r.text

# Fetch the HTML data from the weather website for Delhi
htmldata = getdata("https://weather.com/en-IN/weather/today/l/28.61,77.23?par=google&temp=c/") 

# Parse the HTML data using BeautifulSoup
soup = BeautifulSoup(htmldata, 'html.parser')

# Extract the current temperature
current_temp = soup.find("span", class_="CurrentConditions--tempValue--MHmYY")
temp = current_temp.text if current_temp else "N/A"

# Extract the chance of rain
chances_rain = soup.find("div", class_="CurrentConditions--precipValue--2aJSf")
rain = chances_rain.text if chances_rain else "N/A"

# Prepare the result string
result = f"Current temperature: {temp} in Delhi\nChance of rain: {rain}"

# Show the weather update as a toast notification
n.show_toast("Live Weather Update", result, duration=10)
