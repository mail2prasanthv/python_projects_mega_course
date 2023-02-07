# Converting json to python dictionary and parse various data point
import requests

pload = {'username':'Olivia','password':'123'}

response = requests.post('https://httpbin.org/post',data = pload)

jsonResponse = response.json();

print("Entire Response as Dictionary\n-------------\n", jsonResponse)

print("Contents of Form:",jsonResponse["form"])
print("Username inside form:",jsonResponse["form"]["username"])

