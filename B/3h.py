import urllib2
import json


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

    s1 = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=RId=' + id2 + '&count=1000000&attributes=Id,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
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
    # print list(s)
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


def idAuidid(id1, id2, jsonId1):
    res = []
    AA = jsonId1['entities'][0]['AA']
    auId = []
    for aa in AA:
        if aa.has_key('AuId'):
            auId.append(aa['AuId'])
    linkres = linkcomp(auId, 'Composite(AA.AuId=', ")")
    for jsons in linkres:
        for entity in jsons['entities']:
            # print entity
            if int(id2) in entity['RId']:
                for aa in entity['AA']:
                    if (aa.has_key("AuId")):
                        if aa['AuId'] in auId:
                            res.append([int(id1), aa['AuId'], entity['Id'], int(id2)])
    return res


def AuididAuid(id1, id2, jsonAuId1, jsonAuId2):
    s = []
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
    # print se
    for i in list(se):
        s.append([int(id1), i, int(id2)])
    # print list(s)
    return list(s)


def AuidAfidAuid(id1, id2, jsonAuId1, jsonAuId2):
    s = []
    AfId1 = [];
    AfId2 = []
    for entity1 in jsonAuId1['entities']:
        if entity1.has_key('AA'):
            AAId1 = entity1['AA']
            for aa in AAId1:
                if aa.has_key('AuId'):
                    if aa['AuId'] == long(id1) and aa.has_key('AfId'):
                        AfId1.append(aa['AfId'])
    for entity2 in jsonAuId2['entities']:
        if entity2.has_key('AA'):
            AAId2 = entity2['AA']
            for aa in AAId2:
                if aa.has_key('AuId'):
                    if aa['AuId'] == long(id2) and aa.has_key('AfId'):
                        AfId2.append(aa['AfId'])

    AfId = set(AfId1) & set(AfId2)
    for i in list(AfId):
        s.append([int(id1), i, int(id2)])

    return s


# ------------------------------------------------3h---------------------------------------------

atattrList = ['C', 'J']


def foundAfByAu(jsonAuId, auId):
    AfId = []
    for entity in jsonAuId['entities']:
        if entity.has_key('AA'):
            AAId = entity['AA']
            for aa in AAId:
                if aa.has_key('AuId'):
                    if aa['AuId'] == long(auId) and aa.has_key('AfId'):
                        AfId.append(aa['AfId'])
    return AfId


def foundAttrByEntity(entity):
    idAttrList = []
    for attr in idAttrList:
        if (entity.has_key(attr)):
            idAttrList.append(entity[attr][attr + 'Id'])
    if entity.has_key('F'):
        for f in entity['F']:
            if (f.has_key('FId')):
                idAttrList.append(f['FId'])
    if entity.has_key('AA'):
        for aa in entity['AA']:
            if (aa.has_key('AuId')):
                idAttrList.append(aa['AuId'])
    return idAttrList


def idAuAfAu(id1, id2, jsonId1, jsonAuId2):
    res = []
    afId2 = foundAfByAu(jsonAuId2, id2)
    auId1 = []
    mp = {}
    for aa in jsonId1['entities'][0]['AA']:
        if aa.has_key('AuId'):
            auId1.append(aa['AuId'])
            mp[aa['AuId']] = []
    linkres = linkcomp(auId1, "Composite(AA.AuId=", ")")
    for jsons in linkres:
        for entity in jsons['entities']:
            if entity.has_key('AA'):
                nowAA = entity['AA']
                for aa in nowAA:
                    for stdau in auId1:
                        if aa.has_key('AuId') and aa.has_key('AfId') and aa['AuId'] == stdau:
                            mp[stdau].append(aa['AfId'])
    for stdau in auId1:
        nowres = set(mp[stdau]) & set(afId2)
        for x in nowres:
            res.append([int(id1), stdau, x, int(id2)])
    return res


def AuAfAuid(id1, id2, jsonAuId1, jsonId2):
    res = idAuAfAu(id2, id1, jsonId2, jsonAuId1)
    nowres = []
    for result in res:
        nowres.append(res.reverse())
    return nowres


