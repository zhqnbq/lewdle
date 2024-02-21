import json

# fp=open("plain.data.txt","r",encoding="utf-8")
# k=fp.read()
# dictForPlain={}
# for i in k.split(","):
#     _=i.split(':')
#     print(_)
#     dictForPlain[_[0]]=_[1]
# with open("plain.json","w") as fp2:
#     print(json.dumps(dictForPlain),file=fp2)

fp=open("dict.json","r")
__d=[]
dict=json.load(fp)
for i in dict:
    __d.append(i.lower())
with open("dict2.json","w") as fp2:
    print(json.dumps(__d),file=fp2)
    