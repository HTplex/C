from flask import Flask
from flask import request
import urllib2
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	# print dir(request)
	id1 = str(request.args.get('id1'))
	id2 = str(request.args.get('id2'))
	s=[]
	# io
	data = init(id1,id2)
	jsonAuId1 = data[0]
	jsonAuId2 = data[1]
	jsonId1 = data[2]
	jsonId2 = data[3]
	jsonRId2 = data[4]

	m = idid(id1, id2)
	if len(m) > 0:
		s.append(m)
	print s

	m = idFidid(id1, id2, jsonId1, jsonId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s

	m = idCidid(id1, id2, jsonId1, jsonId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s

	m = idJidid(id1, id2, jsonId1, jsonId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s

	m = ididid(id1, id2, jsonId1, jsonRId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s

	m = ididAuid(id1, id2, jsonId1, jsonAuId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s

	m = Auididid(id1, id2, jsonAuId1, jsonRId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s

	m = idAuidid(id1, id2, jsonId1, jsonId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s
	print "ha"

	m = AuididAuid(id1, id2, jsonAuId1, jsonAuId2)
	if len(m) > 0:
		for n in m:
			s.append(n)
	print s
	print "hei"

	m = AuidAfidAuid(id1, id2, jsonAuId1, jsonAuId2)
	if len(m) > 0:
		for n in m:
			s.append(n)


#main
	return str(s)
def init(id1, id2):
	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Composite(AA.AuId=' + id1 + ')&count=10000&attributes=Id,RId,AA.AfId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonAuId1 = json.loads(html.read())

	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Composite(AA.AuId=' + id2 + ')&count=10000&attributes=Id,RId,AA.AfId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonAuId2 = json.loads(html.read())

	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=' + id1 + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonId1 = json.loads(html.read())

	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=' + id2 + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonId2 = json.loads(html.read())

	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=RId=' + id2 + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonRId2 = json.loads(html.read())

	return [jsonAuId1, jsonAuId2, jsonId1, jsonId2, jsonRId2]


def idid(id1, id2):
	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Or(Or(And(Id=' + id1 + ',Composite(AA.AuId=' + id2 + ')),And(Composite(AA.AuId=' + id1 + '),Id=' + id2 + ')),And(Id=' + id1 + ',RId=' + id2 + '))&count=99999999&attributes=Id,Ti,Y,D,RId,AA.AuId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsona = json.loads(html.read())
	if len(jsona['entities']) != 0:
		return [int(id1), int(id2)]
	return []


def idFidid(id1, id2, jsonId1, jsonId2):
	s = []
	if len(jsonId1['entities']) > 0 and len(jsonId2['entities']) > 0:
		if jsonId1['entities'][0].has_key('F') and jsonId2['entities'][0].has_key('F'):
			RFId1 = [m['FId'] for m in jsonId1['entities'][0]['F']]
			RFId2 = [m['FId'] for m in jsonId2['entities'][0]['F']]
			RFId12 = set(RFId1) & set(RFId2)
			for i in list(RFId12):
				s.append([int(id1), i, int(id2)])
	return s


def idCidid(id1, id2, jsonId1, jsonId2):
	s = []
	if len(jsonId1['entities']) > 0 and len(jsonId2['entities']) > 0:
		if jsonId1['entities'][0].has_key('C') and jsonId2['entities'][0].has_key('C'):

			RCId1 = jsonId1['entities'][0]['C']['CId']
			RCId2 = jsonId1['entities'][0]['C']['CId']
			if RCId1 == RCId2:
				s.append([int(id1), RCId1, int(id2)])
	return s


def idJidid(id1, id2, jsonId1, jsonId2):
	s = []
	if len(jsonId1['entities']) > 0 and len(jsonId2['entities']) > 0:
		if jsonId1['entities'][0].has_key('J') and jsonId2['entities'][0].has_key('J'):

			RJId1 = jsonId1['entities'][0]['J']['JId']
			RJId2 = jsonId1['entities'][0]['J']['JId']
			if RJId1 == RJId2:
				s.append([int(id1), RJId1, int(id2)])
	return s


def ididetc(id1, id2, jsonId1):
	RId1 = [m['RId'] for m in jsonId1['entities']]
	s = set()
	if len(RId1) > 0:
		for RIds in RId1[0]:
			s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=' + str(
				RIds) + '&count=10000&attributes=RId,AA.AuId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
			html = urllib2.urlopen(s1)
			jsonId1RId = json.loads(html.read())
			s = s | set(jsonId1RId['entities'][0]['RId'])
	#print list(s)
	return list(s)


def ididid(id1, id2, jsonId1, jsonRId2):
	s = []
	RId1 = [m['RId'] for m in jsonId1['entities']]
	if len(RId1) > 0:
		RId1 = RId1[0]
	Id2 = [m['Id'] for m in jsonRId2['entities']]
	se = set(RId1) & set(Id2)
	for i in list(se):
		s.append([int(id1), i, int(id2)])
	return list(s)


def idAuidid(id1, id2, jsonId1, jsonId2):
	s = []
	if len(jsonId1['entities']) > 0 and len(jsonId2['entities']) > 0:
		if jsonId1['entities'][0].has_key('AA') and jsonId2['entities'][0].has_key('AA'):
			AuId1 = [m['AuId'] for m in jsonId1['entities'][0]['AA']]
			AuId2 = [m['AuId'] for m in jsonId2['entities'][0]['AA']]
			AuId12 = set(AuId1) & set(AuId2)
			for i in list(AuId12):
				s.append([int(id1), i, int(id2)])
	return s


def AuididAuid(id1, id2,jsonAuId1,jsonAuId2):
	s=[]
	Id1 = list(set([m['Id'] for m in jsonAuId1['entities']]))
	Id2 = list(set([m['Id'] for m in jsonAuId2['entities']]))

	se = set(Id1) & set(Id2)
	for i in list(se):
		s.append([int(id1), i, int(id2)])
	return list(s)


def ididAuid(id1, id2, jsonId1, jsonAuId2):
	s = []
	RId1 = [m['RId'] for m in jsonId1['entities']]
	if len(RId1) > 0:
		RId1 = RId1[0]

	Id2 = list(set([m['Id'] for m in jsonAuId2['entities']]))
	se = set(RId1) & set(Id2)
	for i in list(se):
		s.append([int(id1), i, int(id2)])

	return list(s)


def Auididid(id1, id2, jsonAuId1, jsonRId2):
	s = []
	Id1 = list(set([m['Id'] for m in jsonAuId1['entities']]))
	Id2 = [m['Id'] for m in jsonRId2['entities']]
	se = set(Id1) & set(Id2)
	#print se
	for i in list(se):
		s.append([int(id1), i, int(id2)])
	#print list(s)
	return list(s)


def AuidAfidAuid(id1, id2, jsonAuId1, jsonAuId2):
	s = []
	#print jsonAuId1['entities'][0]
	if len(jsonAuId1['entities']) > 0 and len(jsonAuId2['entities']) > 0:
		if jsonAuId1['entities'][0].has_key('AA') and jsonAuId2['entities'][0].has_key('AA'):
			AfId1 = [m['AfId'] for m in jsonAuId1['entities'][0]['AA']]
			AfId2 = [m['AfId'] for m in jsonAuId2['entities'][0]['AA']]
			AfId12 = set(AfId1) & set(AfId2)
			for i in list(AfId12):
				s.append([int(id1), i, int(id2)])

	return s
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
