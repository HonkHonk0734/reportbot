import discord
import sqlite3
import datetime as dt


conn = sqlite3.connect('userreports.db')

c = conn.cursor()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        current_date = dt.date.today()
        string_date = current_date.strftime('%Y-%m-%d')
        author = message.author
        accused = message.split()[1]
        print(accused)
        print('{0.author} said:\n{0.content} at:\n'.format(message) + string_date )
        # c.execute("INSERT INTO employees VALUES (, 'Schrafer', 50000)")


client = MyClient()

conn.commit()

client.run('ODg4MDYxNjQ4OTA3MTQ5MzMz.YUNN3A.ntnrbyefTq5sJvFidz5uFgbjQxg')