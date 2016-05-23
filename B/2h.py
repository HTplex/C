import urllib2
import json

id1 = '2009155608'  # '2009155608'  # '2140251882'  #
id2 = '2341209399'  # '1974331052'  # '2134693834'


def iihop():
	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Composite(AA.AuId=' + id1 + ')&count=10000&attributes=Id,RId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonAuId1 = json.loads(html.read())
	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Composite(AA.AuId=' + id2 + ')&count=10000&attributes=Id,RId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonAuId2 = json.loads(html.read())

	# AA.AuId-Id-AA.AuId

	names = set([m['Id'] for m in jsonAuId1['entities']]) & set([m['Id'] for m in jsonAuId2['entities']])
	print names

	# AA.AuId-Id-Id
	AuidRids = set()
	for Ai in list(set([m['Id'] for m in jsonAuId1['entities']])):
		s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=' + str(
			Ai) + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
		html = urllib2.urlopen(s1)
		jsonAuIdId1 = json.loads(html.read())
		if int(id2) in jsonAuIdId1['entities'][0]['RId']:
			AuidRids = AuidRids | Ai
	names = names | AuidRids
	print names

	# AA.AuId-AA.AFId-AA.AuId

	names1 = [m['Id'] for m in jsonAuId1['entities']]
	names2 = [m['Id'] for m in jsonAuId2['entities']]
	names = names | set(names1) & set(names2)

	print names

	# Id-Id-Id & Id-Id-AuId
	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=' + id1 + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonIdId1 = json.loads(html.read())
	s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=' + id2 + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
	html = urllib2.urlopen(s1)
	jsonIdId2 = json.loads(html.read())

	RId1 = [m['RId'] for m in jsonIdId1['entities']]
	RId2 = [m['RId'] for m in jsonIdId2['entities']]
	print '!'
	print RId1
	RIds = set()
	AuIds = set()
	for RId in RId1[0]:
		s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=Id=' + str(
			RId) + '&count=10000&attributes=RId,AA.AuId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
		html = urllib2.urlopen(s1)
		jsonRIdId = json.loads(html.read())
		# print jsonRIdId['entities'][0]['RId']
		if int(id2) in jsonRIdId['entities'][0]['RId']:
			RIds = RIds | set([RId])
		if int(id2) in [m['AuId'] for m in jsonIdId2['entities'][0]['AA']]:
			AuIds = AuIds | set([RId])
	names = names | RIds
	names = names | AuIds

	print names

	# Id-AA.AuId-Id
	if jsonIdId2['entities'][0].has_key('AA'):
		RAuId1 = [m['AuId'] for m in jsonIdId2['entities'][0]['AA']]
		RAuId2 = [m['AuId'] for m in jsonIdId2['entities'][0]['AA']]
		RAuId12 = set(RAuId1) & set(RAuId2)
		names = names | RAuId12
		print names

	# Id-J.JId-Id
	if jsonIdId2['entities'][0].has_key('J'):
		RJId1 = [m['JId'] for m in jsonIdId2['entities'][0]['J']]
		RJId2 = [m['JId'] for m in jsonIdId2['entities'][0]['J']]
		RJId12 = set(RJId1) & set(RJId2)
		names = names | RJId12
		print names

	# Id-F.FId-Id
	if jsonIdId2['entities'][0].has_key('F'):
		RFId1 = [m['FId'] for m in jsonIdId2['entities'][0]['F']]
		RFId2 = [m['FId'] for m in jsonIdId2['entities'][0]['F']]
		RFId12 = set(RFId1) & set(RFId2)
		names = names | RFId12
		print names

	# Id-C.CId-Id
	if jsonIdId2['entities'][0].has_key('C'):
		RCId1 = [m['CId'] for m in jsonIdId2['entities'][0]['C']]
		RCId2 = [m['CId'] for m in jsonIdId2['entities'][0]['C']]
		RCId12 = set(RCId1) & set(RCId2)
		names = names | RCId12
		print names


if __name__ == '__main__':
	iihop()
