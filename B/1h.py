import urllib2
import json

id1 = '2140251882'
id2 = '2143157063'
s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Or(Or(And(Id='+id1+',Composite(AA.AuId='+id2+')),And(Composite(AA.AuId='+id1+'),Id='+id2+')),And(Id='+id1+',RId='+id2+'))&count=99999999&attributes=Id,Ti,Y,D,RId,AA.AuId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'

#print(s1)
html = urllib2.urlopen(s1)
jsona = json.loads(html.read())
print jsona


