from flask import Flask
import pymysql
pymysql.install_as_MySQLdb()
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template, request
from models import Feile
import platform, os
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@app.route('/')
def hello_world():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    data_type = request.args.get('type')
    if not page:
        page = 1
    else:
        page = int(page)
        if page <= 0:
            page = 1
    if not data_type:
        data_type = 1
    else:
        data_type = int(data_type)
    data_s = Feile.query.filter_by(type=int(data_type)).paginate(page, per_page=10, error_out=False)  # 根据条件查询数据
    data_list = []  # return数据list
    for data in data_s.items:
        data_list.append(data.to_dict())
    img = ''
    if data_type == 1:
        img = 'G.png'
    if data_type == 2:
        img = 'P.png'
    if data_type == 3:
        img = 't.png'
    if data_type == 4:
        img = 'ym.png'
    static_url = 'static/img/' + img
    return render_template('g1.html', **{'data': data_list,
                                            'page': page+1,
                                            'type': data_type,
                                            'img_url': static_url,
                                            'back_url': page-1})


@app.route('/g2')
def g2():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    data_type = request.args.get('type')
    if not page:
        page = 1
    else:
        page = int(page)
        if page <= 0:
            page = 1
    if not data_type:
        data_type = 2
    else:
        data_type = int(data_type)
    data_s = Feile.query.filter_by(type=int(data_type)).paginate(page, per_page=10, error_out=False)  # 根据条件查询数据
    data_list = []  # return数据list
    for data in data_s.items:
        data_list.append(data.to_dict())

    return render_template('g2.html', **{'data': data_list,
                                         'page': page+1,
                                            'type': data_type,
                                            'back_url': page-1})

@app.route('/g3')
def g3():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    data_type = request.args.get('type')
    if not page:
        page = 1
    else:
        page = int(page)
        if page <= 0:
            page = 1
    if not data_type:
        data_type = 3
    else:
        data_type = int(data_type)
    data_s = Feile.query.filter_by(type=int(data_type)).paginate(page, per_page=10, error_out=False)  # 根据条件查询数据
    data_list = []  # return数据list
    for data in data_s.items:
        data_list.append(data.to_dict())

    return render_template('g3.html', **{'data': data_list,
                                         'page': page+1,
                                            'type': data_type,
                                            'back_url': page-1})

@app.route('/g4')
def g4():
    page = request.args.get('page')
    per_page = request.args.get('per_page')
    data_type = request.args.get('type')
    if not page:
        page = 1
    else:
        page = int(page)
        if page <= 0:
            page = 1
    if not data_type:
        data_type = 4
    else:
        data_type = int(data_type)
    data_s = Feile.query.filter_by(type=int(data_type)).paginate(page, per_page=10, error_out=False)  # 根据条件查询数据
    data_list = []  # return数据list
    for data in data_s.items:
        data_list.append(data.to_dict())

    return render_template('g4.html', **{'data': data_list,
                                         'page': page+1,
                                            'type': data_type,
                                            'back_url': page-1})


# 数据库连接配置
if platform.system() == 'Windows':
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1:3306/feile"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = True
    db = SQLAlchemy(app, use_native_unicode='utf8')


if __name__ == '__main__':
    app.run()
