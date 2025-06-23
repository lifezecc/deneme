import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot çalışıyor: {bot.user}")

@bot.event
async def on_member_remove(member):
    try:
        await member.guild.ban(member, reason="Sunucudan ayrıldığı için otomatik banlandı.")
        print(f"{member} sunucudan ayrıldı ve banlandı.")
    except Exception as e:
        print(f"Hata: {e}")

bot.run("MTM4NjQyMjg5ODg5MzM4OTg3NQ.GusRFb.pTixxUNuGNOs_H20vBkw7Y4fkkLJKkqAmd7FQs")  # <-- kendi bot token'ını buraya gir
