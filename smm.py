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
from telethon.errors import SessionPasswordNeededError, PhoneNumberInvalidError, PhoneNumberBannedError
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from bs4 import BeautifulSoup as bs
import os, sys, requests, re, json, time
from random import choice
from concurrent.futures import ThreadPoolExecutor as tpe
import webbrowser
import datetime
import sqlite3
import shutil

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
{B}[{V}•{B}]{o} Version      : {vi}SmmKingdomTask {V}v{J}1.1
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
  print(f"{o}[{V}1{o}] Démarrer les tâches automatiques")
  print(f"{o}[{V}2{o}] Changer le compte Telegram")
  print(f"{o}[{V}3{o}] Obtenir les cookies d'un compte")
  print(f"{o}[{V}4{o}] Déconnexion Telegram")
  print(f"{o}[{V}5{o}] Gérer les comptes Instagram")
  print(f"{o}[{V}6{o}] Mettre à jour le Bot")
  print(f"{o}[{V}0{o}] Quitter")
  print(f"{o}═════════════════════════════════════════")
  sel=input(f"{o}[{V}?{o}] Votre choix : {B}")
  if sel=="1":
    var.clear()
    var.append("1")
    number()
  elif sel=="2":
    change_telegram_account()
    menu()
  elif sel=="3":
    main()
  elif sel=="4":
    os.system("rm -r sessions")
    os.system("rm number.txt")
    clear()
    print(f"{r}Déconnexion réussie{S}")
    time.sleep(4)
    menu()
  elif sel=="5":
    manage_insta_accounts()
  elif sel=="6":
    update_bot()
  elif sel=="0":
    exit()
  else:
    menu()