def ididid_id_or_au(id1, id2, jsonId1, json2):  # json2 = jsonRid2 or jsonAuId2
    res = []
    id2List = []
    for entity in json2['entities']:
        id2List.append(entity['Id'])
    Rid1List = []
    if len(jsonId1['entities']) > 0 and jsonId1['entities'][0].has_key('RId'):
        Rid1List = jsonId1['entities'][0]['RId']

    if len(Rid1List) == 0:
        return res

    linkres = linkcomp(Rid1List, "Id=", "")

    for jsons in linkres:
        for entity in jsons['entities']:
            if entity.has_key('RId'):
                nowRid = entity['RId']
                nowres = set(nowRid) & set(id2List)
                for x in nowres:
                    res.append([int(id1), entity['Id'], x, int(id2)])
    return res


def Auididid_or_au(id1, id2, jsonAuId1, json2):  # json2 = jsonRid2 or jsonAuId2
    res = []
    id2List = []
    for entity in json2['entities']:
        id2List.append(entity['Id'])
    id1List = []
    for entity in jsonAuId1['entities']:
        id1List.append(entity['Id'])
    linkres = linkcomp(id1List, "Id=", "")
    if len(linkres)==1:
        for entity in linkres:
           if entity.has_key('RId'):
                nowRid = entity['RId']
                nowres = set(nowRid) & set(id2List)
                for x in nowres:
                    res.append([int(id1), entity['Id'], x, int(id2)])
    else:
        for entity in linkres:
            if entity.has_key('RId'):
                nowRid = entity['RId']
                nowres = set(nowRid) & set(id2List)
                for x in nowres:
                    res.append([int(id1), entity['Id'], x, int(id2)])

    return res


def ididEid(id1, id2, jsonId1, jsonId2):
    res = []
    id2AttrList = []
    if len(jsonId2['entities']) > 0:
        enti2 = jsonId2['entities'][0]
        id2AttrList = foundAttrByEntity(enti2)
    Rid1List = []
    if jsonId1['entities'][0].has_key('RId'):
        Rid1List = jsonId1['entities'][0]['RId']
    linkres = linkcomp(Rid1List, "Id=", "")
    for jsons in linkres:
        for entity in jsons['entities']:
            nowAttr = foundAttrByEntity(entity)
            nowres = set(nowAttr) & set(id2AttrList)
            for x in nowres:
                res.append([int(id1), entity['Id'], x, int(id2)])
    return res


def AuidEid(id1, id2, jsonAuId1, jsonId2):
    res = []
    id1AttrList = []
    if len(jsonId2['entities']) > 0:
        enti1 = jsonId2['entities'][0]
        id1AttrList = foundAttrByEntity(enti1)

    if len(jsonAuId1['entities']) > 0:
        for enti2 in jsonAuId1['entities']:
            id2AttrList = foundAttrByEntity(enti2)

            res = set(id1AttrList) & set(id2AttrList)
            for x in list(res):
                res.append([int(id1), enti2['Id'], x, int(id2)])
    return res


def idEidAu(id1, id2, jsonId1, jsonAuId2):
    return idEidid(id1, id2, jsonId1, jsonAuId2)


def idEidid(id1, id2, jsonId1, jsonRId2):
    res = []
    id1AttrList = []
    if len(jsonId1['entities']) > 0:
        enti1 = jsonId1['entities'][0]
        id1AttrList = foundAttrByEntity(enti1)

    if len(jsonRId2['entities']) > 0:
        for enti2 in jsonRId2['entities']:
            id2AttrList = foundAttrByEntity(enti2)
            nowres = set(id1AttrList) & set(id2AttrList)
            for x in list(nowres):
                res.append([int(id1), x, enti2['Id'], int(id2)])
    return res


def idAuidAu(id1, di2, jsonId1):
    res = []
    AA = []
    if len(jsonId1['entities']) > 0:
        if jsonId1['entities'][0].has_key('AA'):
            AA = jsonId1['entities'][0]['AA']
    auId = []
    for aa in AA:
        if aa.has_key('AuId'):
            auId.append(aa['AuId'])
    linkres = linkcomp(auId, 'Composite(AA.AuId=', ")")
    for entity in linkres:
        au2list = []
        if entity.has_key('AA'):
            for aa in entity['AA']:
                if aa.has_key('AuId'):
                    au2list.append(aa['AuId'])
        if int(id2) in au2list:
            for au in au2list:
                if au in auId:
                    res.append([int(id1), au, entity['Id'], int(id2)])
    return res


