import flask
from flask import Flask
from flask import request
from random import uniform
import re

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
    result='00000'
    resultCount={}
    for i in range(0,len(word)):
        if word[i] == pred[i]:
            result[i]="1"
            try:
                resultCount[pred[i]]+=1
            except:
                resultCount[pred[i]]=1
    for i in range(0,len(word)):
        if result[i] !="1" and word.count(pred[i])!=0:
            try:
                if resultCount[pred[i]] != word.count(pred[i]):
                    resultCount[pred[i]]+=1
                    result[i]="2"
            except:
                resultCount[pred[i]]=1
                result[i]="2"
    return result
    # print(word)
    # for i in range(0,len(word)):
    #     print(i)
    #     if word[i] == pred[i]:
    #         result += '1'
    #         try:
    #             resultCount[pred[i]]+=1
    #         except:
    #             resultCount[pred[i]]=1
    #     elif word.count(pred[i]) != 0:
    #         try:
                

    #         result += '2'
    #     else :
    #         result += '0'
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
    return flask.render_template("lewdle2.html",data=_list)

@app.route('/main.min.css')
def main_min_css():
    return flask.render_template("css/main.min.css")

@app.route('/wordle.min.css')
def wordle_min_css():
    return flask.render_template("css/wordle.min.css")

@app.route('/smartbanner.min.css')
def smartbanner_min_css():
    return flask.render_template("css/smartbanner.min.css")

@app.route('/checkValid',methods=['POST'])
def checkValid():
    _get = request.form["word"].lower()
    if _valid.count(_get)!=0:
        return '1'
    return '0'


if __name__=="__main__":
    app.run(port=11451,host="0.0.0.0",debug=True)   #调用run方法，设定端口号，启动服务