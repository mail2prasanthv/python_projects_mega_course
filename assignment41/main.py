#building  new rest apis


from flask import Flask,request


app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

@app.post("/countries")
def addCountries():
    if request.is_json:
        requestjson = request.get_json()
        id = max(country["id"] for country in countries) + 1
        # //reading from the request
        name = requestjson["name"]
        capital = requestjson["capital"]
        area = requestjson["area"]
        # creating new dictionary
        country ={"id": id, "name": name, "capital": capital, "area": area}
        # adding item to list
        countries.append(country);
        return country, 201
    return {"error": "Request must be JSON"}, 415


@app.get("/countries")
def getCountries():
    return countries