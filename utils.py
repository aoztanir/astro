import requests
import config
import time 
def get_token(code: str, tries=0):
  data = {
    'client_id': config.CLIENT_ID,
    'client_secret': config.CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': config.REDIRECT_URI,
    'scope': 'identify guilds'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  print(code)
  
 
  try:
    resp = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
  
    resp.raise_for_status()
    return resp.json()['access_token']
  except Exception as e:
    print(e)
    if "429" in str(e):
      if tries>3:
        return None
      time.sleep(2)
      tries=tries+1
      return get_token(code, tries)
    else:
      return None

def get_user_guilds(token: str, tries=0):
  resp = requests.get("https://discord.com/api/v6/users/@me/guilds", headers={"Authorization": f"Bearer {token}"})
  try:
    resp.raise_for_status()
  except Exception as e:
    if "429" in str(e):
      if tries>3:
        return None
      time.sleep(2)
      tries=tries+1
      return get_user_guilds(token, tries)
    else:
      return None
  return resp.json()

def get_bot_guilds(tries=0):
  token = config.BOT_TOKEN
  resp = requests.get("https://discord.com/api/v6/users/@me/guilds", headers={"Authorization": f"Bot {token}"})
  try:
    resp.raise_for_status()
  except Exception as e:
    print(e)
    if "429" in str(e):
      if tries>3:
        return None
      time.sleep(2)
      tries=tries+1
      return get_bot_guilds(tries)
    else:
      return None
  return resp.json()

def get_admin_bool(guild_id, bot_guilds: list):
  # mutual_guilds = [guild for guild in user_guilds if guild['id'] in map(lambda i: i['id'], bot_guilds) and (guild['permissions']& 0x000000008)==0x000000008]
  # mutual_guilds = [guild for guild in user_guilds if guild['id'] == str(guild_id) and (guild['permissions']& 0x000000008)==0x000000008]
  for guild in bot_guilds:
    if guild['id']==str(guild_id):
      if (guild['permissions']& 0x000000008)==0x000000008:
        return True
  return False

def get_mutal_guilds(user_guilds: list, bot_guilds: list):
  # mutual_guilds = [guild for guild in user_guilds if guild['id'] in map(lambda i: i['id'], bot_guilds) and (guild['permissions']& 0x000000008)==0x000000008]
  mutual_guilds = [guild for guild in user_guilds if guild['id'] in map(lambda i: i['id'], bot_guilds)]
  return mutual_guilds

def get_inv_guilds(user_guilds: list, bot_guilds: list):
  non_mutual_guilds = [guild for guild in user_guilds if guild['id'] not in map(lambda i: i['id'], bot_guilds) and (guild['permissions']& 0x000000008)==0x000000008]
  return non_mutual_guilds

def get_guild_data(guild_id: int, tries=0):
  token=config.BOT_TOKEN
  resp = requests.get(f"https://discord.com/api/v6/guilds/{guild_id}", headers={"Authorization": f"Bot {token}"})
  try:
    resp.raise_for_status()
    return resp.json()
  except Exception as e:
    if "429" in str(e):
      if tries>3:
        return None
      time.sleep(2)
      tries=tries+1
      return get_guild_data(guild_id, tries)
    else:
      return None

def get_channels(guild_id: int, tries=0):
  token=config.BOT_TOKEN
  resp = requests.get(f"https://discord.com/api/v6/guilds/{guild_id}/channels", headers={"Authorization": f"Bot {token}"})
  try:
    resp.raise_for_status()
    return resp.json()
  except Exception as e:
    if "429" in str(e):
      if tries>3:
        return None
      time.sleep(2)
      tries=tries+1
      return get_channels(guild_id, tries)
    else:
      return None

def get_user_data(token: str, tries=0):
  resp = requests.get("https://discord.com/api/users/@me", headers={"Authorization": f"Bearer {token}"})
  try:
    resp.raise_for_status()
    return resp.json()
  except Exception as e:
    if "429" in str(e):
      if tries>3:
        return None
      time.sleep(2)
      tries=tries+1
      return get_user_data(token, tries)
    else:
      return None


def get_astro_guild_data(guild_id):
  id=config.CLIENT_ID
  token=config.BOT_TOKEN
  resp = requests.get(f"https://discord.com/api/v6/guilds/{guild_id}/members/{id}", headers={"Authorization": f"Bot {token}"})
  resp.raise_for_status()
  return resp.json()

def get_member_guild(guild_id, token, id):
  # id=config.CLIENT_ID
  # token=config.BOT_TOKEN
  resp = requests.get(f"https://discord.com/api/v6/guilds/{guild_id}/members/{id}", headers={"Authorization": f"Bearer {token}"})
  resp.raise_for_status()
  return resp.json()
  