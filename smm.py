import requests
import os
import random
import threading
import json
import platform
import os, sys, time
import time as t
from uuid import uuid4
from telethon.errors import FloodWaitError
from telethon.errors import SessionPasswordNeededError, PhoneNumberInvalidError
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from bs4 import BeautifulSoup as bs
import os, sys, requests, re, json, time
from random import choice
from concurrent.futures import ThreadPoolExecutor as tpe

vi='\033[1;35m'
R='\033[1;91m'
V='\033[1;92m'
black="\033[1;30m"
J='\033[1;33m'
C='\033[1;96m'
B='\033[1;97m'
Bl='\033[1;34m'
o="\x1b[38;5;214m"    # Orange
O='\033[38;5;208m'
S='\033[0m'
c='\033[7;96m'
r='\033[7;91m'
v='\033[7;92m'
ro='\033[1;41m'
co='\033[1;46m'


logo = f"""
{o}════════════════════════════════════════════════════════════
{vi}┌──────────────────────────────────────────────┐        {V}2025
│   ______              _       _           _     │
│  |  ____|            | |     | |         | |    │
│  | |__  __  ___ __ __| | __ _| |__   __ _| |_   │
│  |  __| \ \/ / '__/ _` |/ _` | '_ \ / _` | __|  │
│  | |____ >  <| | | (_| | (_| | | | | (_| | |_   │
│  |______/_/\_\_|  \__,_|\__, |_| |_|\__,_|\__|  │
│                         __/ |                  │
│                        |___/                   │
└──────────────────────────────────────────────┘
{o}════════════════════════════════════════════════════════════
{B}[{V}•{B}]{o} Projet       : {vi}real{V}(proj)
{B}[{V}•{B}]{o} Auteur       : {vi}Fares Alex
{B}[{V}•{B}]{o} Statut       : {vi}rest
{B}[{V}•{B}]{o} Version      : {vi}SmmKingdomTask {V}v{J}1.0
{o}════════════════════════════════════════════════════════════
"""

clien=[]
var1=[]
var2=[]
var=[]
compte=[]
comptes=[]
rq=requests.session()
session = "sessions"
BASE_DIR = os.path.join(os.path.dirname(__file__), "SmmKingdomTask")
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
peer = "SmmKingdomTasksBot"
api_id = 2040
api_hash = "b18441a1ff607e10a989891a5462e627"
def user():
  a=random.randint(30,999)
  b=random.randint(0,9)
  c=random.randint(0,9)
  d=random.randint(0,30)
  e=random.randint(10,99)
  f=random.randint(20,29)
  g=random.randint(300,500)
  i=random.randint(6,12)
  k=random.randint(1000000,10000000)
  j="".join(random.SystemRandom().choice("AZERTYUIOPQSDFGHJKLMWXCVBN") for i in range(5))
  proc=random.choice(['qcom',f'mt{random.randint(6750,6790)}'])
  marque=random.choice(['TCL','TECNO','SAMSUNG','ITEL','VIVO','REDMI','MEIZU','HUAWEI','HONOR','ONE PLUS','REALME','SONY','POCO','DOCOMO','OPPO','NOKIA'])
  h=random.choice(['720x,1280','1080x1920','1920x2500'])
  en = random.choice(['en_US','en_GB','en_FR'])
  version=random.choice(['5.0','5.0.1','6.0.1','7.1','8.1.0','9','10','11','12','13','14'])
  ua=f"Instagram {a}.{b}.{c}.{d}.{e} Android ({f}/{version}; {g}dpi; {h}; {marque}; Note {i}; {j}; {proc}; {en}; {k})"
  return ua
def clear():
  os.system('clear')
  print(logo)
