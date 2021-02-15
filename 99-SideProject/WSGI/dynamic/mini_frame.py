from functools import wraps
from pymysql import connect
import re

url_func_dict = dict()


def route(url):
    def set_func(func):
        url_func_dict[url] = func
        @wraps(func)
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route('/index.html')
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    # 创建连接数据库
    conn = connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='stock_db',
        charset='utf8')
    print(conn)
    cs = conn.cursor()
    cs.execute('select * from info;')
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    tr_template = ''' <tr>
            <th>1</th>
            <th>000007</th>
            <th>全新好</th>
            <th>10.01%</th>
            <th>4.40%</th>
            <th>16.05</th>
            <th>14.60</th>
            <th>2021-02-16</th>
            <th>
            <input type='button" value="添加" id="toAdd" name="toAdd" systemidvalue="000007">
            </th>
        </tr>
        '''
    html = ''
    for line in stock_infos:
        html += tr_template

    content = re.sub(r"\{%content%\}", html, content)
    return content


@route('/center.html')
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    return content


def application(env, start_response):
    status = '200 ok'
    headers = [('Content-typ', 'text/html')]
    start_response(status, headers)

    file_name = env['path_info']
    try:
        return url_func_dict[file_name]()
    except KeyError:
        return '异常，file not found'
