# -*- coding: utf-8 -*-
from linepy import *
import sys, json, codecs, os
tkn = json.load(codecs.open("tokens.json","r","utf-8"))
cl = LINE(tkn["tokens"][0], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('主機-{} 登入成功 '.format(cl.profile.displayName))
k1 = LINE(tkn["tokens"][1], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('1號機-{} 登入成功 '.format(k1.profile.displayName))
k2 = LINE(tkn["tokens"][2], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('2號機-{} 登入成功 '.format(k2.profile.displayName))
k3 = LINE(tkn["tokens"][3], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('3號機-{} 登入成功 '.format(k3.profile.displayName))
k4 = LINE(tkn["tokens"][4], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('4號機-{} 登入成功 '.format(k4.profile.displayName))
k5 = LINE(tkn["tokens"][5], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('5號機-{} 登入成功 '.format(k5.profile.displayName))
js = LINE(tkn["tokens"][6], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('JS防-{} 登入成功 '.format(js.profile.displayName))
js2 = LINE(tkn["tokens"][7], appName="IOS\t8.14.2\tIphone X\t8.1.0") 
print('JS2防-{} 登入成功 '.format(js2.profile.displayName))

print("開始設定好友")
cl.findAndAddContactsByMid(k1.profile.mid)
cl.findAndAddContactsByMid(k2.profile.mid)
cl.findAndAddContactsByMid(k3.profile.mid)
cl.findAndAddContactsByMid(k4.profile.mid)
cl.findAndAddContactsByMid(k5.profile.mid)
cl.findAndAddContactsByMid(js.profile.mid)
cl.findAndAddContactsByMid(js2.profile.mid)
k1.findAndAddContactsByMid(cl.profile.mid)
k1.findAndAddContactsByMid(k2.profile.mid)
k1.findAndAddContactsByMid(k3.profile.mid)
k1.findAndAddContactsByMid(k4.profile.mid)
k1.findAndAddContactsByMid(k5.profile.mid)
k1.findAndAddContactsByMid(js.profile.mid)
k1.findAndAddContactsByMid(js2.profile.mid)
k2.findAndAddContactsByMid(cl.profile.mid)
k2.findAndAddContactsByMid(k1.profile.mid)
k2.findAndAddContactsByMid(k3.profile.mid)
k2.findAndAddContactsByMid(k4.profile.mid)
k2.findAndAddContactsByMid(k5.profile.mid)
k2.findAndAddContactsByMid(js.profile.mid)
k2.findAndAddContactsByMid(js2.profile.mid)
k3.findAndAddContactsByMid(cl.profile.mid)
k3.findAndAddContactsByMid(k1.profile.mid)
k3.findAndAddContactsByMid(k2.profile.mid)
k3.findAndAddContactsByMid(k4.profile.mid)
k3.findAndAddContactsByMid(k5.profile.mid)
k3.findAndAddContactsByMid(js.profile.mid)
k3.findAndAddContactsByMid(js2.profile.mid)
k4.findAndAddContactsByMid(cl.profile.mid)
k4.findAndAddContactsByMid(k1.profile.mid)
k4.findAndAddContactsByMid(k2.profile.mid)
k4.findAndAddContactsByMid(k3.profile.mid)
k4.findAndAddContactsByMid(k5.profile.mid)
k4.findAndAddContactsByMid(js.profile.mid)
k4.findAndAddContactsByMid(js2.profile.mid)
k5.findAndAddContactsByMid(cl.profile.mid)
k5.findAndAddContactsByMid(k1.profile.mid)
k5.findAndAddContactsByMid(k2.profile.mid)
k5.findAndAddContactsByMid(k3.profile.mid)
k5.findAndAddContactsByMid(k4.profile.mid)
k5.findAndAddContactsByMid(js.profile.mid)
k5.findAndAddContactsByMid(js2.profile.mid)
js.findAndAddContactsByMid(cl.profile.mid)
js.findAndAddContactsByMid(k1.profile.mid)
js.findAndAddContactsByMid(k2.profile.mid)
js.findAndAddContactsByMid(k3.profile.mid)
js.findAndAddContactsByMid(k4.profile.mid)
js.findAndAddContactsByMid(k5.profile.mid)
js.findAndAddContactsByMid(js2.profile.mid)
js2.findAndAddContactsByMid(cl.profile.mid)
js2.findAndAddContactsByMid(k1.profile.mid)
js2.findAndAddContactsByMid(k2.profile.mid)
js2.findAndAddContactsByMid(k3.profile.mid)
js2.findAndAddContactsByMid(k4.profile.mid)
js2.findAndAddContactsByMid(k5.profile.mid)
js2.findAndAddContactsByMid(js.profile.mid)
print("開始初始化設定…")
for y in [cl,k1,k2,k3,k4,k5,js,js2]:
    for x in y.groups:
        y.leaveGroup(x)
        print("leave "+x)
    for x in y.getGroupIdsInvited():
        y.rejectGroupInvitation(x)
        print("reject "+x)
    print("success !!")
sys.exit()



"""

def lineBot2(op):
    try:
        if op.type ==0:
            return
        elif op.type == 32:
            if op.param3 == jsMID:
                try:
                    cl.findAndAddContactsByMid(jsMID)
                    cl.inviteIntoGroup(op.param1,[jsMID])
                except:
                    try:
                        k1.findAndAddContactsByMid(jsMID)
                        k1.inviteIntoGroup(op.param1,[jsMID])
                    except:
                        try:
                            k2.findAndAddContactsByMid(jsMID)
                            k2.inviteIntoGroup(op.param1,[jsMID])
                        except:
                            try:
                                k3.findAndAddContactsByMid(jsMID)
                                k3.inviteIntoGroup(op.param1,[jsMID])
                            except:
                                try:
                                   k4.findAndAddContactsByMid(jsMID)
                                   k4.inviteIntoGroup(op.param1,[jsMID])
                                except:
                                    try:
                                        k5.findAndAddContactsByMid(jsMID)
                                        k5.inviteIntoGroup(op.param1,[jsMID])
                                    except:
                                        G = cl.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        random.choice(set["bot1"]).updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        js.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        random.choice(set["bot1"]).updateGroup(G)
                if not cek(op.param2):
                    random.choice(set["bot1"]).kickoutFromGroup(op.param1,[op.param2])
                ban["blacklist"][op.param2] = True
                json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
        elif op.type == 17:
            if op.param2 in ban["blacklist"]: 
                random.choice(set["bot1"]).kickoutFromGroup(op.param1,[op.param2])
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = True
                random.choice(set["bot1"]).updateGroup(G)
        elif op.type ==19:
            if not cek(op.param2):
                try:
                    k5.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        k4.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            k3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                k2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        js.acceptGroupInvitation(op.param1)
                                        js.kickoutFromGroup(op.param1,[op.param2])
                                        G = js.getGroupWithoutMembers(op.param1)
                                        G.preventedJoinByTicket = False
                                        js.updateGroup(G)
                                        Ticket = js.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G.preventedJoinByTicket = True
                                        js.updateGroup(G)
                                        js.leaveGroup(op.param1)
                                        cl.findAndAddContactsByMid(jsMID)
                                        cl.inviteIntoGroup(op.param1,[jsMID])
                                    else:
                                        pass
                ban["blacklist"][op.param2] = True
                json.dump(ban, codecs.open('ban.json','w','utf-8'), sort_keys=True, indent=4, ensure_ascii=False) 
            if op.param3 in clMID:
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = False
                try:
                    k1.updateGroup(G)
                    Ticket = k1.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    try:
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                    except:
                        try:
                            k3.updateGroup(G)
                            Ticket = k3.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                k4.updateGroup(G)
                                Ticket = k4.reissueGroupTicket(op.param1)
                                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            except:
                                try:
                                    k5.updateGroup(G)
                                    Ticket = k5.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                except:
                                    pass
                try:
                    random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
                    G.preventedJoinByTicket = True
                    random.choice(set["bot1"]).updateGroup(G)
                except:
                    pass
            elif op.param3 in k1MID:
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = False
                try:
                    k2.updateGroup(G)
                    Ticket = k2.reissueGroupTicket(op.param1)
                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    try:
                        k3.updateGroup(G)
                        Ticket = k3.reissueGroupTicket(op.param1)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                    except:
                        try:
                            k4.updateGroup(G)
                            Ticket = k4.reissueGroupTicket(op.param1)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                k5.updateGroup(G)
                                Ticket = k5.reissueGroupTicket(op.param1)
                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            except:
                                try:
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                except:
                                    pass
                try:
                    random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
                    G.preventedJoinByTicket = True
                    random.choice(set["bot1"]).updateGroup(G)
                except:
                    pass
            elif op.param3 in k2MID:
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = False
                try:
                    k3.updateGroup(G)
                    Ticket = k3.reissueGroupTicket(op.param1)
                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    try:
                        k4.updateGroup(G)
                        Ticket = k4.reissueGroupTicket(op.param1)
                        k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                    except:
                        try:
                            k5.updateGroup(G)
                            Ticket = k5.reissueGroupTicket(op.param1)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                k1.updateGroup(G)
                                Ticket = k1.reissueGroupTicket(op.param1)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            except:
                                try:
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                except:
                                    pass
                try:
                    random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
                    G.preventedJoinByTicket = True
                    random.choice(set["bot1"]).updateGroup(G)
                except:
                    pass
            elif op.param3 in k3MID:
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = False
                try:
                    k4.updateGroup(G)
                    Ticket = k4.reissueGroupTicket(op.param1)
                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    try:
                        k5.updateGroup(G)
                        Ticket = k5.reissueGroupTicket(op.param1)
                        k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                    except:
                        try:
                            k1.updateGroup(G)
                            Ticket = k1.reissueGroupTicket(op.param1)
                            k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                k2.updateGroup(G)
                                Ticket = k2.reissueGroupTicket(op.param1)
                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            except:
                                try:
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                except:
                                    pass
                try:
                    random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
                    G.preventedJoinByTicket = True
                    random.choice(set["bot1"]).updateGroup(G)
                except:
                    pass
            elif op.param3 in k4MID:
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = False
                try:
                    k5.updateGroup(G)
                    Ticket = k5.reissueGroupTicket(op.param1)
                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    try:
                        k1.updateGroup(G)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                    except:
                        try:
                            k2.updateGroup(G)
                            Ticket = k2.reissueGroupTicket(op.param1)
                            k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                k3.updateGroup(G)
                                Ticket = k3.reissueGroupTicket(op.param1)
                                k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            except:
                                try:
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                except:
                                    pass
                try:
                    random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
                    G.preventedJoinByTicket = True
                    random.choice(set["bot1"]).updateGroup(G)
                except:
                    pass
            elif op.param3 in k5MID:
                G = cl.getGroupWithoutMembers(op.param1)
                G.preventedJoinByTicket = False
                try:
                    k1.updateGroup(G)
                    Ticket = k1.reissueGroupTicket(op.param1)
                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                except:
                    try:
                        k2.updateGroup(G)
                        Ticket = k2.reissueGroupTicket(op.param1)
                        k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                    except:
                        try:
                            k3.updateGroup(G)
                            Ticket = k3.reissueGroupTicket(op.param1)
                            k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        except:
                            try:
                                k4.updateGroup(G)
                                Ticket = k4.reissueGroupTicket(op.param1)
                                k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            except:
                                try:
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k5.acceptGroupInvitationByTicket(op.param1,Ticket)
                                except:
                                    pass
                try:
                    random.choice(set["bot1"]).cancelGroupInvitation(op.param1,[op.param2])
                    G.preventedJoinByTicket = True
                    random.choice(set["bot1"]).updateGroup(G)
                except:
                    pass
            elif op.param3 in ban["owners"]:
                try:
                    k5.findAndAddContactsByMid(op.param3)
                    k5.inviteIntoGroup(op.param1,[op.param3])
                except:
                    try:
                        k4.findAndAddContactsByMid(op.param3)
                        k4.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            k3.findAndAddContactsByMid(op.param3)
                            k3.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                k2.findAndAddContactsByMid(op.param3)
                                k2.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    k1.findAndAddContactsByMid(op.param3)
                                    k1.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                    except:a
                                        pass
        elif op.type == 13:
            if not cek(op.param2) and clMid in op.param3:
                js.rejectGroupInvitation(op.param1)
    except Exception as error:
        print(error)
def bot2run():
    while 1:
        try:
            ops = oepolls.singleTrace(count=50)
            if ops is not None:
                for op in ops:
                    lineBot2(op)
                    oepolls.setRevision(op.revision)
        except:
            pass
threading.Thread(target=bot2run).start()
"""
