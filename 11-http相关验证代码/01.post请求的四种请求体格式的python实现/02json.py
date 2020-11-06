import json
import requests
headers = {'Content-Type': 'application/json'}
datas = json.dumps({"param1": "Detector", "param2": "cnblogs"})
r = requests.post("http://httpbin.org/post", data=datas, headers=headers)
print(r.text)


'''
{
  "args": {},
  "data": "{\"param2\": \"cnblogs\", \"param1\": \"Detector\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "43",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.23.0",
    "X-Amzn-Trace-Id": "Root=1-5fa25e19-6674ce240c46845240b8ef29"
  },
  "json": {
    "param1": "Detector",
    "param2": "cnblogs"
  },
  "origin": "113.111.80.201",
  "url": "http://httpbin.org/post"
}

'''
