# -*_coding:utf8-*-

from urllib import request
import json
from werkzeug.routing import BaseConverter
from flask import Flask, render_template, Blueprint, request, jsonify, make_response, session,abort

# name寻找当前工程目录，传入的是模块的名字
app = Flask(__name__)
# 创建蓝图对象
user_bp = Blueprint('user', __name__)


# 模块响应
@app.route('/')
def home():
    mint = 123
    mstr = 'fgsdtg'
    data = dict(
        my_int=123,
        my_str='fgsdtg')
    # 根据网页变量名对应渲染
    # return render_template('index.html', my_str=mstr, my_int=mint)
    # return render_template('index.html', **data)
    return jsonify


#   设置cookie
@app.route('/cookie')
def set_cookie():
    response = make_response('hello cookie')
    #                   设置cooke的内容，还有存活时间s
    response.set_cookie('key', 'value', max_age=3600)
    # 获取cookie
    resp = request.cookies.get('key')
    # 删除cookie
    response.delete_cookie('key')
    return resp


#   配置文件设置
class defaultConfig(object):
    SECRET_KEY = 'asfs5ewtwe2'

app.config.from_object(defaultConfig)

# 直接设置
app.secret_key = 'sadfsfsd42ewtwe5'


#   设置session
@app.route('/set_session')
def set_session():
    #   写入session需要设置   SECRET_KEY
    session['username'] = 'aaaaaaa'
    #   读session
    username = session.get('username')
    #   快速返回页面错误
    if username is None:
        abort()
    return username

@app.errorhandler(ZeroDivisionError)
def send(e):
    print(e)
    return ''

if __name__ == '__main__':

    try:
        # 运行调试服务器
        app.run(host='0.0.0.0', port=80, debug=False)
    except:
        pass
