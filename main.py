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
plain = open("plain.json","r")
plainDict=json.load(plain)

def getRes(word,pred):
    result=''
    print(word)
    for i in range(0,len(word)):
        print(i)
        if word[i] == pred[i]:
            result += '1'
        elif word.count(pred[i]) != 0:
            result += '2'
        else :
            result += '0'
    return result

@app.route('/lewdle',methods=['POST','GET'])
def lewdle():
    if request.method=="POST":
        print(request.form)
        _word = request.form['word'].lower()
        _pred = request.form['predict'].lower()
        if len(_word) != len(_pred):
            return '-1'
        return getRes(_word,_pred)
    word=_dict[int(uniform(0,999))]
    _list=[word,str(len(word))]
    try :
        _Text = plainDict[word]
        _list.append(_Text)
    except:
        _list.append('')
    return flask.render_template("lewdle.html",data=_list)

@app.route('/checkValid',methods=['POST'])
def checkValid():
    if _valid.count(request.form['word'])!='0':
        return '1'
    return '0'


if __name__=="__main__":
    app.run(port=11451,host="0.0.0.0",debug=True)   #调用run方法，设定端口号，启动服务