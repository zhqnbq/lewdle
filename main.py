import flask
from flask import Flask
from flask import request
from random import uniform

import json

app=Flask(__name__)         #实例化并命名为app实例

_valid=[]
dict=open("dicktionary.json","r")
_dict=json.load(dict) 
validDict=open("dict.json","r")
_valid=json.load(validDict)

@app.route('/lewdle')
def lewdle():
    word=_dict[int(uniform(0,999))]
    _list=[word,str(len(word))]
    return flask.render_template("lewdle.html",data=_list)

@app.route('/checkValid',methods=['POST'])
def checkValid():
    if _valid.count(request.form['word'])!='0':
        return '1'
    return '0'


if __name__=="__main__":
    app.run(port=11451,host="0.0.0.0",debug=True)   #调用run方法，设定端口号，启动服务