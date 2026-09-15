import requests

url = "https://sample.com"
data = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3",
}
files = {(None, None)}

r = requests.post(url=url, data=data, files=files)
print(f"{r.request.headers}")
