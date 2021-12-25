'''Invite this wonderful bot to your server today!'''

from discord.ext import commands
from packages.utils import Embed, ImproperType
import requests, json, os
import discord

class Command(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def invite(self, ctx):
      #return await ctx.send('This command is currently under maintenance. The developers will try to get it up again as soon as possible. In the meantime feel free to use `n.help` to get the other commands. Thank you for your understanding!')
      embed = Embed('Here\'s your link!', 'Thank you for deciding to invite this bot to your server!\n\nAdd Lacan NTSport to your server!\n\n**__Invites:__**\n**[Administrator Permissions](https://discord.com/api/oauth2/authorize?client_id=713352863153258556&permissions=8&scope=bot)**\n**[Required Permissions](https://discord.com/api/oauth2/authorize?client_id=713352863153258556&permissions=1514446253281&scope=bot)**\n\n__What we offer:__\n\n:small_blue_diamond:  Unique NT user stats (e.g. settings :gear:) brought to you.\n:small_blue_diamond: Team Stats\n:small_blue_diamond: Car guessing game\n:small_blue_diamond: Typing race\n:small_blue_diamond: Exclusive Nitrotype Hangman\n:small_blue_diamond: Economy system\n:small_blue_diamond:  Register your NT account to the bot!\n:small_blue_diamond: Team competition hosting for a custom amount of time.\n\n__Premium :diamond_shape_with_a_dot_inside: (Run `n.premium` for more info!) :__\n\n:small_orange_diamond: Updating speed, gold, races and registered role through the command `n.update` \n:small_orange_diamond: Updating nickname to `[TAG] Display name`\n:small_orange_diamond: Add team member roles to team members in supported teams.\n\nAdd one of the best NT stats tracking bots to your server **today**! :grinning:.', 'link')
      
      if (ctx.author.id) in [505338178287173642]:
        embed.footer(f'Discord user '+str(ctx.author.name + '#' + ctx.author.discriminator)+' is a 🛠️developer🛠️ of this bot. ', 'https://media.discordapp.net/attachments/719414661686099993/765490220858081280/output-onlinepngtools_32.png')
      else:
        embed.footer(f''+str(ctx.author.name + '#' + ctx.author.discriminator)+' is attempting to invite me to a server.💗 \n Become a premium 💠 member today!', 'https://cdn.discordapp.com/attachments/719414661686099993/754971786231283712/season-callout-badge.png')

      await embed.send(ctx)
      try:
        await ctx.message.delete()
      except:
        pass
def setup(client):
    client.add_cog(Command(client))
