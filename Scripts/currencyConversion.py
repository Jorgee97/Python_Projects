import urllib.request, json

api_key_currency_layer = "852e2a704a89e1f31fc9f46eb446448e"

with urllib.request.urlopen("http://www.apilayer.net/api/live?access_key=852e2a704a89e1f31fc9f46eb446448e&format=1") as url:
    data = json.loads(url.read().decode())
    print(data)