def linkcomp(lis, prev, after):
    leng = len(prev) + len(after) + 16
    probStr = ""
    num = 1800 / leng

    a = 0
    b = num
    jsons = []
    #    print len(lis)
    #   print b
    if num < len(lis):
        while b < len(lis):
            for id in lis[a:b]:
                tmp = prev + str(id) + after
                if probStr == "":
                    probStr = tmp
                probStr = "Or(" + probStr + "," + tmp + ")"
            probStr = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=' + probStr
            probStr = probStr + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
            #          print probStr
            html = urllib2.urlopen(probStr)
            probStr = ""
            jsons.append(json.loads(html.read())['entities'])
            #         print jsons
            a = a + num;
            b = b + num;

        for id in lis[b - num:len(lis)]:
            tmp = prev + str(id) + after
            if probStr == "":
                probStr = tmp
            probStr = "Or(" + probStr + "," + tmp + ")"
        probStr = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=' + probStr
        probStr = probStr + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
        html = urllib2.urlopen(probStr)
        probStr = ""
        jsons.append(json.loads(html.read())['entities'])
    else:
        for id in lis[0:len(lis)]:
            tmp = prev + str(id) + after
            if probStr == "":
                probStr = tmp
            probStr = "Or(" + probStr + "," + tmp + ")"
        probStr = 'https://oxfordhk.azure-api.net/academic/v1.0/evaluate?expr=' + probStr
        probStr = probStr + '&count=1000000&attributes=Id,RId,AA.AuId,J.JId,C.CId,F.FId&subscription-key=f7cc29509a8443c5b3a5e56b0e38b5a6'
        html = urllib2.urlopen(probStr)
        probStr = ""
        jsons.append(json.loads(html.read()))
    print jsons
    return jsons


def test(func, id1, id2, json1, json2):
    res = func(id1, id2, json1, json2)
    for x in res:
        print x
    return res


def test(func, id1, id2, json1, json2):
    res = func(id1, id2, json1, json2)
    for x in res:
        print x
    return res


if __name__ == '__main__':
    s = []
    id1 = '1979408141'
    id2 = '192568081'

    data = init(id1, id2)
    jsonAuId1 = data[0]
    jsonAuId2 = data[1]
    jsonId1 = data[2]
    jsonId2 = data[3]
    jsonRId2 = data[4]

    m = idid(id1, id2)
    if len(m) > 0:
        s.append(m)
    print s

    if len(jsonAuId1['entities']) == 0:
        if len(jsonAuId2['entities']) == 0:
            print 'idid'
            m = idFidid(id1, id2, jsonId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = idCidid(id1, id2, jsonId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = idJidid(id1, id2, jsonId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = ididid(id1, id2, jsonId1, jsonRId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = idAuidid(id1, id2, jsonId1)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = ididid_id_or_au(id1, id2, jsonId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = ididEid(id1, id2, jsonId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = idEidid(id1, id2, jsonId1, jsonRId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

        else:
            print 'idAuid'
            m = ididAuid(id1, id2, jsonId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = idAuAfAu(id1, id2, jsonId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = ididid_id_or_au(id1, id2, jsonId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = idEidAu(id1, id2, jsonId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)
            m = idAuidAu(id1, id2, jsonId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)


    else:
        if len(jsonAuId2['entities']) == 0:
            print 'Auidid'

            m = Auididid(id1, id2, jsonAuId1, jsonRId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = AuAfAuid(id1, id2, jsonAuId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = Auididid_or_au(id1, id2, jsonAuId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = AuidEid(id1, id2, jsonAuId1, jsonId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)


        else:

            m = AuididAuid(id1, id2, jsonAuId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = AuidAfidAuid(id1, id2, jsonAuId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

            m = Auididid_or_au(id1, id2, jsonAuId1, jsonAuId2)
            if len(m) > 0:
                for n in m:
                    s.append(n)

print s

# s.extend(test(idEidid,id1,id2,jsonId1,jsonRId2))

# idEidid(id1, id2, jsonId1, jsonRId2)
