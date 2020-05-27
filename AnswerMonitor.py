import os, discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print('Answer Monitor Launch')

@client.event
async def on_message(message):
  message_id = message.id
  created_at = message.created_at
  author = message.author
  content = message.content
  #do what you want with the answers

client.run(TOKEN)