from flask import Flask
from flask_cors import *
from flask import Flask, render_template, request, session, jsonify, redirect
import os
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import quart
import random, string
# from oauth import Oauth
from threading import Thread
from replit import db
from utils import *
from ratelimit import limits




app= Flask(__name__)
# app = quart_cors(app)
# rate_limiter = RateLimiter(app)
limiter = Limiter(
    app,
    key_func=get_remote_address

)

@app.route('/api', methods=['GET','POST'])

@cross_origin(['https://teamastro.ml'])
def api():

  return{
    'time':1
  }

@app.route('/token/<code>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def oauth(code: str):
  token = get_token(code)
  # session['token']= token
  return {
    'token':token
  }

@app.route('/userinfo/<token>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def userData(token: str):
  userData = get_user_data(token)
  # session['token']= token
  return userData

@app.route('/guilds/<token>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def guilds(token: str):
  # userData = get_user_data(token)
  user_guilds = get_user_guilds(token)
  bot_guilds = get_bot_guilds()
  mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
  guilds_to_inv = get_inv_guilds(user_guilds, bot_guilds)

  
  return{
    'mutualGuilds':mutual_guilds,
    'guilds':guilds_to_inv,
  }
  # session['token']= token
  return userData


@app.route('/submitrole/<token>/<guildid>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def submitRole(token: str, guildid: str):
  guild_id=guildid
  userData = get_user_data(token)
  user_info=userData
  user_guilds = get_user_guilds(token)
  # bot_guilds = get_bot_guilds()
  # mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
  guild_info = get_guild_data(guildid)

  admin=False
  for guild in user_guilds:
    if guild['id']==guild_info['id']:
      # print(guild['id'])
      if (guild['permissions']& 0x000000008)==0x000000008:
        admin=True


  if admin ==False:
    return {
      "error" : True
    }

  msgData={}
  title = request.form.get('title')
  description = request.form.get('description')
  server = guild_id
  channel= request.form.get('channel')
  role= request.form.get('role')
  f = request.form
  color=request.form.get('color')
  color=str(color).strip("#")
  print(color)
  titles=[]
  values=[]
  roleAdds=[]
  roleToGives=[]
  emojis=[]
  for key in f.keys():
    for value in f.getlist(key):
      
      if "fieldTitle" in str(key):
        # clearState=True
        # if modState==False:
        #   db["mod_words"][str(guild_id)]["words"].clear()
          # modState=True
        titles.append(str(value))
        print (key,":",value)
      if "fieldValue" in str(key):
        # clearState=True
        # if modState==False:
        #   db["mod_words"][str(guild_id)]["words"].clear()
          # modState=True
        values.append(str(value))
        print (key,":",value)
      if "roleToGive" in str(key):
        roleToGives.append(str(value))
      if "emoji" in str(key):
        emojis.append(str(value))

  for i in range(len(emojis)):
    roleAdds.append({'role':roleToGives[i], 'emoji':emojis[i]})
  
  fields=[]
  for i in range(len(titles)):
    fields.append({'title':titles[i], 'value':values[i]})

  if title==None:
    pass
  else:

    msgData={'title':title, 
    'description':description, 
    'server': server, 
    'channel': channel,
    'pic': f"https://cdn.discordapp.com/avatars/{user_info['id']}/{user_info['avatar']}.png",
    'sent': False,
    'role': role,
    'fields': fields,
    'color': color,
    'roleAdds': roleAdds,
    'id': None,
    'name':user_info['username'] }
    print(msgData)
    try:
      db["reaction_roles"][str(guild_id)].append(msgData)
    except:
      db["reaction_roles"][str(guild_id)]=[]
      db["reaction_roles"][str(guild_id)].append(msgData)
    return { 'done': True
    }
  return {
        "error" : True
      }











@app.route('/removereactionrole/<token>/<guildid>/<index>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def removeReactionRole(token: str, guildid: str, index: int):
  guild_id=guildid
  userData = get_user_data(token)
  user_info=userData
  user_guilds = get_user_guilds(token)
  # bot_guilds = get_bot_guilds()
  # mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
  guild_info = get_guild_data(guildid)

  admin=False
  for guild in user_guilds:
    if guild['id']==guild_info['id']:
      # print(guild['id'])
      if (guild['permissions']& 0x000000008)==0x000000008:
        admin=True


  if admin ==False:
    return {
      "error" : True
    }
  print(index)
  db["reaction_roles"][str(guild_id)].pop(int(index))
  return "done"







@app.route('/submitannouncement/<token>/<guildid>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def submitAnnouncement(token: str, guildid: str):
  guild_id=guildid
  userData = get_user_data(token)
  user_info=userData
  user_guilds = get_user_guilds(token)
  # bot_guilds = get_bot_guilds()
  # mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
  guild_info = get_guild_data(guildid)

  admin=False
  for guild in user_guilds:
    if guild['id']==guild_info['id']:
      # print(guild['id'])
      if (guild['permissions']& 0x000000008)==0x000000008:
        admin=True


  if admin ==False:
    return {
      "error" : True
    }

  msgData={}
  title = request.form.get('title')
  description = request.form.get('description')
  server = guild_id
  channel= request.form.get('channel')
  role= request.form.get('role')
  f = request.form
  color=request.form.get('color')
  color=str(color).strip("#")
  print(color)
  titles=[]
  values=[]
  for key in f.keys():
    for value in f.getlist(key):
      
      if "fieldTitle" in str(key):
        # clearState=True
        # if modState==False:
        #   db["mod_words"][str(guild_id)]["words"].clear()
          # modState=True
        titles.append(str(value))
        print (key,":",value)
      if "fieldValue" in str(key):
        # clearState=True
        # if modState==False:
        #   db["mod_words"][str(guild_id)]["words"].clear()
          # modState=True
        values.append(str(value))
        print (key,":",value)
  fields=[]
  for i in range(len(titles)):
    fields.append({'title':titles[i], 'value':values[i]})
  
  # try:
  #   ping=request.form.get('ping')
  # except:
  #   ping="off"
  # if ping==None:
  #   ping="off"
  print(title)
  if title==None:
    pass
  else:
    print("hi")
    # msgData={'title':title, 
    # 'description':description, 
    # 'ping':ping, 'server': server, 
    # 'pic': f"https://cdn.discordapp.com/avatars/{user_info['id']}/{user_info['avatar']}.png",
    # 'name':user_info['name'] }
    # db["announcement"].clear()
    msgData={'title':title, 
    'description':description, 
    # 'ping':ping, 
    'server': server, 
    'channel': channel,
    'pic': f"https://cdn.discordapp.com/avatars/{user_info['id']}/{user_info['avatar']}.png",
    'role': role,
    'fields': fields,
    'color': color,

    'name':user_info['username'] }
    print(msgData)
    db["announcement"].append(msgData)
    return { 'done': True
    }
  return {
        "error" : True
      }
  
@app.route('/submitsettings/<token>/<guildid>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def submitSettings(token: str, guildid: str):
  guild_id=guildid
  # userData = get_user_data(token)
  user_guilds = get_user_guilds(token)
  # bot_guilds = get_bot_guilds()
  # mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
  guild_info = get_guild_data(guildid)

  admin=False
  for guild in user_guilds:
    if guild['id']==guild_info['id']:
      # print(guild['id'])
      if (guild['permissions']& 0x000000008)==0x000000008:
        admin=True


  if admin ==False:
    return {
      "error" : True
    }
  prefixNew = request.form.get('prefix')
  db["prefixes"][str(guild_info["id"])]=str(prefixNew)
  f = request.form
  db["mod_words"][str(guild_id)]["words"].clear()
  for key in f.keys():
    for value in f.getlist(key):
      print(key,":",value)
      if "modWords" in str(key):
        # clearState=True
        # if modState==False:
        
          # modState=True
        db["mod_words"][str(guild_id)]["words"].append(str(value))
        print("mod word appended")
  
  
  return {
    "modWords": list(db["mod_words"][str(guild_id)]["words"]),
    "prefix": list(db["prefixes"][str(guild_info["id"])])
  }

@app.route('/guild/<token>/<guildid>', methods=['GET','POST'])
# @limiter.limit("1/3seconds")
@cross_origin(['https://teamastro.ml'])
def guild(token: str, guildid: str):
  channels=[]
  guild_id=guildid
  userData = get_user_data(token)
  user_guilds = get_user_guilds(token)
  bot_guilds = get_bot_guilds()
  mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
  guild_info = get_guild_data(guildid)
  # print(guild_info)
  status=False
  try:
    prefix = db["prefixes"][str(guild_id)]
  except:
    prefix="."
  channelsa = get_channels(guild_id)
  roles=guild_info['roles']
  try:
    channelsa.pop(0)
    channelsa.pop(0)
  except:
    pass
  channels = [x for x in channelsa if x['type']==0]
  mod_words=[]
  try:
      mod_words=db["mod_words"][str(guild_id)]["words"]
  except:
    db["mod_words"][str(guild_id)]={}
    db["mod_words"][str(guild_id)]["words"]=[]
    mod_words=db["mod_words"][str(guild_id)]["words"]
  volume=100

  try:
    volume = db["volumes"][str(guild_id)]["volume"]
  except:
    volume= 100
  playing=None
  try:
    playing=db["playing"][str(guild_id)]
  except:
    playing=None

  try:
    queue = dict(db["queue"][str(guild_info["id"])])
    # names= list(db["queue"][str(guild_info["id"])]["name"])
    # links= list(db["queue"][str(guild_info["id"])]["link"])
    queueLength=len(db["queue"][str(guild_info["id"])]["name"])
    if queueLength>10:
      queueLength=10
  except:
    queue=None
    queueLength=0
    
  for element in mutual_guilds:
    if guild_id == element["id"]:
      status=True
  admin=False
  for guild in user_guilds:
    if guild['id']==guild_info['id']:
      # print(guild['id'])
      if (guild['permissions']& 0x000000008)==0x000000008:
        admin=True
  astroAdmin=get_admin_bool(guild_id, bot_guilds)
  if status==False:
    return {
      'error':True
    }
  try:
    queues = list(queue["name"])[:10]
    thumnails =list(queue["thumbnail"])[:10]
    links =list(queue["link"])[:10]
    durations = list(queue["duration"])[:10]
    requestors = list(queue["requestor"])[:10]
    
    volume = int(volume)
  except Exception as e:
    print("EXCEPTION"+str(e))
    queues = []
    thumnails =[]
    links = []
    durations = []
    requestors = []
    volume = 100
  try:
    playing =  dict(playing)
  except:
    playing =  {}
  rolesToAdd=[]
  for element in roles:
    if not (element['permissions']& 0x000000008)==0x000000008:
      if element['managed']==False:
        if not element["position"]==0:
          rolesToAdd.append(element)
  current_reaction_roles=[]    
  try:
    role_save=list(db["reaction_roles"][str(guild_id)])
    for i in range(len(role_save)):
      adds=[]
      desc=""
      for element in role_save[i]["roleAdds"]:
        adds.append({'role': element["role"], 'emoji': element["emoji"]})
        desc+=element["emoji"]+" -> "+element["role"]+" | "
      DATA ={
        'title': role_save[i]["title"],
        'roles': adds,
        'pic': role_save[i]["pic"],
        'desc': " | "+desc
      }
      current_reaction_roles.append(DATA)
  except Exception as e:
    print(e)

  
  # print(queue)
  return jsonify({
    'guild':guild_info,
    'admin':admin,
    'astroadmin': astroAdmin,
    'modWords':list(mod_words),
    'info':{
      'prefix': prefix,
      'modWords':list(mod_words),
      'channels':list(channels),
      'roles':list(roles),
      'rolesToAdd':list(rolesToAdd),
      'current_reaction_roles': current_reaction_roles
    },
    'userInfo':userData,

    'music':{
      # 'queue': queueLength,
      'queue':  list(queues),
      'thumbnails': list(thumnails),
      'links': list(links),
      'durations': list(durations),
      'requestors': list(requestors),
      'playing' : list(playing),
      'volume': int(volume),
      'playing': dict(playing)
    }
    
  })
  # session['token']= token
  # return userData


# @app.route('/music/<guildid>', methods=['GET','POST'])
# # @limiter.limit("1/3seconds")
# @cross_origin(['https://teamastro.ml'])
# def music( guildid: str):
#   guild_id=guildid
#   try:
#     volume = db["volumes"][str(guild_id)]["volume"]
#   except:
#     volume= 100
#   playing=None
#   try:
#     playing=db["playing"][str(guild_id)]
#   except:
#     playing=None

#   try:
#     queue = dict(db["queue"][str(guild_info["id"])])
#     # names= list(db["queue"][str(guild_info["id"])]["name"])
#     # links= list(db["queue"][str(guild_info["id"])]["link"])
#     queueLength=len(db["queue"][str(guild_info["id"])]["name"])
#     if queueLength>10:
#       queueLength=10
#   except:
#     queue=None
#     queueLength=0
#   # print(queue)
#   try:
#     queues = list(queue["name"])[:10]
#     thumnails =list(queue["thumbnail"])[:10]
#     links =list(queue["link"])[:10]
#     durations = list(queue["duration"])[:10]
#     requestors = list(queue["requestor"])[:10]
    
#     volume = int(volume)
#   except:
#     queues = []
#     thumnails =[]
#     links = []
#     durations = []
#     requestors = []
    
#   try:
#     playing =  dict(playing)
#   except:
#     playing =  {}

#   # print(queue)
#   return jsonify({
#     'music':{
#       # 'queue': queueLength,
#       'queue':  queues,
#       'thumbnails': thumnails,
#       'links': links,
#       'durations': durations,
#       'requestors': requestors,
#       'playing' : playing,
#       'volume': volume
#     }
    
#   })
#   # session['token']= token
#   # return userData





import subprocess

# if __name__ == '__main__':
#   app.run(host='0.0.0.0', port=8080)
def run():
  # Lava = Thread(target=os.system("java -jar Lavalink.jar"))
  # Lava.start()
  # subprocess.run(["java", " -jar Lavalink.jar"])
  app.run(host="0.0.0.0", port=8080)
  # os.system("java -jar Lavalink.jar")

def keep_alive():
  server = Thread(target=run)
  server.start()
  
  # Lava = Thread(target=os.system("java -jar Lavalink.jar"))
  # Lava.start()
















# from flask import Flask, render_template, request, session, jsonify, redirect
# import os
# import requests
# import flask
# import random, string
# # from oauth import Oauth
# from threading import Thread
# from replit import db
# from utils import *

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "test123"


# ok_chars = string.ascii_letters + string.digits
# @app.route("/")
# def home():
#   return redirect("https://astrodisc.ml")

# def run():
#   app.run(host="0.0.0.0", port=8080)

# def keep_alive():
#   server = Thread(target=run)
#   server.start()