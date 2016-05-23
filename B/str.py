ids=[100,101,102,103,104]

probStr=""
prev="Id="
after=""

for id in ids[1:4]:
    tmp = prev+str(id)+after
    if probStr == "":
        probStr = tmp
    probStr = "Or("+probStr+","+tmp+")"
probStr='https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr='+probStr
probStr=probStr+'&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
print probStr