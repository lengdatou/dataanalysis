#coding:utf-8
'''
Created on 2016年3月2日

@author: RD04
'''

import json
import os





#===============================================================================
# if __name__ == "__main__":
#     fishs=json.load(file('fish.json'), 'utf-8')
#     fishid={}
#     for f in fishs:
#         fishid[str(f['id'])]=0
#         
#     fishrefresh=json.load(file('refresh5.json'), 'utf-8')
#     for ref in fishrefresh:
#         reftimes=3600/ref["interval"]
#         randall=0
#         for item in ref['items']:
#             randall=randall+item['rand']
#         for item in ref['items']:
#             if item['type']=='single':
#                 fishid[str(item['fishid'])]=fishid[str(item['fishid'])]+item['rand']*reftimes/randall
# 
#     
#     for i in fishid.keys():
#         print i,fishid[i]
#===============================================================================
    
#===============================================================================
# if __name__ == "__main__":
#     goods=json.load(file('otherjson\\trade.json'), 'utf-8')
#     evegood = goods['common2']
#     for f in evegood:
#         #print 'goodsId is',f['goodsId']
#         a=(f['cv']/5)/f['money']
#         b=(f['cvpool']/5)/f['money']
#         if a==300 and b==30:
#             print f['vis'],'||||',f['name'],f['money'],a,b,'OK'
#         else:
#             print 'error!!!!',f['vis'],'||||',f['name'],f['money'],a,b
#         print '------------------------------------'
#     raw_input()
#===============================================================================
 
partner  =  0
jsonname = 'goods'


VALUE_ITEM_TAG_GOLD             = u'G'
VALUE_ITEM_TAG_LOTTERY          = u'L'
VALUE_ITEM_TAG_PROP             = u'P'
VALUE_ITEM_TAG_DIAMOND          = u'D'


def printlist(listA,ifnewline=False):
    for i in listA:
        if ifnewline==False:
            print i,
        else:
            print i

def checklistinlist(listA,listB,specialnumlist=[37]):
    for i in listA:
        if i not in listB:
            if i in specialnumlist:
                continue
            else:
                return False
    return True

def getfiles(vname):
    allfiles=os.listdir('otherjson')
    tempfiles=[]
    for i in range(len(allfiles)):
        if allfiles[i].endswith(vname+'.json')==True:
                tempfiles.append(allfiles[i])
    return tempfiles
 
def checkgoods(vjsonname):
    goods=json.load(file('otherjson\\'+vjsonname), 'utf-8')
    paytypefile=json.load(file('otherjson\\'+'paytypelist.json'), 'utf-8')
    vpartner=vjsonname.split('-')[0]
    if vpartner==vjsonname or vpartner=='11':
        cvrate=300
        cvpoolrate=30
        vpartner='11'
    else:
        cvrate=150
        cvpoolrate=15
    if vjsonname.endswith('goods.json')==True:
        evegood = goods['goods']  
    else:
        evegood = goods['common2']
    countright=0
    countwrong=0
    for f in evegood:
        #print 'goodsId is',f['goodsId']
        a=(f['cv']/5)/f['money']
        b=(f['cvpool']/5)/f['money']
       # if f.get()
        if a==cvrate and b==cvpoolrate and (f['id']/1000-int(vpartner))==1000 and checklistinlist(f['paytypelist'], paytypefile[str(vpartner)]):
            countright+=1
            ifeeror='Ok'
        else:
            countwrong+=1
            ifeeror='Error!!!!!'
        printobj=[f['paytypelist'],f['id'],'||||',f['vis'],'||||',f['name'],f['money'],a,b,ifeeror]
        printlist(printobj)
        print '\n------------------------------------'
    print "right : ",countright,", wrong : ",countwrong
    if countwrong>0:
        return vpartner,False
    else:
        return vpartner,True

            
def updateactions():
    filename='actions'
    allfiles=os.listdir('otherjson')
    tempfiles=[]
    for i in range(len(allfiles)):
        if allfiles[i].endswith(filename+'.json')==True:
                tempfiles.append(allfiles[i])
    for j in tempfiles:
        actionfile=json.load(file('otherjson\\'+j), 'utf-8')


def runcheckgoods():
    wrongfiles=[]
    if partner!=0:
        handlefilenames=[str(partner)+'-goods.json']
    else:
        handlefilenames=getfiles('goods')
    for vf in handlefilenames:
        checkresult=eval('checkgoods')(vf)
        if checkresult[1]==False:
            wrongfiles.append(checkresult[0])
    print 'Wrong files list is : ',wrongfiles
    
def getpaytypelist():
    handlefilenames=getfiles('trade')
    plist={}
    for vf in handlefilenames:
        vpartner=vf.split('-')[0]
        if vpartner==vf:
            vpartner='11'
        paytype=json.load(file('otherjson\\'+vf), 'utf-8')
        plist[vpartner]=paytype['common2'][0]['paytypelist']
    return plist

def parseValueItems(vstr):
    ret = []
    if len(vstr)==0:
        return ret
    strs = vstr.split(u',')
    for vs in strs:
        tag = vs[0]
        vstrs = vs[1:].split(u'-')
        
        vi = ValueItem()
        vi.type = VALUE_ITEM_TAG_MAP.get(tag)
        for sss in vstrs:
            vi.values.append(int(sss))
        ret.append(vi)
        if vi.type==const.VALUE_ITEM_TYPE_PROP:
            assert len(vi.values)==2#道具类型,[id,count]
    return ret

def valueItemList2String(vilist):
    ret = u''
    for vi in vilist:
        ret += (vi.toString() + u',')
    if len(ret)==0:
        return ret
    return ret[:-1]

def makeValueItemString(gold, lottery, propid, propcount):
    ret = u''
    if gold>0:
        ret += (u'%s%d,' % (const.VALUE_ITEM_TAG_GOLD, gold))
    if lottery>0:
        ret += (u'%s%d,' % (const.VALUE_ITEM_TAG_LOTTERY, lottery))
    if propid>0:
        ret += (u'%s%d-%d,' % (const.VALUE_ITEM_TAG_PROP, propid, propcount))
    if len(ret)==0:
        return ret
    return ret[:-1]

if __name__ == "__main__":
    runcheckgoods()
    #getpaytypelist()



    
                
   
