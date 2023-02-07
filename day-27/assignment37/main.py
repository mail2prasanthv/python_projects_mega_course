# Making get Request
import requests

r =requests.get('https://www.google.com')

print("Status Code: ",r.status_code)

print("Content-Type: ", r.headers['Content-Type'])
print("Entire Response\n-------------\n", r.text)