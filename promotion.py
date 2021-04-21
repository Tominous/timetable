import discord


async def vote(ctx):
    await ctx.channel.send(
    embed=discord.Embed(title="Loved Timetable? Then vote it to support!",
    description="Our heart would wish that you voted in both bot lists,\n\
    but your vote on top.gg would be enough.\n\
<:topgg:834421312994279535>  [top.gg](https://top.gg/bot/789202881336311849/vote) (waiting to be verified)\n\
<:discordbotlist:834424137224814642>  [DiscordBotList](https://discordbotlist.com/bots/timetable/upvote)\n\
<:discordboats:834424137174614086>  [Discord Boats](https://discord.boats/bot/789202881336311849/vote)\n\
**We don't earn money from your votes!**",
    colour=0xACB6C4))


async def invite(ctx):
    await ctx.channel.send(
    embed=discord.Embed(title="Loved Timetable? Then invite it to other servers!",
    description="Invite link can be found at:\n\
<:topgg:834421312994279535>  [top.gg](https://top.gg/bot/789202881336311849) (waiting to be verified)\n\
<:botsgg:834424137631006720>  [bots.gg](https://discord.bots.gg/bots/789202881336311849) (waiting to be verified)\n\
<:discordbotlist:834424137224814642>  [DiscordBotList](https://discordbotlist.com/bots/timetable)\n\
<:discordboats:834424137174614086>  [Discord Boats](https://discord.boats/bot/789202881336311849)",
    colour=0xACB6C4))
