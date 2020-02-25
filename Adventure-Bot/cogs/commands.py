from discord.ext import commands
import discord

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='alliance', aliases=['alli'])
    async def alliance(self, ctx):
        
        role = discord.utils.get(ctx.author.roles, name='Bullets')
        if role:
            new_role = discord.utils.get(ctx.guild.roles, name='Welfare')
        else:
            role = discord.utils.get(ctx.author.roles, name='Welfare')
            new_role = discord.utils.get(ctx.guild.roles, name='Bullets')
        await ctx.author.remove_roles(role)
        await ctx.author.add_roles(new_role)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            pass
        else:
            await message.channel.send(f'Hi, {message.author.mention}')
            print(dir(message.author))

def setup(bot):
    bot.add_cog(Commands(bot))
