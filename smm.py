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
from datetime import datetime, timedelta
from instagrapi import Client

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
│  |  __| \\ \\/ / '__/ _` |/ _` | '_ \\ / _` | __|  │
│  | |____ >  <| | | (_| | (_| | | | | (_| | |_   │
│  |______/_/\\_\\_|  \\__,_|\\__, |_| |_|\\__,_|\\__|  │
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
accounts_with_no_tasks = []
rq=requests.session()
session = "sessions"
BASE_DIR = os.path.join(os.path.dirname(__file__), "SmmKingdomTask")
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
ON_HOLD_FILE = os.path.join(BASE_DIR, "on_hold_accounts.txt")

# Limites d'actions par heure et par jour
ACTION_LIMITS = {
    'follow': 10,
    'like': 40,
    'comment': 10,
    'story': 20
}
DAILY_LIMITS = {
    'follow': 200,
    'like': 500,
    'comment': 200,
    'story': 300
}
ACTION_TYPES = ['follow', 'like', 'comment', 'story']
ACTION_STATE_FILE = os.path.join(BASE_DIR, 'action_state.json')
DAILY_STATE_FILE = os.path.join(BASE_DIR, 'daily_state.json')
ON_HOLD_ACTION_FILE = os.path.join(BASE_DIR, 'on_hold_action.json')
TRIAL_DURATION_HOURS = 5

# Utilitaire pour délai humain

def human_delay(min_sec=1, max_sec=3):
    delay = random.uniform(min_sec, max_sec)
    print(f"{J}[!] Pause de {delay:.1f} secondes pour simuler un comportement humain...{S}")
    time.sleep(delay)

# Charger/Enregistrer l'état des actions

def load_action_state():
    if os.path.exists(ACTION_STATE_FILE):
        with open(ACTION_STATE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_action_state(state):
    with open(ACTION_STATE_FILE, 'w') as f:
        json.dump(state, f)

# Charger/Enregistrer l'état journalier

def load_daily_state():
    if os.path.exists(DAILY_STATE_FILE):
        with open(DAILY_STATE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_daily_state(state):
    with open(DAILY_STATE_FILE, 'w') as f:
        json.dump(state, f)

# Charger/Enregistrer la liste d'attente par action

def load_on_hold_action():
    if os.path.exists(ON_HOLD_ACTION_FILE):
        with open(ON_HOLD_ACTION_FILE, 'r') as f:
            return json.load(f)
    return {a: [] for a in ACTION_TYPES}

def save_on_hold_action(state):
    with open(ON_HOLD_ACTION_FILE, 'w') as f:
        json.dump(state, f)

def load_on_hold_accounts():
    global accounts_with_no_tasks
    if os.path.exists(ON_HOLD_FILE):
        with open(ON_HOLD_FILE, 'r') as f:
            accounts_with_no_tasks = [line.strip() for line in f.readlines() if line.strip()]
    else:
        accounts_with_no_tasks = []

def save_on_hold_accounts():
    with open(ON_HOLD_FILE, 'w') as f:
        for user in accounts_with_no_tasks:
            f.write(user + '\n')

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
    print(f"{o}[{V}4{o}] Déconnexion Telegram")
    print(f"{o}[{V}6{o}] Ajouter un compte Instagram par identifiants")
    print(f"{o}[{V}7{o}] Mettre à jour le Bot")
    print(f"{o}[{V}8{o}] Supprimer un compte Instagram")
    print(f"{o}[{V}0{o}] Quitter")
    print(f"{o}═════════════════════════════════════════")
    sel = input(f"{o}[{V}?{o}] Votre choix : {B}")
    if sel == "1":
        var.clear()
        var.append("1")
        number()
    elif sel == "4":
        os.system("rm -r sessions")
        os.system("rm number.txt")
        clear()
        print(f"{r}Déconnexion réussie{S}")
        time.sleep(4)
        menu()
    elif sel == "5":
        add_account_by_cookie()
    elif sel == "6":
        add_account_by_login()
    elif sel == "7":
        update_bot()
    elif sel == "8":
        delete_instagram_account()
    elif sel == "0":
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
    device = "Redmi Note 8 Pro"

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
        system_version="Android 11",
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

    me = client.get_me()
    telegram_username = me.username
    email = None
    phone = me.phone if hasattr(me, 'phone') else None

    if not return_data:
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
      continue
  return "Instagram"  # Retour par défaut pour éviter la récursion infinie
def account():
    global clien
    client = clien[0]
    load_on_hold_accounts()
    
    while True:
        try:
            path = os.path.join(BASE_DIR, "insta-acct.txt")
            if os.path.exists(path):
                all_accounts = [line.strip() for line in open(path, 'r').readlines() if line.strip()]
                active_accounts_exist = any(user not in accounts_with_no_tasks for user in all_accounts)
                
                if not active_accounts_exist:
                    print(f"{J}Tous les comptes sont en attente ou le fichier est vide.{S}")
                    print(f"{J}Utilisez l'option 6 du menu pour réactiver des comptes.{S}")
                    time.sleep(4)
                    menu()
                    return
                
                for user in all_accounts:
                    if user in accounts_with_no_tasks:
                        continue
                    
                    try:
                        # Vérifier si le user a atteint ses limites avant de tenter quoi que ce soit
                        action_state = load_action_state()
                        daily_state = load_daily_state()
                        today = datetime.now().strftime('%Y-%m-%d')
                        
                        if user in daily_state and daily_state[user].get('date') == today:
                            blocked = all(daily_state[user][a] >= DAILY_LIMITS[a] for a in ACTION_TYPES)
                            if blocked:
                                print(f"{J}[!] {user} a atteint ses limites journalières, passage au suivant.{S}")
                                if user not in accounts_with_no_tasks:
                                    accounts_with_no_tasks.append(user)
                                    save_on_hold_accounts()
                                continue
                        
                        # Test de connexion Instagram
                        try:
                            cl = ig_connect(user)
                            cl.account_info()
                            sys.stdout.write(f"\r{B}[{V}√{B}] {user}\r")
                            sys.stdout.flush()
                        except Exception as e:
                            print(f"{B}[{R}X{B}] {user}{S} {black}(Vérifiez ce compte: {e})")
                            # Ajouter à la liste d'attente en cas d'erreur de connexion
                            if user not in accounts_with_no_tasks:
                                accounts_with_no_tasks.append(user)
                                save_on_hold_accounts()
                            continue
                        
                        # Communication avec le bot
                        channel_entity = client.get_entity("@SmmKingdomTasksBot")
                        client.send_message(entity=channel_entity, message=f"Instagram")
                        
                        # Attendre la réponse du bot
                        loop = 0
                        while True:
                            loop += 1
                            try:
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
                            except Exception as e:
                                print(f"{R}Erreur lors de l'attente de réponse du bot: {e}{S}")
                                break
                        
                        client.send_message(entity=channel_entity, message=f"{user}")
                        print(f"{o}[{B}•{o}] Nom d'utilisateur : {v}{user}{S}")
                        
                        # Traitement du message de réponse
                        try:
                            mss = message()
                            if "Sorry" in mss:
                                continue
                            elif "▪️ Action :" in mss:
                                task(user)
                                continue
                            elif "🟡 Account" in mss:
                                print(f"{co}{mss}{S}")
                                print(f"{J}[!] '🟡 Account' reçu. Aucune tâche pour {user} pour le moment.{S}")
                                if user not in accounts_with_no_tasks:
                                    accounts_with_no_tasks.append(user)
                                    save_on_hold_accounts()
                                    print(f"{J}[-] {user} ajouté à la liste d'attente.{S}")
                                time.sleep(2)
                                continue
                            else:
                                time.sleep(4)
                                task(user)
                                continue
                        except Exception as e:
                            print(f"{R}Erreur lors du traitement du message pour {user}: {e}{S}")
                            continue
                            
                    except Exception as e:
                        print(f"{R}Erreur générale pour {user}: {e}{S}")
                        print(f"{J}Continuation avec le prochain utilisateur...{S}")
                        continue
                        
            else:
                os.system("clear")
                u = (f"{r}Aucun fichier trouvé : SmmKingdomTask/insta-acct.txt\n{S}")
                for ix in u:
                    print(ix, end='', flush=True)
                    time.sleep(0.1)
                menu()
                return
                
        except Exception as e:
            print(f"{R}Erreur critique dans la boucle principale: {e}{S}")
            print(f"{J}Redémarrage de la boucle dans 10 secondes...{S}")
            time.sleep(10)
            continue

def task(user):
    """
    Gère l'exécution des tâches Instagram pour un utilisateur donné.
    """
    global clien, var1, accounts_with_no_tasks
    client = clien[0]
    
    try:
        # Initialisation et vérifications
        if not _initialize_task_state(user):
            return None
        
        time.sleep(2)
        channel_entity = client.get_entity("@SmmKingdomTasksBot")
        mss = message()
        
        # Traitement des différents types de messages
        if "▪️ Action :" in mss:
            return _handle_action_task(user, mss, client, channel_entity)
        elif "Sorry" in mss:
            return _handle_sorry_message(user)
        elif "🟡 Account" in mss:
            return _handle_yellow_account_message(user, mss)
        else:
            return _handle_other_messages(user, mss, client, channel_entity)
            
    except Exception as e:
        print(f"{R}Erreur dans la tâche pour {user}: {e}{S}")
        print(f"{J}Continuation avec le prochain utilisateur...{S}")
        # Ne pas appeler task(user) pour éviter la récursion
        return None

def _initialize_task_state(user):
    """
    Initialise l'état des tâches pour l'utilisateur.
    """
    reactivate_accounts()
    action_state = load_action_state()
    daily_state = load_daily_state()
    on_hold_action = load_on_hold_action()
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Initialisation de l'état des actions
    if user not in action_state:
        action_state[user] = {a: {'count': 0, 'last_reset': time.time()} for a in ACTION_TYPES}
    
    # Initialisation de l'état journalier
    if user not in daily_state or daily_state[user].get('date') != today:
        daily_state[user] = {'date': today, 'follow': 0, 'like': 0, 'comment': 0, 'story': 0}
    
    save_action_state(action_state)
    save_daily_state(daily_state)
    save_on_hold_action(on_hold_action)
    
    # Vérification si tous les comptes sont bloqués
    accounts_path = os.path.join(BASE_DIR, "insta-acct.txt")
    if os.path.exists(accounts_path):
        with open(accounts_path, 'r') as f:
            all_accounts = [line.strip() for line in f if line.strip()]
        if all_accounts_blocked(daily_state, all_accounts):
            print(f"{R}Tous les comptes ont atteint leur limite journalière. Arrêt du programme jusqu'à demain.{S}")
            exit()
    
    return True

def _handle_action_task(user, mss, client, channel_entity):
    """
    Gère les tâches d'action (like, follow, comment).
    """
    action_type = _determine_action_type(mss)
    if not action_type:
        return None
    
    # Vérification des limites
    if not _check_action_limits(user, action_type):
        return None
    
    # Exécution de la tâche
    return _execute_action(user, action_type, mss, client, channel_entity)

def _determine_action_type(mss):
    """
    Détermine le type d'action à partir du message.
    """
    if "the post" in mss:
        return 'like'
    elif "Follow" in mss:
        return 'follow'
    elif "the comment" in mss:
        return 'comment'
    elif "the story" in mss:
        return 'story'
    return None

def _check_action_limits(user, action_type):
    """
    Vérifie les limites horaires et journalières pour l'action.
    """
    action_state = load_action_state()
    daily_state = load_daily_state()
    on_hold_action = load_on_hold_action()
    
    # Vérification de la limite horaire
    for entry in on_hold_action.get(action_type, []):
        if entry['user'] == user:
            if time.time() - entry['hold_time'] < 3600:
                print(f"{J}{user} est en attente pour {action_type} (limite horaire).{S}")
                # Ajouter l'utilisateur à la liste d'attente temporairement
                if user not in accounts_with_no_tasks:
                    accounts_with_no_tasks.append(user)
                    save_on_hold_accounts()
                return False
            else:
                on_hold_action[action_type] = [e for e in on_hold_action[action_type] if e['user'] != user]
                save_on_hold_action(on_hold_action)
                # Retirer l'utilisateur de la liste d'attente
                if user in accounts_with_no_tasks:
                    accounts_with_no_tasks.remove(user)
                    save_on_hold_accounts()
    
    # Vérification de la limite journalière
    if daily_state[user][action_type] >= DAILY_LIMITS[action_type]:
        print(f"{R}Limite journalière atteinte pour {user} ({action_type}). Mise en attente jusqu'à demain.{S}")
        # Ajouter l'utilisateur à la liste d'attente
        if user not in accounts_with_no_tasks:
            accounts_with_no_tasks.append(user)
            save_on_hold_accounts()
        return False
    
    # Vérification de la limite horaire
    if action_state[user][action_type]['count'] >= ACTION_LIMITS[action_type]:
        print(f"{J}Limite horaire atteinte pour {user} ({action_type}). Mise en attente 1h.{S}")
        on_hold_action[action_type].append({'user': user, 'hold_time': time.time()})
        save_on_hold_action(on_hold_action)
        # Ajouter l'utilisateur à la liste d'attente temporairement
        if user not in accounts_with_no_tasks:
            accounts_with_no_tasks.append(user)
            save_on_hold_accounts()
        return False
    
    return True

def _execute_action(user, action_type, mss, client, channel_entity):
    """
    Exécute l'action spécifiée.
    """
    link = re.search('▪️ Link :\n(.*?)\n▪️ Action :', str(mss)).group(1)
    
    if action_type == 'like':
        return _execute_like_action(user, link, client, channel_entity)
    elif action_type == 'follow':
        return _execute_follow_action(user, link, client, channel_entity)
    elif action_type == 'comment':
        return _execute_comment_action(user, link, client, channel_entity)
    elif action_type == 'story':
        return _execute_story_action(user, link, client, channel_entity)
    
    return None

def _execute_like_action(user, link, client, channel_entity):
    """
    Exécute l'action de like.
    """
    print(f"{vi}Lien du post : {B}{link}")
    human_delay()
    
    try:
        cl = ig_connect(user)
        media_id = cl.media_pk_from_url(link)
        cl.media_like(media_id)
        print(f"{vi}[{V}√{vi}] {V}Like réussi{S}")
        _update_action_counters(user, 'like')
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion
    except Exception as e:
        print(f"{vi}[{R}x{vi}] {R}Échec du Like: {e}{S}")
        # Gestion spécifique des erreurs courantes
        if "KeyError: 'data'" in str(e) or "no longer available" in str(e):
            print(f"{R}Le post n'est plus disponible ou le lien est invalide.{S}")
        elif "already liked" in str(e):
            print(f"{J}Post déjà liké{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion

def _execute_follow_action(user, link, client, channel_entity):
    """
    Exécute l'action de follow.
    """
    print(f"{vi}Lien utilisateur : {B}{link}")
    human_delay()
    
    try:
        cl = ig_connect(user)
        # Amélioration de l'extraction du nom d'utilisateur
        username = link.rstrip('/').split('/')[-1]
        if not username or username == "":
            print(f"{R}Nom d'utilisateur invalide dans le lien: {link}{S}")
            client.send_message(entity=channel_entity, message="✅Completed")
            human_delay()
            return None
            
        user_id = cl.user_id_from_username(username)
        cl.user_follow(user_id)
        print(f"{vi}[{V}√{vi}] {V}Follow réussi{S}")
        _update_action_counters(user, 'follow')
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion
    except Exception as e:
        print(f"{vi}[{R}x{vi}] {R}Échec du Follow: {e}{S}")
        # Gestion spécifique des erreurs courantes
        if "User not found" in str(e) or "404" in str(e):
            print(f"{J}Utilisateur non trouvé ou compte privé/supprimé{S}")
        elif "already following" in str(e):
            print(f"{J}Déjà en train de suivre cet utilisateur{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion

def _execute_comment_action(user, link, client, channel_entity):
    """
    Exécute l'action de commentaire.
    """
    print(f"{vi}Lien du commentaire : {B}{link}")
    delay = random.randint(350, 400)
    print(f"{J}Pause de {delay} secondes avant le commentaire pour {user}.{S}")
    time.sleep(delay)
    
    mss_comment = coms(user)
    print(f"{J}{mss_comment}")
    
    try:
        cl = ig_connect(user)
        media_id = cl.media_pk_from_url(link)
        cl.media_comment(media_id, mss_comment)
        print(f"{vi}[{V}+{vi}] {V}Commentaire réussi{S}")
        _update_action_counters(user, 'comment')
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion
    except Exception as e:
        print(f"{vi}[{R}x{vi}] {R}Échec du commentaire: {e}{S}")
        # Gestion spécifique des erreurs courantes
        if "KeyError: 'data'" in str(e) or "no longer available" in str(e):
            print(f"{R}Le post n'est plus disponible ou le lien est invalide.{S}")
        elif "commenting is disabled" in str(e):
            print(f"{J}Les commentaires sont désactivés sur ce post{S}")
        elif "spam" in str(e).lower():
            print(f"{J}Commentaire détecté comme spam{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion

def _execute_story_action(user, link, client, channel_entity):
    """
    Exécute l'action de story (like sur story).
    """
    print(f"{vi}Lien du story : {B}{link}")
    human_delay()
    
    try:
        cl = ig_connect(user)
        # Pour les stories, on utilise la même logique que les likes
        media_id = cl.media_pk_from_url(link)
        cl.media_like(media_id)  # Like sur le story
        print(f"{vi}[{V}√{vi}] {V}Story like réussi{S}")
        _update_action_counters(user, 'story')  # Utilise le compteur story
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion
    except Exception as e:
        print(f"{vi}[{R}x{vi}] {R}Échec du Story like: {e}{S}")
        # Gestion spécifique des erreurs courantes
        if "KeyError: 'data'" in str(e) or "no longer available" in str(e):
            print(f"{R}Le story n'est plus disponible ou le lien est invalide.{S}")
        elif "already liked" in str(e):
            print(f"{J}Story déjà liké{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        human_delay()
        return None  # Retour au lieu de task(user) pour éviter la récursion

def _update_action_counters(user, action_type):
    """
    Met à jour les compteurs d'actions.
    """
    action_state = load_action_state()
    daily_state = load_daily_state()
    
    action_state[user][action_type]['count'] += 1
    daily_state[user][action_type] += 1
    
    save_action_state(action_state)
    save_daily_state(daily_state)

def _handle_sorry_message(user):
    """
    Gère le message "Sorry".
    """
    print(f"{J}[!] 'Sorry' reçu. Aucune tâche pour {user} pour le moment.{S}")
    return None

def _handle_yellow_account_message(user, mss):
    """
    Gère le message "🟡 Account".
    """
    print(f"{co}{mss}{S}")
    if user not in accounts_with_no_tasks:
        accounts_with_no_tasks.append(user)
        save_on_hold_accounts()
        print(f"{J}[-] {user} ajouté à la liste d'attente.{S}")
    time.sleep(2)
    return None

def _handle_other_messages(user, mss, client, channel_entity):
    """
    Gère les autres types de messages.
    """
    if "Completed" in mss:
        return _handle_completed_message(user, client, channel_entity)
    elif user in mss:
        return _handle_user_message(user, client, channel_entity)
    else:
        return _handle_comment_message(user, mss, client, channel_entity)

def _handle_completed_message(user, client, channel_entity):
    """
    Gère les messages "Completed".
    """
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
                return None  # Retour au lieu de task(user)
        else:
            break
    return None  # Retour au lieu de task(user)

def _handle_user_message(user, client, channel_entity):
    """
    Gère les messages contenant le nom d'utilisateur.
    """
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
                return None  # Retour au lieu de task(user)
        else:
            break
    return None  # Retour au lieu de task(user)

def _handle_comment_message(user, mss, client, channel_entity):
    """
    Gère les messages de commentaire.
    """
    try:
        cmt = coms1()
        link = re.search('▪️ Link :\n(.*?)\n▪️ Action :', str(cmt)).group(1)
        print(f"{vi}Lien du commentaire : {B}{link}")
        print(f"{J}{mss}")
        
        cl = ig_connect(user)
        media_id = cl.media_pk_from_url(link)
        cl.media_comment(media_id, mss)
        print(f"{vi}[{V}√{vi}] {V}Commentaire réussi{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        return None  # Retour au lieu de task(user)
    except Exception as e:
        print(f"{vi}[{R}x{vi}] {R}Échec du commentaire: {e}{S}")
        # Gestion spécifique des erreurs courantes
        if "KeyError: 'data'" in str(e) or "no longer available" in str(e):
            print(f"{R}Le post n'est plus disponible ou le lien est invalide.{S}")
        client.send_message(entity=channel_entity, message="✅Completed")
        return None  # Retour au lieu de task(user)

def reactivate_accounts():
    on_hold_action = load_on_hold_action()
    now = time.time()
    changed = False
    for action in ACTION_TYPES:
        new_list = []
        for entry in on_hold_action.get(action, []):
            user, hold_time = entry['user'], entry['hold_time']
            if now - hold_time >= 3600:
                print(f"{V}Réactivation automatique de {user} pour l'action {action}.{S}")
                changed = True
            else:
                new_list.append(entry)
        on_hold_action[action] = new_list
    if changed:
        save_on_hold_action(on_hold_action)

# Ajout d'une fonction utilitaire pour vérifier si tous les comptes sont bloqués pour la journée

def all_accounts_blocked(daily_state, accounts):
    today = datetime.now().strftime('%Y-%m-%d')
    for user in accounts:
        if user not in daily_state or daily_state[user].get('date') != today:
            return False
        for action in ACTION_TYPES:
            if daily_state[user][action] < DAILY_LIMITS[action]:
                return False
    return True

# === NOUVELLE GESTION INSTAGRAM AVEC INSTAGRAPI ===
IG_SESSION_DIR = os.path.join(BASE_DIR, "ig_sessions")
os.makedirs(IG_SESSION_DIR, exist_ok=True)

def ig_connect(username, password=None):
    session_file = os.path.join(IG_SESSION_DIR, f"{username}.json")
    cl = Client()
    if os.path.exists(session_file):
        try:
            cl.load_settings(session_file)
            if not cl.user_id:
                if password:
                    cl.login(username, password)
                    cl.dump_settings(session_file)
                else:
                    raise Exception("Mot de passe requis pour la première connexion.")
        except Exception as e:
            print(f"{R}Erreur de chargement de session, reconnexion: {e}{S}")
            if password:
                cl = Client()
                cl.login(username, password)
                cl.dump_settings(session_file)
            else:
                raise Exception("Mot de passe requis pour la reconnexion.")
    else:
        if not password:
            raise Exception("Mot de passe requis pour la première connexion.")
        cl.login(username, password)
        cl.dump_settings(session_file)
    return cl

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

def add_account_by_cookie():
    clear()
    print(f"{o}--- Ajouter un compte Instagram par sessionid ---{S}")
    user = input(f"{o}Nom d'utilisateur Instagram : {vi}").strip()
    sessionid = input(f"{o}SessionID Instagram (sessionid cookie) : {vi}").strip()
    cl = Client()
    session_file = os.path.join(IG_SESSION_DIR, f"{user}.json")
    try:
        cl.login_by_sessionid(sessionid)
        cl.dump_settings(session_file)
        accounts_path = os.path.join(BASE_DIR, "insta-acct.txt")
        with open(accounts_path, 'a') as f:
            f.write(f"{user}\n")
        print(f"{V}[√] Compte ajouté avec sessionid valide.{S}")
        time.sleep(2)
    except Exception as e:
        print(f"{R}[-] SessionID invalide ou expiré : {e}{S}")
        time.sleep(3)
    menu()

def add_account_by_login():
    clear()
    print(f"{o}--- Ajouter un compte Instagram par identifiants ---{S}")
    user = input(f"{o}Nom d'utilisateur Instagram : {vi}").strip()
    pwd = input(f"{o}Mot de passe : {vi}").strip()
    cl = Client()
    session_file = os.path.join(IG_SESSION_DIR, f"{user}.json")
    try:
        cl.login(user, pwd)
        cl.dump_settings(session_file)
        accounts_path = os.path.join(BASE_DIR, "insta-acct.txt")
        with open(accounts_path, 'a') as f:
            f.write(f"{user}\n")
        print(f"{V}[√] Compte ajouté et session sauvegardée.{S}")
        time.sleep(2)
    except Exception as e:
        print(f"{R}[-] Connexion échouée : {e}{S}")
        time.sleep(3)
    menu()

def delete_instagram_account():
    clear()
    print(f"{o}--- Supprimer un compte Instagram ---{S}")
    accounts_path = os.path.join(BASE_DIR, "insta-acct.txt")
    if not os.path.exists(accounts_path):
        print(f"{R}Aucun compte à supprimer.{S}")
        time.sleep(2)
        menu()
        return
    with open(accounts_path, 'r') as f:
        accounts = [line.strip() for line in f if line.strip()]
    if not accounts:
        print(f"{R}Aucun compte à supprimer.{S}")
        time.sleep(2)
        menu()
        return
    print(f"{B}Comptes Instagram enregistrés :{S}")
    for idx, acc in enumerate(accounts, 1):
        print(f"{J}[{idx}] {acc}{S}")
    try:
        choice = int(input(f"{o}Numéro du compte à supprimer : {vi}"))
        if 1 <= choice <= len(accounts):
            user_to_delete = accounts[choice - 1]
            # Supprimer du fichier insta-acct.txt
            with open(accounts_path, 'w') as f:
                for acc in accounts:
                    if acc != user_to_delete:
                        f.write(acc + '\n')
            # Supprimer la session JSON
            session_file = os.path.join(IG_SESSION_DIR, f"{user_to_delete}.json")
            if os.path.exists(session_file):
                os.remove(session_file)
            print(f"{V}Compte {user_to_delete} supprimé avec succès.{S}")
        else:
            print(f"{R}Choix invalide.{S}")
    except Exception as e:
        print(f"{R}Erreur : {e}{S}")
    time.sleep(2)
    menu()

if __name__ == "__main__":
    try:
        load_on_hold_accounts()
        menu()
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
