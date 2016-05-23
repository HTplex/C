import urllib2
import json

s = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=2140251882&count=10000&attributes=Id,AA.AuId,AA.AfId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
html = urllib2.urlopen(s)
jsona = json.loads(html.read())
print jsona['entities'][0]['AA']