def menu():
  global var
  clear()
  print(f"{o}[{V}1{o}] Auto Tasks Bot")
  print(f"{o}[{V}2{o}] Get Account")
  print(f"{o}[{V}3{o}] Get Cookies")
  print(f"{o}[{V}4{o}] Deconnection T/G")
  print(f"{o}[{V}0{o}] Exit")
  print(f"{o}═════════════════════════════════════════")
  sel=input(f"{o}[{V}?{o}] Choice: {B}")
  if sel=="1":
    var.append("1")
    number()
  elif sel=="2":
    var.append("2")
    number()
  elif sel=="3":
    main()
  elif sel=="4":
    os.system("rm -r sessions")
    os.system("rm number.txt")
    clear()
    print(f"{r}Deconnected{S}")
    time.sleep(4)
    menu()
  elif sel=="0":
    exit()
  else:
    menu()
def number():
  clear()
  try:
    phone=open("number.txt","r").read()
  except:
    phone=input(f"{o}[{V}?{o}] Number T/G: {vi}")
    open("number.txt","w").write(phone)
  telegram(phone, return_data=False)
def telegram(phone, return_data):
    global clien
    clien = []
    app_version = "5.1.7 x64"
    device = "Redmi Note 7 Pro"

    # Création du dossier de session si nécessaire
    if not os.path.exists(session):
        os.makedirs(session)

    # Initialisation du client
    client = TelegramClient(
        f"{session}/{phone}",
        api_id=api_id,
        api_hash=api_hash,
        device_model=device,
        app_version=app_version,
        system_version="Android 10",
        lang_code="us",
        system_lang_code="en-US",
    )

    clien.append(client)
    client.connect()

    
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone=phone)
            clear()

            
            if os.path.exists("number.txt"):
                with open("number.txt", "r") as f:
                    number = f.read().strip()
            else:
                number = "Unknown"

            print(f"[!] Your Number: {number}")
            code = input("[?] Input Code Text: ")

            client.sign_in(phone=phone, code=code)
            clear()

        except SessionPasswordNeededError:
            pw2fa = input("[?] Input Password 2FA: ")
            client.sign_in(phone=phone, password=pw2fa)

    
    if not return_data:
        me = client.get_me()
        print(f"[√] Your Account: {me.first_name} {me.last_name}")
        print("═════════════════════════════════════════")

        
        if var[0] == "1":
            account()  
        elif var[0] == "2":
            manage()  

