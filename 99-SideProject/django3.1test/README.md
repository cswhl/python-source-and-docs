1、运行angular前端应用
```
cd angular11-frontEnd
npm run start
```

2、运行django应用
```
workon django3.1
cd djangoAPI
python manage.py runserver 0.0.0.0:8000
```

3、阿里云部署:
修改angular的package.json:
```
"start": "ng serve --port=8889 --host=0.0.0.0",
```
运行angular应用:
```
npm run start
```

