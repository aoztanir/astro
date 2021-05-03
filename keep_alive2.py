from flask import Flask, render_template, request, session, jsonify, redirect
import os
import requests
import flask
import random, string
# from oauth import Oauth
from threading import Thread
from replit import db
from utils import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "test123"


ok_chars = string.ascii_letters + string.digits
@app.route("/")
def home():
  user_info=None
  state=False
  discriminator=None
  if 'token' in session:
    state=True
    user_info = get_user_data(session.get('token'))
    discriminator = int(user_info['discriminator'])%5
  return render_template('index.html',userInfo=user_info, state=state, discriminator=discriminator)

@app.route('/logout')
def logout():
  session.clear()
  return redirect("/")

@app.route('/oauth/discord')
def oauth():
  token = get_token(request.args.get('code'))
  session['token']= token
  return redirect("/dashboard")
  # user_guilds = get_user_guilds(token)
  # bot_guilds = get_bot_guilds()
  # mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
  # return jsonify(mutual_guilds)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('/404.html'), 404


@app.route('/astro-is-ready')
def astroReady():
	rand_ammnt = random.randint(10, 100)
	random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))
	return render_template('/astro-is-ready.html', random_str=random_str)

@app.route('/dashboard')
def dashboard():
  try:
    if 'token' not in session:
      return redirect("/login")
    user_guilds = get_user_guilds(session.get('token'))
    bot_guilds = get_bot_guilds()
    mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)
    guilds_to_inv = get_inv_guilds(user_guilds, bot_guilds)
    user_info = get_user_data(session.get('token'))
    print(user_info)
    return render_template('dashboardNice.html', guilds=mutual_guilds,guildsWithout=guilds_to_inv, userInfo = user_info, discriminator = int(user_info['discriminator'])%5)
  except Exception as e:
    print(e)
    return redirect('/logout')

# @app.route('/submit/<guild_id>')
# def submit(guild_id: int):
#   #########################ADD TRY CATCH
#   if 'token' not in session:
#       return redirect("/login")
  
#   user_guilds = get_user_guilds(session.get('token'))
#   bot_guilds = get_bot_guilds()
#   status=False
#   mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)

#   for element in mutual_guilds:
#     if guild_id == element["id"]:
#       status=True
#   if status==False:
#     return redirect('/dashboard')
  
#   prefix = request.args.get('prefix')
#   try:
#     db[str(guild_id)]=str(prefix)
#   except:
#     return redirect(f'/dashboard')
#   return redirect(f'/guild/{guild_id}')
#   # password = request.args.get('password')


