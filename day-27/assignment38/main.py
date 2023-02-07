# Making post Request
import requests

pload = {'username':'Olivia','password':'123'}

r = requests.post('https://httpbin.org/post',data = pload)

print("Status Code: ",r.status_code)

print("Content-Type: ", r.headers['Content-Type'])
print("Entire Response\n-------------\n", r.text)