import requests
headers = {"Content-Type": "text/xml"}
datas = """<?xml version="1.0"?>
<methodCall>
    <methodName>examples.getStateName</methodName>
    <params>
        <param>
            <value><i4>41</i4></value>
        </param>
    </params>
</methodCall>"""
r = requests.post("http://httpbin.org/post", data=datas, headers=headers)
print(r.text)

'''
{
  "args": {},
  "data": "<?xml version=\"1.0\"?>\n<methodCall>\n    <methodName>examples.getStateName</methodName>\n    <params>\n        <param>\n            <value><i4>41</i4></value>\n        </param>\n    </params>\n</methodCall>",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "198",
    "Content-Type": "text/xml",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.23.0",
    "X-Amzn-Trace-Id": "Root=1-5fa264d0-5327af4318ca22c71490c922"
  },
  "json": null,
  "origin": "113.111.80.201",
  "url": "http://httpbin.org/post"
}

'''