def managers():
  global clien
  client=clien[0]
  channel_entity = client.get_entity("@SmmKingdomTasksBot")
  channel_username = "@SmmKingdomTasksBot"
  posts = client(GetHistoryRequest(peer=channel_entity, limit=10, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
  count=[0,1,2,3,4,5,6,7,8,9]
  for p in count:
    message=posts.messages[p].message
    if "Thank you" in message:
      continue
    elif "Instagram :" in message:
      return message
    elif "WAS NOT rewarded" in message:
      continue
    elif "is not approved" in message:
      continue
    elif "Account was passed" in message:
      continue
    elif "on review now" in message:
      continue
    else:
      continue
def manage():
  count=managers()
  path=os.path.join(BASE_DIR, "acc.txt")
  open(path,'w').write(str(count))
  for x in open(path,'r').readlines():
    acc=x.strip()
    if "💎" in acc:
      user=re.search("💎 (.*?) /",str(acc)).group(1)
      print(f"{vi}{o}Username: {vi}{user}")
      pwd=input(f"{o}Password: {vi}")
      s_acc=open(os.path.join(BASE_DIR, "Compte.txt"),'a')
      s_acc.write(f"{user}|{pwd}\n")
      s_acc.close()
      continue
    elif "✅" in acc:
      cuser=acc.split("✅ ")[1].split(" (")[0]
      print(f"{vi}{o}Username: {vi}{cuser}")
      pwd=input(f"{o}Password: {vi}")
      s_acc=open(os.path.join(BASE_DIR, "Compte.txt"),'a')
      s_acc.write(f"{cuser}|{pwd}\n")
      s_acc.close()
      continue
    else:
      continue
  os.system(f"rm {path}")
def message():
  global clien
  client=clien[0]
  channel_entity = client.get_entity("@SmmKingdomTasksBot")
  channel_username = "@SmmKingdomTasksBot"
  posts = client(GetHistoryRequest(peer=channel_entity, limit=10, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
  count=[0,1,2,3,4,5,6,7,8,9]
  for p in count:
    message=posts.messages[p].message
    if "Thank you" in message:
      continue
    elif "Here is a" in message:
      continue
    elif "WAS NOT rewarded" in message:
      continue
    elif "is not approved" in message:
      continue
    elif "Account was passed" in message:
      continue
    else:
      return message
def coms1():
  global clien
  client=clien[0]
  channel_entity = client.get_entity("@SmmKingdomTasksBot")
  channel_username = "@SmmKingdomTasksBot"
  posts = client(GetHistoryRequest(peer=channel_entity, limit=10, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
  count=[0,1,2,3,4,5,6,7,8,9]
  for p in count:
    message=posts.messages[p].message
    if "Thank you" in message:
      continue
    elif "the comment" in message:
      return message
    else:
      continue
def coms(user):
  global clien
  client=clien[0]
  channel_entity = client.get_entity("@SmmKingdomTasksBot")
  channel_username = "@SmmKingdomTasksBot"
  posts = client(GetHistoryRequest(peer=channel_entity, limit=10, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
  count=[0,1,2,3,4,5,6,7,8,9]
  for p in count:
    message=posts.messages[p].message
    if "Thank you" in message:
      continue
    elif "▪️ Action :" in message:
      continue
    elif "Here is a" in message:
      continue
    elif user in message:
      continue
    elif "Completed" in message:
      continue
    elif "======" in message:
      continue
    else:
      return message
def insta():
  global clien
  client=clien[0]
  channel_entity = client.get_entity("@SmmKingdomTasksBot")
  channel_username = "@SmmKingdomTasksBot"
  posts = client(GetHistoryRequest(peer=channel_entity, limit=10, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
  count=[0,1,2,3,4,5,6,7,8,9]
  for p in count:
    message=posts.messages[p].message
    if "Thank you" in message:
      continue
    elif "Here is a" in message:
      continue
    elif "Please give us" in message:
      return message
    elif "Please choose" in message:
      return message
    elif "⚠️Please do it" in message:
      return message
    elif "======" in message:
      return message
    elif "Instagram" in message:
      return message
    elif "New story is required!" in message:
      return message
    elif "New post is required!" in message:
      return message
    else:
      insta()
def account():
  global clien
  client=clien[0]
  while True:
    path=os.path.join(BASE_DIR, "insta-acc.txt")
    if os.path.exists(path):
      for x in open(path,'r').readlines():
        acc=x.strip()
        user=acc.split("|")[0]
        cooks=acc.split("|")[1]
        uid="3218350887150471448"
        like=likes1(uid,cooks)
        if "ok" in like:
          sys.stdout.write(f"\r{B}[{V}√{B}] {user}\r")
          sys.stdout.flush()
        else:
          print(f"{B}[{R}X{B}] {user}{S} {black}(Verify this account)")
          continue
        channel_entity = client.get_entity("@SmmKingdomTasksBot")
        channel_username = "@SmmKingdomTasksBot"
        client.send_message(entity=channel_entity, message=f"Instagram")
        loop = 0
        while True:
          loop += 1
          if insta() in "Instagram":
            if loop <= 10:
              sys.stdout.write(f"\rInstagram {loop}s\r")
              sys.stdout.flush()
              time.sleep(0.1)
            else:
              client.send_message(entity=channel_entity, message="Instagram")
              break
          else:
            break
        client.send_message(entity=channel_entity, message=f"{user}")
        print(f"{o}[{B}•{o}] Username: {v}{user}{S}")
        mss=message()
        if "Sorry" in mss:
          continue
        elif "▪️ Action :" in mss:
          task(cooks,user)
          continue
        elif "🟡 Account" in mss:
          print(f"{co}{mss}{S}")
          client.send_message(entity=channel_entity, message="🔙Back")
          time.sleep(2)
          continue
        else:
          time.sleep(4)
          task(cooks,user)
          continue
    else:
      os.system("clear")
      u=(f"{r}No File /sdcard/SmmKingdomTask/insta-acc.txt Detected\n{S}")
      for ix in u:
        print(ix,end='',flush=True)
        time.sleep(0.1)
      menu()
def task(cooks,user):
  global clien,var1
  client=clien[0]
  try:
    channel_entity = client.get_entity("@SmmKingdomTasksBot")
    channel_username = "@SmmKingdomTasksBot"
    mss=message()
    if "▪️ Action :" in mss:
      if "the post" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}PostLink: {B}{link}")
        like=likes(link,cooks)
        if "ok" in like:
          print(f"{vi}[{V}√{vi}] {V}Like Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Like No Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
      elif "Follow" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}UserLink: {B}{link}")
        follow=followers(link,cooks)
        if "ok" in follow:
          print(f"{vi}[{V}√{vi}] {V}Followers Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Followers No Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
      elif "the comment" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}CommentLink: {B}{link}")
        time.sleep(2)
        mss=coms(user)
        print(f"{J}{mss}")
        comms=comment(link,cooks,mss)
        if "ok" in comms:
          print(f"{vi}[{V}+{vi}] {V}Comment Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Comment No Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
      elif "Stories" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}StoriesLink: {B}{link}")
        story(link,cooks)
        time.sleep(2)
        print(f"{vi}[{V}√{vi}] {V}Stories view Succes{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        task(cooks,user)
      elif "Open the video" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}TvLink: {B}{link}")
        Tv(link,cooks)
        print(f"{vi}[{V}√{vi}] {V}TV view Succes{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        task(cooks,user)
    elif "Sorry" in mss:
      return None
    elif "🟡 Account" in mss:
      return None
    else:
      if "Completed" in mss:
        i = 0
        while True:
          i += 1
          if message() in "✅Completed":
            if i <= 15:
              sys.stdout.write(f"\r✅Completed {i}s\r")
              sys.stdout.flush()
              time.sleep(0.1)
            else:
              client.send_message(entity=channel_entity, message="✅Completed")
              task(cooks,user)
          else:
            break
        task(cooks,user)
      elif user in mss:
        a = 0
        while True:
          a += 1
          if message() in user:
            if a <= 15:
              sys.stdout.write(f"\r{user} {a}s\r")
              sys.stdout.flush()
              time.sleep(0.1)
            else:
              client.send_message(entity=channel_entity, message=f"{user}")
              task(cooks,user)
          else:
            break
        task(cooks,user)
      else:
        cmt=coms1()
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(cmt)).group(1)
        print(f"{vi}CommentLink: {B}{link}")
        print(f"{J}{mss}")
        comms=comment(link,cooks,mss)
        if "ok" in comms:
          print(f"{vi}[{V}√{vi}] {V}Comment Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Comment No Succes{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
  except:
    task(cooks,user)
def comment(link, cooks, mss):
    header0 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'fr-FR',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user()
    }
    try:
        rq1=rq.get(link,headers=header0,cookies={'cookie':cooks})
        rp1=bs(rq1.text,'html.parser')
        uid=re.search('"media_id":"(.*?)"',str(rp1)).group(1)
        print(f"{o}CommentID: {vi}{uid}{S}")
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de Connection{S}\r")
        sys.stdout.flush()
        comment(link,cooks,mss)
    except:
        return "status fail"
    header= {
        "x-ig-app-id": "1217981644879628",
        "x-asbd-id": "198387",
        "x-instagram-ajax": "c161aac700f",
        "accept": "*/*",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent":"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03S) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19",
        "x-csrftoken": cooks.split("csrftoken= ")[1].split(";")[0],
        "x-requested-with": "XMLHttpRequest",
        "cookie": cooks
    }
    data={'comment_text':mss}
    url=f"https://i.instagram.com/api/v1/web/comments/{uid}/add/"
    try:
        rq2=rq.post(url,headers=header,data=data).text
        return rq2
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de Connection{S}\r")
        sys.stdout.flush()
        comment(link,cooks,mss)
    except:
        return "fail"
def likes1(uid,cooks):
  headers = {
  "x-ig-app-id": "1217981644879628",
  "x-asbd-id": "198387",
  "x-instagram-ajax": "c161aac700f",
  "accept": "*/*",
  "content-length": "0",
  "content-type": "application/x-www-form-urlencoded",
  "user-agent":user(),
  "x-csrftoken": cooks.split("csrftoken= ")[1].split(";")[0],
  "x-requested-with": "XMLHttpRequest",
  "cookie": cooks}
  try:
    rq2=requests.post(f"https://i.instagram.com/api/v1/media/{uid}/like/", headers=headers).text
  except requests.exceptions.ConnectionError:
    sys.stdout.write(f"\r{r}Pas de Connection{S}\r")
    sys.stdout.flush()
    likes1(uid,cooks)
  except:
    likes1(uid,cooks)
  return rq2
def likes(link, cooks):
    header0 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'fr-FR',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user()
    }
    try:
        rq1=rq.get(link,headers=header0,cookies={'cookie':cooks})
        rp1=bs(rq1.text,'html.parser')
        uid=re.search('"media_id":"(.*?)"',str(rp1)).group(1)
        print(f"{o}PostID: {vi}{uid}{S}")
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de Connection{S}\r")
        sys.stdout.flush()
        likes(link,cooks)
    except:
        return "status fail"
    headers = {
        "x-ig-app-id": "1217981644879628",
        "x-asbd-id": "198387",
        "x-instagram-ajax": "c161aac700f",
        "accept": "*/*",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent":user(),
        "x-csrftoken": cooks.split("csrftoken= ")[1].split(";")[0],
        "x-requested-with": "XMLHttpRequest",
        "cookie": cooks
    }
    try:
        rq2=requests.post(f"https://i.instagram.com/api/v1/media/{uid}/like/", headers=headers).text
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de Connection{S}\r")
        sys.stdout.flush()
        likes(link,cooks)
    except:
        return "status fail"
    return rq2
def followers(link, cooks):
    header0 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'fr-FR',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user()
    }
    try:
        rq1=rq.get(link,headers=header0,cookies={'cookie':cooks})
        rp1=bs(rq1.text,'html.parser')
        uid=re.search('"user_id":"(.*?)"',str(rp1)).group(1)
        print(f"{o}UserID: {vi}{uid}{S}")
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de Connection{S}\r")
        sys.stdout.flush()
        followers(link,cooks)
    except:
        return "fail"
    headers = {
        "x-ig-app-id": "1217981644879628",
        "x-asbd-id": "198387",
        "x-instagram-ajax": "c161aac700f",
        "accept": "*/*",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent":user(),
        "x-csrftoken": cooks.split("csrftoken= ")[1].split(";")[0],
        "x-requested-with": "XMLHttpRequest",
        "cookie": cooks
    }
    try:
        rq2=requests.post(f"https://i.instagram.com/api/v1/friendships/create/{uid}/", headers=headers).text
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de Connection{S}\r")
        sys.stdout.flush()
        followers(link,cooks)
    except:
        return "fail"
    return rq2
def story(link, cooks):
    header0 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'fr-FR',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user()
    }
    try:
        rq1=rq.get(link,headers=header0,cookies={'cookie':cooks})
        rp1=bs(rq1.text,'html.parser')
    except:
        story(link,cooks)
    return rp1
def Tv(link, cooks):
    header0 = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'fr-FR',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user()
    }
    try:
        rq1=rq.get(link,headers=header0,cookies={'cookie':cooks})
        rp1=bs(rq1.text,'html.parser')
        time.sleep(4)
    except:
        Tv(link,cooks)
    return rp1
def main():
  clear()
  print(f"{o}[{V}1{o}] Manuel Cookie")
  print(f"{o}[{V}2{o}] Dump Cookie")
  print(f"{o}═════════════════════════════════════════")
  sel=input(f"{o}[{V}?{o}] Choice: {B}")
  if sel=="1":
    cooks()
  elif sel=="2":
    dump()
  else:
    main()
def cooks():
  clear()
  user=input(f"{o}[{V}?{o}]Username: {B}")
  pwd=input(f"{o}[{V}?{o}]Password: {B}")
  uid = uuid4()
  url = "https://i.instagram.com/api/v1/accounts/login/"
  header0 = {
  'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
  "Accept": "/",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "en-US",
  "X-IG-Capabilities": "3brTvw==",
  "X-IG-Connection-Type": "WIFI",
  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
  'Host': 'i.instagram.com',
  'Connection': 'keep-alive'}
  data1 = {
  'uuid': uid,
  'password': pwd,
  'username': user,
  'device_id': uid,
  'from_reg': 'false',
  '_csrftoken': 'YcJzPesTYxMTfmpSOiVn3pfRAJdrETFD',
  'login_attempt_countn': '0'}
  try:
    rq=requests.session()
    rq1 = rq.post(url=url, headers=header0, data=data1)
    rp1 = rq1.text
  except Exception as e:
    print(e)
  if "ok" in rp1:
    cookies=str(rq1.cookies.get_dict())[1:-1].replace("'",'').replace(':','=').replace(',',';')
    print(f"{B}[{V}Lariot{B}] {V}{user} {B}| {V}{pwd}")
    print(f"{B}[{V}COOKIE{B}] {V}{cookies}")
    s_acc=open(os.path.join(BASE_DIR, "insta-acc.txt"),'a')
    s_acc.write(f"{user}|{cookies}\n")
    s_acc.close()
    remove()
    input(f"{o}[{B}•{o}]Enter For Back")
    key()
  else:
    print(f"{B}[{R}!{B}]Incorrect {r}{user}{S} {B}| {r}{pwd}{S}")
    time.sleep(2)
    cooks()
def remove():
  global user
  user=[]
  input_file = os.path.join(BASE_DIR, "insta-acc.txt")
  user.append(input_file)
  unique_ids = {}
  with open(input_file, 'r') as infile:
    lines = infile.readlines()
    lines_reversed = lines[::-1]
    for line in lines_reversed:
      line = line.strip()
      values = line.split('|')
      if len(values) == 2:
        id, pas = values
        key = f"{id}"
        if key not in unique_ids:
          unique_ids[key] = line
  os.system(f"rm {input_file}")
  with open(input_file, 'w') as outfile:
    for line in unique_ids.values():
      outfile.write(line + '\n')
  remove1()
def remove1():
  global user
  input_file = user[0]
  user.append(input_file)
  unique_ids = {}
  with open(input_file, 'r') as infile:
    lines = infile.readlines()
    lines_reversed = lines[::-1]
    for line in lines_reversed:
      line = line.strip()
      values = line.split('|')
      if len(values) == 2:
        id, pas = values
        key = f"{id}"
        if key not in unique_ids:
          unique_ids[key] = line
  os.system(f"rm {input_file}")
  with open(input_file, 'w') as outfile:
    for line in unique_ids.values():
      outfile.write(line + '\n')
    print(f"{B}[{V}√{B}] Auto Remove Succes")
  return "ok"
def dump():
	global comptes
	os.system("clear")
	print(logo)
	path=input(f"{o}[{V}+{o}]File Path: {B}")
	if os.path.exists(path):
		for x in open(path,'r').readlines():
			comptes.append(x.strip())
		base()
	else:
		os.system("clear")
		i=(f"{r}No File Detected\n{S}")
		for ix in i:
		  print(ix,end='',flush=True)
		  time.sleep(0.1)
		dump()
def base():
  global comptes
  for acc in comptes:
    user=acc.split("|")[0]
    pwd=acc.split("|")[1]
    uid = uuid4()
    url = "https://i.instagram.com/api/v1/accounts/login/"
    header0 = {
    'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'}
    data1 = {
    'uuid': uid,
    'password': pwd,
    'username': user,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'YcJzPesTYxMTfmpSOiVn3pfRAJdrETFD',
    'login_attempt_countn': '0'}
    try:
      rq=requests.session()
      rq1 = rq.post(url=url, headers=header0, data=data1)
      rp1 = rq1.text
    except Exception as e:
      print(e)
    if "ok" in rp1:
      cookies=str(rq1.cookies.get_dict())[1:-1].replace("'",'').replace(':','=').replace(',',';')
      print(f"{B}[{V}Lariot{B}] {V}{user} {B}| {V}{pwd}")
      print(f"{B}[{V}COOKIE{B}] {V}{cookies}")
      s_acc=open(os.path.join(BASE_DIR, "insta-acc.txt"),'a')
      s_acc.write(f"{user}|{cookies}\n")
      s_acc.close()
      remove()
      continue
    else:
      print(f"{B}[{R}!{B}]Incorrect {r}{user}{S} {B}| {r}{pwd}{S}")
      continue
def key():
    import webbrowser
    import datetime
    os.system('clear')
    av = "Pro"
    ar = "JK"
    # Chemin du fichier d'autorisation généré par le backend Flask
    auth_file = os.path.expanduser("~/.smmkingdom_auth")
    # Vérification de l'abonnement
    if os.path.exists(auth_file):
        with open(auth_file, 'r') as f:
            lines = f.read().splitlines()
            if len(lines) >= 2:
                expire_str = lines[1].strip()
                try:
                    expire_date = datetime.datetime.strptime(expire_str, "%Y-%m-%d")
                    if expire_date >= datetime.datetime.now():
                        menu()
                        return
                    else:
                        print(f"{r}Votre abonnement a expiré le {expire_str}.{S}")
                except Exception as e:
                    print(f"Erreur de lecture de la date d'expiration: {e}")
            else:
                print(f"{r}Fichier d'autorisation corrompu.{S}")
    # Si pas d'abonnement valide, générer une clé et rediriger vers le site de paiement
    centre = "".join(random.SystemRandom().choice("AZERTYUIOPQSDFGHJKLMWXCVBNabcdefghijklmnopqrstuvwxyz") for i in range(30))
    apv = f"{av}{centre}{ar}"
    os.system("clear")
    la = (f"{r}Vous n'êtes pas encore approuvé pour cet outil.{S}\n{B}[{V}≈{B}] {Bl}Votre clé: {o}{apv}\n{B}[{V}≈{B}]{Bl} Veuillez copier votre clé et payer sur le site.\n{B}[{V}≈{B}] {Bl}Site de paiement: {o}https://passportdl.pythonanywhere.com/\n")
    for lax in la:
        print(lax, end='', flush=True)
        time.sleep(0.05)
    time.sleep(2)
    with open(auth_file, 'w') as lar:
        lar.write(apv + "\n")
        lar.write((datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d"))
    ouvrir_site_paiement()
    exit()
def check_subscription():
    import os
    import datetime
    auth_file = os.path.expanduser("~/.smmkingdom_auth")
    if os.path.exists(auth_file):
        with open(auth_file, 'r') as f:
            lines = f.read().splitlines()
            if len(lines) >= 2:
                expire_str = lines[1].strip()
                try:
                    expire_date = datetime.datetime.strptime(expire_str, "%Y-%m-%d")
                    if expire_date >= datetime.datetime.now():
                        return True
                except Exception as e:
                    pass
    print("Votre abonnement n'est pas actif ou a expiré. Veuillez renouveler.")
    key()
    return False
def ouvrir_site_paiement():
    url = "https://faresal.pythonanywhere.com"
    if sys.platform.startswith('linux'):
        os.system(f"xdg-open {url}")
    elif sys.platform.startswith('win'):
        os.startfile(url)
    elif sys.platform.startswith('darwin'):
        os.system(f"open {url}")
    else:
        print(f"Va sur {url}")
menu()