def number():
  clear()
  try:
    phone=open("number.txt","r").read()
  except:
    phone=input(f"{o}[{V}?{o}] Numéro de téléphone T/G : {vi}")
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
    try:
        client.connect()
    except sqlite3.OperationalError as e:
        if "database is locked" in str(e):
            print(f"{R}La base de données de session est verrouillée.{S}")
            print(f"{J}Cela peut se produire si le script a été mal arrêté. Essayez de supprimer le dossier 'sessions' et réessayez.{S}")
            time.sleep(5)
            exit()
        else:
            print(f"{R}Erreur de connexion Telethon: {e}{S}")
            exit()
    except Exception as e:
        print(f"{R}Une erreur inattendue est survenue: {e}{S}")
        exit()

    
    if not client.is_user_authorized():
        try:
            client.send_code_request(phone=phone)
            clear()

            
            if os.path.exists("number.txt"):
                with open("number.txt", "r") as f:
                    number = f.read().strip()
            else:
                number = "Inconnu"

            print(f"[*] Votre numéro : {number}")
            code = input("[?] Entrez le code reçu : ")

            client.sign_in(phone=phone, code=code)
            clear()

        except PhoneNumberBannedError:
            clear()
            print(f"{r}[!] Le numéro de téléphone {phone} a été banni par Telegram.{S}")
            print(f"{J}[-] Veuillez utiliser un autre numéro.{S}")
            try:
                os.remove("number.txt")
            except OSError:
                pass
            time.sleep(4)
            menu()
            return # Important to exit the function here
        except PhoneNumberInvalidError:
            clear()
            print(f"{r}[!] Le numéro de téléphone {phone} est invalide.{S}")
            print(f"{J}[-] Veuillez vérifier le numéro et réessayer.{S}")
            try:
                os.remove("number.txt")
            except OSError:
                pass
            time.sleep(4)
            menu()
            return # Important to exit the function here
        except SessionPasswordNeededError:
            pw2fa = input("[?] Entrez le mot de passe (2FA) : ")
            client.sign_in(phone=phone, password=pw2fa)

    
    if not return_data:
        me = client.get_me()
        print(f"[√] Compte : {me.first_name} {me.last_name}")
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
      print(f"{vi}{o}Nom d'utilisateur : {vi}{user}")
      pwd=input(f"{o}Mot de passe : {vi}")
      s_acc=open(os.path.join(BASE_DIR, "Compte.txt"),'a')
      s_acc.write(f"{user}|{pwd}\n")
      s_acc.close()
      continue
    elif "✅" in acc:
      cuser=acc.split("✅ ")[1].split(" (")[0]
      print(f"{vi}{o}Nom d'utilisateur : {vi}{cuser}")
      pwd=input(f"{o}Mot de passe : {vi}")
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
    path=os.path.join(BASE_DIR, "insta-acct.txt")
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
          print(f"{B}[{R}X{B}] {user}{S} {black}(Vérifiez ce compte)")
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
        print(f"{o}[{B}•{o}] Nom d'utilisateur : {v}{user}{S}")
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
      u=(f"{r}Aucun fichier trouvé : SmmKingdomTask/insta-acct.txt\n{S}")
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
        print(f"{vi}Lien du post : {B}{link}")
        like=likes(link,cooks)
        if "ok" in like:
          print(f"{vi}[{V}√{vi}] {V}Like réussi{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Échec du Like{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
      elif "Follow" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}Lien utilisateur : {B}{link}")
        follow=followers(link,cooks)
        if "ok" in follow:
          print(f"{vi}[{V}√{vi}] {V}Follow réussi{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Échec du Follow{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
      elif "the comment" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}Lien du commentaire : {B}{link}")
        time.sleep(2)
        mss=coms(user)
        print(f"{J}{mss}")
        comms=comment(link,cooks,mss)
        if "ok" in comms:
          print(f"{vi}[{V}+{vi}] {V}Commentaire réussi{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Échec du commentaire{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
      elif "Stories" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}Lien des stories : {B}{link}")
        story(link,cooks)
        time.sleep(2)
        print(f"{vi}[{V}√{vi}] {V}Vue des stories réussie{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        task(cooks,user)
      elif "Open the video" in mss:
        link=re.search('▪️ Link :\n(.*?)\n▪️ Action :',str(mss)).group(1)
        print(f"{vi}Lien de la TV : {B}{link}")
        Tv(link,cooks)
        print(f"{vi}[{V}√{vi}] {V}Vue de la TV réussie{S}")
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
        print(f"{vi}Lien du commentaire : {B}{link}")
        print(f"{J}{mss}")
        comms=comment(link,cooks,mss)
        if "ok" in comms:
          print(f"{vi}[{V}√{vi}] {V}Commentaire réussi{S}")
          client.send_message(entity=channel_entity, message="✅Completed")
          task(cooks,user)
        else:
          print(f"{vi}[{R}x{vi}] {R}Échec du commentaire{S}")
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
        print(f"{o}ID du commentaire : {vi}{uid}{S}")
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de connexion{S}\r")
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
        sys.stdout.write(f"\r{r}Pas de connexion{S}\r")
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
    sys.stdout.write(f"\r{r}Pas de connexion{S}\r")
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
        print(f"{o}ID du post : {vi}{uid}{S}")
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de connexion{S}\r")
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
        sys.stdout.write(f"\r{r}Pas de connexion{S}\r")
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
        print(f"{o}ID utilisateur : {vi}{uid}{S}")
    except requests.exceptions.ConnectionError:
        sys.stdout.write(f"\r{r}Pas de connexion{S}\r")
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
        sys.stdout.write(f"\r{r}Pas de connexion{S}\r")
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
  print(f"{o}[{V}1{o}] Cookie manuel")
  print(f"{o}[{V}2{o}] Récupérer les cookies d'un fichier")
  print(f"{o}═════════════════════════════════════════")
  sel=input(f"{o}[{V}?{o}] Votre choix : {B}")
  if sel=="1":
    cooks()
  elif sel=="2":
    dump()
  else:
    main()
def cooks():
  clear()
  user=input(f"{o}[{V}?{o}]Nom d'utilisateur (ou 0 pour annuler) : {B}")
  if user == '0':
      main()
      return
      
  pwd=input(f"{o}[{V}?{o}]Mot de passe (ou 0 pour annuler) : {B}")
  if pwd == '0':
      main()
      return

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
    print(f"{B}[{V}SUCCÈS{B}] {V}{user} {B}| {V}{pwd}")
    print(f"{B}[{V}COOKIE{B}] {V}{cookies}")
    s_acc=open(os.path.join(BASE_DIR, "insta-acct.txt"),'a')
    s_acc.write(f"{user}|{cookies}\n")
    s_acc.close()
    remove()
    while True:
        choice = input(f"{o}[{V}?{o}] Ajouter un autre compte ? (o/n) : {B}").lower()
        if choice == 'o':
            cooks()
            return
        elif choice == 'n':
            main()
            return
        else:
            print(f"{R}Choix invalide. Veuillez répondre par 'o' ou 'n'.{S}")
  else:
    print(f"{B}[{R}!{B}]Identifiants incorrects {r}{user}{S} {B}| {r}{pwd}{S}")
    time.sleep(2)
    cooks()
def remove():
  input_file = os.path.join(BASE_DIR, "insta-acct.txt")
  if not os.path.exists(input_file):
      return

  unique_lines = {}
  with open(input_file, 'r') as infile:
      for line in infile:
          line = line.strip()
          if '|' in line:
              user_id = line.split('|')[0]
              unique_lines[user_id] = line

  with open(input_file, 'w') as outfile:
      for line in unique_lines.values():
          outfile.write(line + '\n')
  print(f"{B}[{V}√{B}] Suppression automatique des doublons réussie")

def dump():
  global comptes
  os.system("clear")
  print(logo)
  path=input(f"{o}[{V}+{o}]Chemin du fichier : {B}")
  if os.path.exists(path):
    for x in open(path,'r').readlines():
      comptes.append(x.strip())
    base()
  else:
    os.system("clear")
    i=(f"{r}Aucun fichier détecté\n{S}")
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
      print(f"{B}[{V}SUCCÈS{B}] {V}{user} {B}| {V}{pwd}")
      print(f"{B}[{V}COOKIE{B}] {V}{cookies}")
      s_acc=open(os.path.join(BASE_DIR, "insta-acct.txt"),'a')
      s_acc.write(f"{user}|{cookies}\n")
      s_acc.close()
      remove()
      continue
    else:
      print(f"{B}[{R}!{B}]Identifiants incorrects {r}{user}{S} {B}| {r}{pwd}{S}")
      continue
  input(f"{o}[{B}•{o}]Appuyez sur Entrée pour revenir en arrière")
  main()

def verify_online_subscription(key_to_check, auth_file):
    """Vérifie la clé d'abonnement en ligne et met à jour le fichier local."""
    api_url = f"https://passportdl.pythonanywhere.com/api/check_status?key={key_to_check}"
    print(f"{Bl}Vérification de l'abonnement en ligne...{S}")
    try:
        response = requests.get(api_url, timeout=15)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "active" and "expires_on" in data:
                expire_str = data["expires_on"]
                with open(auth_file, 'w') as f:
                    f.write(key_to_check + "\n")
                    f.write(expire_str + "\n")
                print(f"{V}Abonnement activé avec succès ! Expire le : {expire_str}{S}")
                time.sleep(3)
                return True
            else:
                print(f"{R}La clé n'est pas valide ou l'abonnement est inactif.{S}")
                print(f"{J}Message du serveur : {data.get('message', 'Aucun message')}{S}")
                time.sleep(3)
                return False
        else:
            print(f"{R}Erreur du serveur de vérification (Code: {response.status_code}).{S}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"{R}Impossible de contacter le serveur de vérification : {e}{S}")
        return False

def key():
    auth_file = os.path.expanduser("~/.smmkingdom_auth")
    
    # Générer une clé unique pour cette tentative de paiement
    av = "Pro"
    ar = "JK"
    centre = "".join(random.SystemRandom().choice("AZERTYUIOPQSDFGHJKLMWXCVBNabcdefghijklmnopqrstuvwxyz") for i in range(30))
    apv = f"{av}{centre}{ar}"
    os.system("clear")
    
    la = (f"{r}Vous n'êtes pas encore approuvé pour cet outil.{S}\n"
          f"{B}[{V}≈{B}] {Bl}Votre clé: {o}{apv}\n"
          f"{B}[{V}≈{B}]{Bl} Veuillez copier cette clé et l'utiliser sur le site de paiement.\n"
          f"{B}[{V}≈{B}] {Bl}Site de paiement: {o}https://passportdl.pythonanywhere.com/\n")
    
    for lax in la:
        print(lax, end='', flush=True)
        time.sleep(0.05)
    
    time.sleep(2)
    ouvrir_site_paiement()
    
    while True:
        input(f"\n{J}Appuyez sur Entrée APRÈS avoir effectué le paiement pour vérifier...{S}")
        if verify_online_subscription(apv, auth_file):
            menu() # L'abonnement est actif, on lance le menu
            break
        else:
            print(f"{J}Veuillez réessayer la vérification ou contacter le support si le problème persiste.{S}")

def check_subscription():
    auth_file = os.path.expanduser("~/.smmkingdom_auth")
    if os.path.exists(auth_file):
        with open(auth_file, 'r') as f:
            lines = f.read().splitlines()
            if len(lines) >= 2:
                key, expire_str = lines[0].strip(), lines[1].strip()
                try:
                    expire_date = datetime.datetime.strptime(expire_str, "%Y-%m-%d")
                    if expire_date >= datetime.datetime.now():
                        print(f"{V}Abonnement local valide trouvé. Expire le: {expire_str}{S}")
                        time.sleep(2)
                        menu()
                        return
                    else:
                        print(f"{r}Votre abonnement local a expiré le {expire_str}.{S}")
                except (ValueError, IndexError):
                    pass # Fichier corrompu, on continue pour appeler key()
    
    # Si aucun abonnement local valide n'est trouvé, on lance le processus de clé
    key()
    return

def ouvrir_site_paiement():
    url = "https://passportdl.pythonanywhere.com"
    print(f"{Bl}Ouverture du site de paiement: {o}{url}{S}")
    try:
        if sys.platform.startswith('linux'):
            # Pour Termux, `xdg-open` peut ne pas être disponible, utiliser `am start`
            if "com.termux" in os.environ.get("PREFIX", ""):
                os.system(f"am start -a android.intent.action.VIEW -d {url}")
            else:
                os.system(f"xdg-open {url}")
        elif sys.platform.startswith('win'):
            os.startfile(url)
        elif sys.platform.startswith('darwin'):
            os.system(f"open {url}")
        else:
            print(f"Veuillez ouvrir ce lien dans votre navigateur : {url}")
    except Exception as e:
        print(f"{R}Impossible d'ouvrir le navigateur automatiquement. Erreur : {e}{S}")
        print(f"Veuillez ouvrir ce lien manuellement : {url}")

def update_bot():
    clear()
    print(f"{o}--- Mise à jour du Bot ---{S}")
    try:
        print(f"{Bl}Téléchargement de la dernière version...{S}")
        url = "https://raw.githubusercontent.com/TRACKbest/nui/main/smm.py"
        response = requests.get(url)
        response.raise_for_status() # Lève une exception si le téléchargement échoue
        
        with open(__file__, 'w', encoding='utf-8') as f:
            f.write(response.text)
            
        print(f"{V}Mise à jour réussie ! Le script va redémarrer.{S}")
        time.sleep(3)
        # Redémarre le script
        os.execv(sys.executable, ['python'] + sys.argv)
    except requests.exceptions.RequestException as e:
        print(f"{R}Erreur lors du téléchargement de la mise à jour: {e}{S}")
        print(f"{J}Veuillez réessayer plus tard ou mettre à jour manuellement depuis GitHub.{S}")
        time.sleep(5)
        menu()
    except Exception as e:
        print(f"{R}Une erreur est survenue lors de la mise à jour: {e}{S}")
        time.sleep(5)
        menu()

def manage_insta_accounts():
    clear()
    path = os.path.join(BASE_DIR, "insta-acct.txt")
    if not os.path.exists(path):
        print(f"{r}Le fichier des comptes Instagram (insta-acct.txt) est introuvable.{S}")
        time.sleep(2)
        menu()
        return

    with open(path, 'r') as f:
        accounts = f.readlines()

    if not accounts:
        print(f"{r}Aucun compte Instagram n'a été trouvé dans le fichier.{S}")
        time.sleep(2)
        menu()
        return

    print(f"{o}--- Comptes Instagram ---{S}")
    for i, acc_line in enumerate(accounts):
        user = acc_line.strip().split('|')[0]
        print(f"{o}[{V}{i+1}{o}] {B}{user}{S}")
    print(f"{o}--------------------------{S}")
    print(f"{o}[{V}0{o}] Retour au menu")

    try:
        choice = input(f"{o}[{V}?{o}] Sélectionnez un compte à supprimer (ou 0 pour revenir) : {B}")
        choice_index = int(choice)

        if choice_index == 0:
            menu()
            return
        
        if 1 <= choice_index <= len(accounts):
            account_to_delete = accounts[choice_index - 1].strip().split('|')[0]
            del accounts[choice_index - 1]
            
            with open(path, 'w') as f:
                f.writelines(accounts)
            
            print(f"{V}Le compte '{account_to_delete}' a été supprimé.{S}")
            time.sleep(2)
            manage_insta_accounts()
        else:
            print(f"{r}Choix invalide.{S}")
            time.sleep(2)
            manage_insta_accounts()

    except ValueError:
        print(f"{r}Entrée invalide. Veuillez saisir un numéro.{S}")
        time.sleep(2)
        manage_insta_accounts()

def change_telegram_account():
    clear()
    print(f"{J}Cette option va supprimer le compte Telegram sauvegardé pour vous permettre d'en connecter un nouveau.{S}")
    time.sleep(2)
    
    # Supprimer le numéro de téléphone sauvegardé
    if os.path.exists("number.txt"):
        os.remove("number.txt")
        print(f"{V}Ancien numéro de téléphone supprimé.{S}")

    # Supprimer le dossier de session pour forcer une nouvelle connexion complète
    session_dir = "sessions"
    if os.path.exists(session_dir):
        try:
            shutil.rmtree(session_dir)
            print(f"{V}Ancien dossier de session supprimé.{S}")
        except OSError as e:
            print(f"{R}Erreur lors de la suppression du dossier de session : {e}.{S}")

    print(f"\n{V}Réinitialisation terminée.{S}")
    print(f"{J}La prochaine fois que vous démarrerez les tâches (option 1), il vous sera demandé un nouveau numéro.{S}")
    time.sleep(4)

if __name__ == "__main__":
    try:
        check_subscription()
    except KeyboardInterrupt:
        print(f"\n{R}Interruption détectée. Fermeture du script...{S}")
    finally:
        if clien and clien[0].is_connected():
            print(f"{Bl}Déconnexion du client Telegram...{S}")
            try:
                clien[0].disconnect()
            except sqlite3.OperationalError as e:
                print(f"{J}Avertissement : La base de données de session était verrouillée lors de la déconnexion. {e}{S}")
        print(f"{V}Script terminé.{S}")

menu()
