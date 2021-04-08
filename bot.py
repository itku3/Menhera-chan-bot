from discord.ext import commands
import discord
import upbit
import today_anime
import os
import requests
import osu


token = open("token/discord-token.txt", 'r').read()
bot = commands.Bot(command_prefix='>')
'''
prefix에서 봇의 접두어를 설정
'''


@bot.event
async def on_ready():
    # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print('------')
    print(bot.user.name+" : "+str(bot.user.id))
    print("로그인 성공!")
    print('------')


@bot.command()
async def ping(ctx):
    # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. f-string은 위에 서술되어 있다시피 버전 3.6 이상부터 사용 가능하다.
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms')


@bot.command(name="시세")
async def _upbit(ctx):
    embed = discord.Embed(title="UPbit 실시간 시세", color=3426654)
    embed.add_field(name='비트코인', value=str(
        upbit.getTradePrice("KRW-BTC")), inline=False)
    embed.add_field(name='아크', value=str(
        upbit.getTradePrice("KRW-ARK")), inline=False)
    embed.add_field(name='비트토렌트', value=str(
        upbit.getTradePrice("KRW-BTT")), inline=False)
    embed.add_field(name='밀크', value=str(
        upbit.getTradePrice("KRW-MLK")), inline=False)
    embed.add_field(name='헌트', value=str(
        upbit.getTradePrice("KRW-HUNT")), inline=False)
    await ctx.send(embed=embed)


@bot.command(name="업비트")
async def __upbit(ctx, *, text):
    text = text
    market = upbit.getCoinName(text)
    embed = discord.Embed(title=text+"의 현재 가격", color=3426654,
                          description=str(upbit.getTradePrice(market)))
    await ctx.send(embed=embed)


@ bot.command(name="오늘애니")
async def _today_anime(ctx):
    embed = discord.Embed(title="오늘 방영하는 애니 목록입니다!", color=3426654,
                          description='\n'.join(today_anime.getTodayAnime()))
    await ctx.send(embed=embed)


@ bot.command(name="아바타")
async def _avatar(ctx, *, text):
    embed = discord.Embed(title=text+"'s Profile", color=3426654)
    embed.set_image(url=osu.getUserid_and_profileimage(text))
    await ctx.send(embed=embed)


@ bot.command(name="명령어")
async def _help(ctx):
    embed = discord.Embed(title="안녕하세요! 멘헤라쟝 이에요! φ(゜▽゜*)♪", color=3426654)
    embed.add_field(name=">명령어", value="멘헤라쟝의 명령어를 알 수 있어요!", inline=False)
    embed.add_field(name=">오늘애니", value="오늘 방영하는 애니목록을 알 수 있어요!", inline=False)
    embed.add_field(
        name=">업비트 [코인이름]", value="업비트에서 해당 코인의 현재 가격을 알 수 있어요!", inline=False)
    embed.add_field(
        name=">아바타 [유저네임]", value="osu.ppy.sh에서 해당하는 유저의 아바타 프로필을 불러와요!", inline=False)
    await ctx.send(embed=embed)

bot.run(token)
