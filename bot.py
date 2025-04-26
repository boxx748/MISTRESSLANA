import discord
import random
import asyncio
import json
import os
from discord.ext import commands

# קריאת קובץ config.json לפרמטרים האחרים
with open('config.json') as f:
    config = json.load(f)

TOKEN = os.getenv("TOKEN")  # קריאת הטוקן מה-Environment ולא מה-config

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=config['PREFIX'], intents=intents)

TASKS = [
    "זחילה עירום מול מראה עם צילום.",
    "כתוב 200 פעמים 'אני חסר ערך'.",
    "שלח הודעת קול מביישת למיסטרס.",
    "אדג'ינג 5 פעמים ביום ללא גמירה.",
    "לבוש בגדי נשים 24 שעות עם תיעוד.",
    "שינה עם פלאג, שלח הוכחת בוקר.",
    "כריעה מול מראה ל-10 דקות עם צילום.",
    "מקלחת קרה 10 דקות.",
    "ספנקינג עצמי 100 חבטות.",
    "Ruined orgasm ותיעוד.",
    "ליקוק רצפה 10 פעמים עם צילום.",
    "לבישת חגורת צניעות 24 שעות.",
    "יומן השפלה יומי.",
    "כריעה שקטה 30 דקות.",
    "תרגול שליטה בנשימה.",
    "תחנונים בקול רם למיסטרס.",
    "כתיבת מכתב התנצלות מלא.",
    "קיפאון מוחלט 30 דקות.",
    "ליקוק נעליים 20 פעמים.",
    "שימוש בגאג שעתיים.",
    "צביטות עצמיות באזור רגיש.",
    "לבוש מביך וצילום.",
    "אוננות עד גבול גמירה חמש פעמים.",
    "עמידה בפינה 20 דקות.",
    "בקש עונש נוסף ישירות.",
    "הקלטת נאום בושה אישי.",
    "שליחת הודעת 'אני כלום' לחברים.",
    "זחילה ממושכת תוך קריאות השפלה.",
    "ציור לב על הגוף עם הכיתוב: 'Property of Mistress Lana'.",
    "כתיבת שיר השפלה אישי.",
    "צפייה בסרטון בושה ודיווח קולי."
]

async def send_task_every_two_hours():
    await bot.wait_until_ready()
    channel = discord.utils.get(bot.get_all_channels(), name="general")
    while not bot.is_closed():
        if channel:
            task = random.choice(TASKS)
            await channel.send(f"רפאל... המשימה שלך עכשיו: **{task}**")
        await asyncio.sleep(7200)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    bot.loop.create_task(send_task_every_two_hours())

@bot.command()
async def משימה(ctx):
    task = random.choice(TASKS)
    await ctx.send(f"{ctx.author.mention} המשימה שלך: **{task}**")

@bot.command()
async def כניעה(ctx):
    responses = [
        "כניעה? עונש משולש בדרך.",
        "כניעה התקבלה. אך זה יכאב מאוד.",
        "אין רחמים. מצפה לעונש קשה יותר."
    ]
    await ctx.send(random.choice(responses))

bot.run(TOKEN)
