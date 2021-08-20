
import os
import discord
import requests #to request http response
import json #to get that responce
import random
from replit import db
from keep_alive import keep_alive


my_secret = os.environ['Access_Token']

client = discord.Client()

sad_words = ["sad","fear","terrible","unhappy","angry","miserable","depressed"]

starter_encouragements = [
  "Cheer up!" , "You're a greatt person / bot! " ,"Stay there, Try to figure out.","Everything will be alright!"
]

if "responding" not in db.keys():
  db["responding"] = True


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  # to get that responce
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]


def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index] 
    db["encouragements"] = encouragements  




#register an event
@client.event

# THis will be caled when a bot is ready to start
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# As soon as bo is ready to work if it receives a message
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content  

#all bot msges by friends starts with $
# This is basic response structure
  if msg.startswith('$hello'):
    await message.channel.send('Hello!')

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))


  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("new ",1)[1] 
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.") 

  if msg.startswith("$del"):
    encouragements = []
    if "encouragemts" in db.keys():
      index =int(msg.split("$del",1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"] 
    await message.channel.send(encouragements) 


  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")
   
  
keep_alive()
client.run(my_secret)


# to actually run it 
# we need to add token from web--- that password
# create a .env file to hide all details paswords and stuff
#my_secret = os.environ['Access_Token']