@app.route('/guild/<guild_id>', methods=["GET", "POST"])
def guild(guild_id: int):
  channels=[]
  
  try:
    if 'token' not in session:
      return redirect("/login")
    user_guilds = get_user_guilds(session.get('token'))
    bot_guilds = get_bot_guilds()
    status=False
    mutual_guilds = get_mutal_guilds(user_guilds, bot_guilds)

    for element in mutual_guilds:
      if guild_id == element["id"]:
        status=True
    if status==False:
      return redirect('/dashboard')
  
    # guilds_to_inv = get_inv_guilds(user_guilds, bot_guilds)
    user_info = get_user_data(session.get('token'))
    # print(user_info)
    guild_info = get_guild_data(guild_id)
    channelsa = get_channels(guild_id)
    # astroGuildData=get_astro_guild_data(guild_info["id"])
    # astroAdmin=False
    # print(guild_info)
    astroAdmin=get_admin_bool(guild_id, bot_guilds)
    # print(astroAdmin)
    
    # if (guild_info['permissions']& 0x000000008)==0x000000008:
    #   astroAdmin=True
    # print(astroAdmin)
    # for role in astroGuildData['roles']:
    #   for element in guildRoles:
    #     if role['id']==element['id']:
    #       if element[]
    # userGuildData=get_member_guild(guild_info['id'], session.get('token'), user_info['id'])

    try:
      channelsa.pop(0)
      channelsa.pop(0)
    except:
      pass
    # print(channels)
    # for element in channelsa:
      
    #   print(element['name'])
    #   print(str(element['permission_overwrites']))
    #   # print(element['permission_overwrites']['allow']& 0x000000008)
    #   print()
    channels = [x for x in channelsa if x['type']==0]


    if not guild_info:
      return redirect("/dashboard")
    # print(guild_info)
    
    try:
      prefix=db["prefixes"][str(guild_info["id"])]
    except:
      prefix="."
    
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
    # print("QUEUE DASH"+queue)
    admin=False
    # print(guild_info)
    for guild in user_guilds:
      if guild['id']==guild_info['id']:
        print(guild['id'])
        if (guild['permissions']& 0x000000008)==0x000000008:
          admin=True
    roles=guild_info['roles']
    # for element in guild_info['roles']:
    #   print(element['id'])
    #   if element['id']==user_info['id']:
    #     print(element['permissions'])
    #     if element['permissions']==0x000000008:
    #       admin=True
    volume=100
    mod_words=[]
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
      mod_words=db["mod_words"][str(guild_id)]["words"]
    except:
      db["mod_words"][str(guild_id)]={}
      db["mod_words"][str(guild_id)]["words"]=[]
      mod_words=db["mod_words"][str(guild_id)]["words"]
    
    # print(str(db["mod_words"][str(guild_id)]["words"]))
    # print(user_info['id'])
    if user_info['id']==str(608778878835621900):
      print("ADMINISTRATOR ENTERED")
      admin=True

    #FORM SETTING
    if request.method == 'POST':
      print("POSTING")
      data = request.form
      # print(data)
      #####PREFIX
      try:
        prefixNew = request.form.get('prefix')
        if prefixNew==None:
          pass
        else:
          db["prefixes"][str(guild_info["id"])]=str(prefixNew)
          prefix=prefixNew
      except:
        pass

      #####MOD WORDS
      # try:
      #   xTemp = db["mod_words"][str(guild_id)]["words"]
      # except:
      #   db["mod_words"][str(guild_id)]["words"]=[]
      modState=False
      clearState=False
      try:
        f = request.form
        for key in f.keys():
          for value in f.getlist(key):
            
            if "mod_words" in str(key):
              clearState=True
              if modState==False:
                db["mod_words"][str(guild_id)]["words"].clear()
                modState=True
              db["mod_words"][str(guild_id)]["words"].append(str(value))
              print (key,":",value)

        try:
          prefixTemp = request.form.get('prefix')
          if prefixNew==None:
            pass
          else:
            if clearState!=True:
              db["mod_words"][str(guild_id)]["words"].clear()
        except:
          pass
        
        # data = request.form.get("mod_words")
        # print("111111 "+ str(data))
        # data = request.form.get("mod_words1")
        # print("222222 " +str(data))
        # mod_words = request.form.get('mod_words')
        # print(mod_words)
      except Exception as e:
        print(e)
      


      # print("prev val"+str(list(db["announcement"])))
      ########## ANNOUNCEMENT ADD LIMITS and REQUIRED
      try:
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

          db["announcement"].append(msgData)
      except Exception as e:
        print(e)
      print(msgData)
      print("new val"+str(list(db["announcement"])))




      return redirect(request.path)
    else:
      return render_template('guild.html', guild=guild_info, userInfo=user_info, discriminator = int(user_info['discriminator'])%5, prefix=prefix, queueLength=queueLength, queue=queue, channels=channels, admin=admin, volume=volume, playing=playing, mod_words=mod_words, roles=roles, astroAdmin=astroAdmin)



  except Exception as e:
    print(e)
    return redirect('/dashboard')

@app.route('/inv')
def inv():
  return redirect("https://discord.com/api/oauth2/authorize?client_id=809609861456723988&permissions=8&redirect_uri=https%3A%2F%2Fteamastro.ml%2Foauth%2Fdiscord&scope=bot")

@app.route('/login')
def login():
	return redirect("https://discord.com/api/oauth2/authorize?client_id=809609861456723988&redirect_uri=https%3A%2F%2Fteamastro.ml%2Foauth%2Fdiscord&response_type=code&scope=identify%20guilds")


@app.route('/commands')
def commands():
	rand_ammnt = random.randint(10, 100)
	random_str = ''.join(random.choice(ok_chars) for a in range(rand_ammnt))
	return render_template('/commandsImage.html', random_str=random_str)



# @app.route("/", defaults={"path": ""}, methods=["GET", "POST", "DELETE"])
# @app.route("/<path:path>", methods=["GET", "POST", "DELETE"])
# def proxy(path):
#   print(db["queue"])
#   # url = os.environ["REPLIT_DB_URL"]
#   # print(url)
#   # if flask.request.path != "/":
#   #   url += flask.request.path

#   # req = requests.Request(flask.request.method, url, data=flask.request.form, params=flask.request.args).prepare()
#   # resp = sess.send(req)

#   # proxy_resp = flask.make_response(resp.text)

#   # proxy_resp.status_code = resp.status_code
#   # for k, v in resp.headers.items():
#   #   proxy_resp.headers[k] = v

#   return db["queue"][str(818961765520900126)]["queue"][0]

# @app.route("/login")
# def login():
# 	code = request.args.get("code")

# 	at = Oauth.get_access_token(code)
# 	session["token"] = at

# 	user = Oauth.get_user_json(at)
# 	user_name, user_id = user.get("username"), user.get("discriminator")

# 	return f"Success, logged in as {user_name}#{user_id}"

def run():
  app.run(host="0.0.0.0", port=8080)

def keep_alive():
  server = Thread(target=run)
  server.start()