from discord.ext import commands
import discord

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='alliance', aliases=['alli'])
    async def alliance(self, ctx):
        print(dir(ctx.guild))
        print(ctx.guild.roles)
        
        role = discord.utils.get(ctx.author.roles, name='bullets')
        if role:
            new_role = discord.utils.get(ctx.guild.roles, name='welfare')
            await ctx.author.remove_roles(role)
            await ctx.author.add_roles(new_role)
        else:
            role = discord.utils.get(ctx.author.roles, name='welfare')
            new_role = discord.utils.get(ctx.guild.roles, name='bullets')
            await ctx.author.remove_roles(role)
            await ctx.author.add_roles(new_role)
        # await ctx.author.add_roles(role)

def setup(bot):
    bot.add_cog(Commands(bot))