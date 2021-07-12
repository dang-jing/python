# -*_coding:utf8-*-
from urllib import request
import json
from werkzeug.routing import BaseConverter
from flask import Flask, render_template, Blueprint,request

# name寻找当前工程目录，传入的是模块的名字
app = Flask(__name__)
# 创建蓝图对象
user_bp = Blueprint('user', __name__)


@app.route('/index', methods=['GET', 'POST'])
def index(name=None):
    if request.method == 'GET':
        name = "WEB SERVER"
        return render_template('index.html', name=name)


@user_bp.route('/aa')
def a():
    return ''


# 定义视图
@app.route('/')
def hello_world():
    return 'Hello World!'

#   自定义转换器
class MobileConverter(BaseConverter):
    #      正则，1开头，数字在3-9，九个字符
    regex = r'1[3-9]\d{9}'

app.url_map.converters['mobile'] = MobileConverter

#转换器
# /user/123     默认string类型
# @app.route('/user/<user_id>')
@app.route('/user/<int:user_id>')
def get_user_data(user_id):
            #拿到传入的对应名值
    return user_id

# /articles?channel_id=123
@app.route('/articles')
def get_articles():
    get = request.args.get('channel_id')
    return get


# 注册蓝图
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == '__main__':

    try:
        # 运行调试服务器
        app.run(host='0.0.0.0', port=80, debug=False)
    except:
        pass
