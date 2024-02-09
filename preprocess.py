import json

fp=open("plain.data.txt","r",encoding="utf-8")
k=fp.read()
dictForPlain={}
for i in k.split(","):
    _=i.split(':')
    print(_)
    dictForPlain[_[0]]=_[1].replace('^','\n')
with open("plain.json","w") as fp2:
    print(json.dumps(dictForPlain),file=fp2)

    