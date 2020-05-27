import os, discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
  print('Answer Scraper Launched')
  answers = client.get_channel(272476376282562560)
  async for message in answers.history():
    message_id = message.id
    created_at = message.created_at
    author = message.author
    content = message.content
    #do what you want with the answers

client.run(TOKEN)