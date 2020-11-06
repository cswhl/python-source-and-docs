import requests
datas = {"param1": "Detector", "param2": "cnblogs"}
r = requests.post("http://httpbin.org/post", data=datas)
print(r.text)
print(r.status_code)

'''
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "param1": "Detector",
    "param2": "cnblogs"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "30",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.23.0",
    "X-Amzn-Trace-Id": "Root=1-5fa25d94-484215c61342edd81f5fb470"
  },
  "json": null,
  "origin": "113.111.80.201",
  "url": "http://httpbin.org/post"
}

200

'''
