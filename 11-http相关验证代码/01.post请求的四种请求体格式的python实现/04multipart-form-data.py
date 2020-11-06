import requests
files = {"file": open("./test.txt", "rb")}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)

'''
{
  "args": {},
  "data": "",
  "files": {
    "file": "1234\n6789\n"
  },
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "154",
    "Content-Type": "multipart/form-data; boundary=44dbc2f96dd8ad3b543e33755c539f97",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.23.0",
    "X-Amzn-Trace-Id": "Root=1-5fa26630-3daf61311a1b70a639705be0"
  },
  "json": null,
  "origin": "113.111.80.201",
  "url": "http://httpbin.org/post"
}

'''
