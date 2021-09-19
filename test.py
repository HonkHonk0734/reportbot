import sqlite3
from colorama.ansi import Fore
import discord
from discord.ext import commands


client = commands.Bot(command_prefix='!',)
print(Fore.GREEN+"Started")

class MyClient(discord.Client):
    async def on_ready(self):
        print(Fore.GREEN+"Logged on as {0}!".format(self.user))

conn = sqlite3.connect('test.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS employees(
            first text,
            last text,
            pay integer
            )""")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

@client.command()
async def test(ctx, *, arg):
    print(arg)
    await ctx.send(arg)

# c.execute("INSERT INTO employees VALUES (?, ?, ?, ?)", (, , , 'report'  ))

# conn.commit()

# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay ))

# conn.commit()

c.execute("SELECT * FROM employees WHERE last='Schrafer'")

print(c.fetchall())

conn.commit()

client = MyClient()

client.run('ODg4MDYxNjQ4OTA3MTQ5MzMz.YUNN3A.ntnrbyefTq5sJvFidz5uFgbjQxg')