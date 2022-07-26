import requests
jsonContent ={
        "Address" :{
            "street_address"  : "123 tester pl",
            "zipCode" : "66652",
            "state" : "TX",
            "city" :  "Austin",
        }
}


#response = requests.get("http://127.0.0.1:8000/api/")
response = requests.post("http://127.0.0.1:8000/api/", json=jsonContent)
print(response.content)
