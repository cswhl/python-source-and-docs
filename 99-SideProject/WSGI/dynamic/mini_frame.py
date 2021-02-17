from functools import wraps
from pymysql import connect
import re
from urllib import parse

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
def index(ret):
    with open("./templates/index.html") as f:
        content = f.read()

    # 创建连接数据库
    connection = connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='stock_db',
        charset='utf8')

    with connection:
        with connection.cursor() as cs:
            cs.execute('select * from info;')
            stock_infos = cs.fetchall()

    tr_template = ''' <tr>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemIdVaule="%s">
            </th>
        </tr>
        '''
    rep_html = ''
    for line in stock_infos:
        rep_html += tr_template % (line[0],
                                   line[1],
                                   line[2],
                                   line[3],
                                   line[4],
                                   line[5],
                                   line[6],
                                   line[7],
                                   line[1],)

    content = re.sub(r"\{%content%\}", rep_html, content)
    return content


@route('/center.html')
def center(ret):
    with open("./templates/center.html") as f:
        content = f.read()

    # 创建连接数据库
    connection = connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='stock_db',
        charset='utf8')

    with connection:
        with connection.cursor() as cs:
            cs.execute(
                'select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i inner join focus as f on i.id=f.info_id;')
            stock_infos = cs.fetchall()

    tr_template = ''' <tr>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>%s</th>
            <th>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </th>
            <th>
                <input type="button" value="删除" id="toDel" name="toDel" systemIdVaule="%s">
            </th>
        </tr>
        '''

    rep_html = ''
    for line in stock_infos:
        rep_html += tr_template % (line[0],
                                   line[1],
                                   line[2],
                                   line[3],
                                   line[4],
                                   line[5],
                                   line[6],
                                   line[0],
                                   line[0],
                                   )

    content = re.sub(r"\{%content%\}", rep_html, content)
    return content


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    stock_code = ret.group(1)

    connection = connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='stock_db',
        charset='utf8')

    with connection:
        # 1 判断是否有这个股票
        with connection.cursor() as cs:
            sql = """select * from info where code=%s;"""
            cs.execute(sql, (stock_code,))
            if not cs.fetchone():
                return "this stock is'n exit, please select other else..."

        # 2 判断是否已经关注
        with connection.cursor() as cs:
            sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
            cs.execute(sql, (stock_code,))
            if cs.fetchone():
                return "already focus, please don't reapet..."

        # 3 关注股票
        with connection.cursor() as cs:
            sql = """insert into focus (info_id) select id from info where code=%s;"""
            cs.execute(sql, (stock_code,))
            connection.commit()

    return "focus success!"

@route(r"/del/(\d+)\.html")
def del_focus(ret):
    stock_code = ret.group(1)

    connection = connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='stock_db',
        charset='utf8')

    with connection:
        # 1 判断是否有这个股票
        with connection.cursor() as cs:
            sql = """select * from info where code=%s;"""
            cs.execute(sql, (stock_code,))
            if not cs.fetchone():
                return "this stock isn't exit, please select other else..."

        # 2 判断是否已经关注
        with connection.cursor() as cs:
            sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
            cs.execute(sql, (stock_code,))
            if not cs.fetchone():
                return "stock isn't focused, please don't cancle..."

        # 3 取消关注
        with connection.cursor() as cs:
            sql = """delete from focus where info_id = (select id from info where code=%s);"""
            cs.execute(sql, (stock_code,))
            connection.commit()

    return "cancle success!"

@route(r"/update/(\d+)\.html")
def show_update_page(ret):

    with open("./templates/update.html") as f:
        content = f.read()

    stock_code = ret.group(1)

    # 1 显示股票代码和信息
    connection = connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='stock_db',
        charset='utf8')

    with connection:
        # 1 获取股票信息
        with connection.cursor() as cs:
            sql = """select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code=%s;"""
            cs.execute(sql, (stock_code,))
            note_info = cs.fetchone()[0]

    content = re.sub(r"\{%code%\}", stock_code, content)
    content = re.sub(r"\{%note_info%\}", note_info, content)
    return content

@route(r"/update/(\d+)/(.*)\.html")
def update_focus(ret):
    stock_code = ret.group(1)
    note_info = ret.group(2)
    note_info = parse.unquote(note_info)

    connection = connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='stock_db',
        charset='utf8')

    with connection:
        # 1 获取股票信息
        with connection.cursor() as cs:
            sql = """update focus set note_info=%s where info_id=(select id from info where code=%s);"""
            cs.execute(sql, (note_info, stock_code))
            connection.commit()

    return "update success!"

def application(env, start_response):
    status = '200 ok'
    headers = [('Content-typ', 'text/html')]
    start_response(status, headers)

    file_name = env['path_info']
    try:
        for url, func in url_func_dict.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return f"请求url:{file_name} 没有对应的函数..."
    except KeyError:
        return '异常，file not found'
